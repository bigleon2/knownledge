#!/usr/bin/env python3
"""
🔍 Analyse des logs système des dernières 24h
==============================================

Script Python qui analyse les logs système Linux pour détecter :
- Erreurs critiques (ERROR, CRITICAL, FAIL, PANIC)
- Tentatives d'authentification échouées (sécurité)
- Redémarrages de services (systemd)
- Problèmes mémoire (OOM Killer)
- Activités suspectes
- Statistiques globales

Auteur : François (orchestré par python-executor agent)
Date : 2026-06-21
Version : 1.0.0
"""

import os
import re
import sys
import glob
import socket
import platform
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from pathlib import Path

# === Configuration ===
LOGS_DIR = Path('/var/log')
REPORT_DIR = Path('/home/z/my-project/reports')
TIMELINE_HOURS = 24

# Patterns de détection
PATTERNS = {
    'errors': re.compile(r'\b(ERROR|CRITICAL|FAIL|FAILED|PANIC|EMERG|ALERT)\b', re.IGNORECASE),
    'warnings': re.compile(r'\b(WARNING|WARN)\b', re.IGNORECASE),
    'auth_fail': re.compile(r'(authentication failure|Failed password|Invalid user|access denied|refused)', re.IGNORECASE),
    'auth_success': re.compile(r'(Accepted password|session opened|Successful login)', re.IGNORECASE),
    'oom': re.compile(r'(Out of memory|oom-killer|killed process)', re.IGNORECASE),
    'service_restart': re.compile(r'(Started|Stopped|Restarting|Unit .* entered failed state)', re.IGNORECASE),
    'kernel': re.compile(r'kernel:', re.IGNORECASE),
    'sudo': re.compile(r'sudo:.*COMMAND=', re.IGNORECASE),
    'usb': re.compile(r'(usb|new USB device|USB disconnect)', re.IGNORECASE),
    'network': re.compile(r'(NetworkManager|eth|wlan|link up|link down)', re.IGNORECASE),
}

# Fichiers de logs à analyser (par ordre de priorité)
LOG_FILES = [
    'syslog',
    'messages',
    'auth.log',
    'secure',
    'kern.log',
    'daemon.log',
    'kern.log',
    'boot.log',
    'dpkg.log',
    'apt/history.log',
]


class LogAnalyzer:
    """Analyseur de logs système."""
    
    def __init__(self, hours=24):
        self.hours = hours
        self.cutoff_time = datetime.now() - timedelta(hours=hours)
        self.stats = {
            'total_lines': 0,
            'relevant_lines': 0,
            'files_analyzed': 0,
            'files_skipped': 0,
            'errors': 0,
            'warnings': 0,
            'auth_failures': 0,
            'auth_success': 0,
            'oom_events': 0,
            'service_restarts': 0,
            'sudo_commands': 0,
        }
        self.findings = defaultdict(list)
        self.ip_failures = Counter()
        self.user_failures = Counter()
        self.services_affected = Counter()
        self.error_messages = Counter()
        self.timeline = defaultdict(lambda: defaultdict(int))
    
    def parse_syslog_date(self, line):
        """Extrait la date d'une ligne de log syslog."""
        # Format syslog classique : "Jun 21 14:23:45"
        match = re.match(r'^(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})', line)
        if match:
            date_str = match.group(1)
            try:
                # Ajouter l'année courante
                current_year = datetime.now().year
                parsed = datetime.strptime(f"{current_year} {date_str}", "%Y %b %d %H:%M:%S")
                return parsed
            except ValueError:
                return None
        return None
    
    def analyze_line(self, line, source_file):
        """Analyse une ligne de log."""
        self.stats['total_lines'] += 1
        
        # Extraction de la date
        log_time = self.parse_syslog_date(line)
        
        # Filtrer par période
        if log_time and log_time < self.cutoff_time:
            return
        
        self.stats['relevant_lines'] += 1
        
        # Timeline par heure
        if log_time:
            hour_key = log_time.strftime("%Y-%m-%d %H:00")
        
        # Détection des patterns
        for category, pattern in PATTERNS.items():
            if pattern.search(line):
                self.stats[category] = self.stats.get(category, 0) + 1
                
                # Enregistrer la découverte
                finding = {
                    'time': log_time.strftime("%H:%M:%S") if log_time else "??:??:??",
                    'source': source_file.name,
                    'message': line.strip()[:200],
                }
                
                # Limiter le nombre de findings par catégorie
                if len(self.findings[category]) < 50:
                    self.findings[category].append(finding)
                
                # Statistiques spécifiques
                if category == 'auth_fail':
                    # Extraire IP
                    ip_match = re.search(r'from\s+(\d+\.\d+\.\d+\.\d+)', line)
                    if ip_match:
                        self.ip_failures[ip_match.group(1)] += 1
                    
                    # Extraire utilisateur
                    user_match = re.search(r'(?:user|for)\s+(\w+)', line)
                    if user_match:
                        self.user_failures[user_match.group(1)] += 1
                
                if category == 'errors':
                    # Extraire le message d'erreur (sans timestamp ni host)
                    msg_match = re.search(r':\s*(.+)$', line)
                    if msg_match:
                        short_msg = msg_match.group(1).strip()[:100]
                        self.error_messages[short_msg] += 1
                
                if category == 'service_restart':
                    svc_match = re.search(r'(\w+\.service|\w+)', line)
                    if svc_match:
                        self.services_affected[svc_match.group(1)] += 1
                
                # Timeline
                if log_time:
                    self.timeline[hour_key][category] += 1
                
                break  # Une ligne = une catégorie max
    
    def analyze_file(self, filepath):
        """Analyse un fichier de log."""
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    self.analyze_line(line, filepath)
            self.stats['files_analyzed'] += 1
            return True
        except PermissionError:
            self.stats['files_skipped'] += 1
            return False
        except Exception as e:
            print(f"  ⚠️  Erreur lecture {filepath}: {e}")
            self.stats['files_skipped'] += 1
            return False
    
    def analyze_rotated_logs(self, base_name):
        """Analyse un log et ses rotations (.1, .2.gz, etc.)."""
        patterns = [
            LOGS_DIR / base_name,
            LOGS_DIR / f"{base_name}.1",
            LOGS_DIR / f"{base_name}.0",
        ]
        
        # Chercher aussi les logs compressés
        for p in LOGS_DIR.glob(f"{base_name}.*"):
            if p.suffix in ['.gz', '.xz', '.bz2']:
                continue  # Skip compressés pour simplicité
            patterns.append(p)
        
        for pattern in patterns:
            if pattern.exists() and pattern.is_file():
                self.analyze_file(pattern)
    
    def run(self):
        """Lance l'analyse complète."""
        print("=" * 70)
        print(f"🔍 ANALYSE DES LOGS SYSTÈME — {self.hours} dernières heures")
        print("=" * 70)
        print(f"📅 Période : depuis {self.cutoff_time.strftime('%Y-%m-%d %H:%M')}")
        print(f"🖥️  Système : {platform.node()} ({platform.system()} {platform.release()})")
        print(f"📁 Répertoire logs : {LOGS_DIR}")
        print()
        
        # Analyse des fichiers de logs
        print("📊 Analyse des fichiers...")
        for log_file in LOG_FILES:
            log_path = LOGS_DIR / log_file
            if log_path.exists():
                print(f"  → {log_file}")
                self.analyze_rotated_logs(log_file)
        
        # Analyse de dmesg (logs kernel)
        print("  → dmesg (kernel)")
        try:
            import subprocess
            result = subprocess.run(['dmesg', '--time-format=iso'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.splitlines():
                    self.analyze_line(line, Path('dmesg'))
        except Exception as e:
            print(f"  ⚠️  dmesg non disponible: {e}")
        
        # Analyse journalctl si disponible
        print("  → journalctl (systemd)")
        try:
            import subprocess
            result = subprocess.run(
                ['journalctl', '--since', f'{self.hours} hours ago', '--no-pager', '-q'],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                for line in result.stdout.splitlines():
                    self.analyze_line(line, Path('journalctl'))
        except Exception as e:
            print(f"  ⚠️  journalctl non disponible: {e}")
        
        print()
        print("✅ Analyse terminée")
        print()
    
    def generate_report(self):
        """Génère un rapport Markdown."""
        report_lines = []
        
        # En-tête
        report_lines.append("# 🔍 Rapport d'Analyse des Logs Système")
        report_lines.append("")
        report_lines.append(f"**Date d'analyse** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"**Période analysée** : {self.hours} dernières heures")
        report_lines.append(f"**Système** : {platform.node()} ({platform.system()} {platform.release()})")
        report_lines.append(f"**Kernel** : {platform.version()}")
        report_lines.append("")
        
        # Résumé statistique
        report_lines.append("## 📊 Résumé Statistique")
        report_lines.append("")
        report_lines.append("| Indicateur | Valeur |")
        report_lines.append("|------------|--------|")
        report_lines.append(f"| Lignes totales analysées | {self.stats['total_lines']:,} |")
        report_lines.append(f"| Lignes pertinentes (< {self.hours}h) | {self.stats['relevant_lines']:,} |")
        report_lines.append(f"| Fichiers analysés | {self.stats['files_analyzed']} |")
        report_lines.append(f"| Fichiers ignorés (permissions) | {self.stats['files_skipped']} |")
        report_lines.append(f"| 🔴 Erreurs critiques | {self.stats['errors']} |")
        report_lines.append(f"| 🟡 Avertissements | {self.stats['warnings']} |")
        report_lines.append(f"| 🔐 Échecs d'authentification | {self.stats['auth_failures']} |")
        report_lines.append(f"| ✅ Authentifications réussies | {self.stats['auth_success']} |")
        report_lines.append(f"| 💀 OOM Killer events | {self.stats['oom_events']} |")
        report_lines.append(f"| 🔄 Redémarrages de services | {self.stats['service_restarts']} |")
        report_lines.append(f"| 👤 Commandes sudo | {self.stats['sudo_commands']} |")
        report_lines.append("")
        
        # Score de santé
        health_score = self.calculate_health_score()
        health_emoji = "🟢" if health_score >= 80 else "🟡" if health_score >= 50 else "🔴"
        report_lines.append(f"### {health_emoji} Score de santé système : **{health_score}/100**")
        report_lines.append("")
        
        # Analyse de sécurité
        if self.stats['auth_failures'] > 0:
            report_lines.append("## 🔐 Analyse de Sécurité")
            report_lines.append("")
            report_lines.append(f"**{self.stats['auth_failures']} tentatives d'authentification échouées** détectées.")
            report_lines.append("")
            
            if self.ip_failures:
                report_lines.append("### 🌐 Top 10 IPs suspectes")
                report_lines.append("")
                report_lines.append("| IP | Tentatives |")
                report_lines.append("|----|------------|")
                for ip, count in self.ip_failures.most_common(10):
                    report_lines.append(f"| `{ip}` | {count} |")
                report_lines.append("")
                
                # Alerte brute force
                top_ip, top_count = self.ip_failures.most_common(1)[0]
                if top_count > 20:
                    report_lines.append(f"⚠️ **ALERTE** : IP `{top_ip}` a tenté {top_count} connexions → possible attaque brute force")
                    report_lines.append("")
            
            if self.user_failures:
                report_lines.append("### 👤 Top 10 utilisateurs ciblés")
                report_lines.append("")
                report_lines.append("| Utilisateur | Tentatives |")
                report_lines.append("|-------------|------------|")
                for user, count in self.user_failures.most_common(10):
                    report_lines.append(f"| `{user}` | {count} |")
                report_lines.append("")
        
        # Erreurs critiques
        if self.stats['errors'] > 0:
            report_lines.append("## 🔴 Erreurs Critiques")
            report_lines.append("")
            report_lines.append(f"**{self.stats['errors']} erreurs critiques** détectées.")
            report_lines.append("")
            
            if self.error_messages:
                report_lines.append("### Top 10 erreurs les plus fréquentes")
                report_lines.append("")
                for msg, count in self.error_messages.most_common(10):
                    report_lines.append(f"- **{count}×** : `{msg}`")
                report_lines.append("")
            
            # Dernières erreurs
            if self.findings['errors']:
                report_lines.append("### Dernières erreurs")
                report_lines.append("")
                for finding in self.findings['errors'][-10:]:
                    report_lines.append(f"- **[{finding['time']}]** ({finding['source']}) {finding['message']}")
                report_lines.append("")
        
        # OOM Events
        if self.stats['oom_events'] > 0:
            report_lines.append("## 💀 OOM Killer Events")
            report_lines.append("")
            report_lines.append(f"**{self.stats['oom_events']} processus tués par manque de mémoire**.")
            report_lines.append("")
            report_lines.append("⚠️ **Recommandation** : Vérifier la consommation mémoire et envisager d'ajouter de la RAM.")
            report_lines.append("")
        
        # Services affectés
        if self.services_affected:
            report_lines.append("## 🔄 Services Affectés")
            report_lines.append("")
            report_lines.append("| Service | Événements |")
            report_lines.append("|---------|------------|")
            for svc, count in self.services_affected.most_common(15):
                report_lines.append(f"| `{svc}` | {count} |")
            report_lines.append("")
        
        # Timeline
        if self.timeline:
            report_lines.append("## 📈 Timeline (par heure)")
            report_lines.append("")
            report_lines.append("| Heure | Erreurs | Warnings | Auth Fail | Autres |")
            report_lines.append("|-------|---------|----------|-----------|--------|")
            for hour in sorted(self.timeline.keys())[-24:]:  # 24 dernières heures
                data = self.timeline[hour]
                errors = data.get('errors', 0)
                warnings = data.get('warnings', 0)
                auth = data.get('auth_fail', 0)
                others = sum(v for k, v in data.items() if k not in ['errors', 'warnings', 'auth_fail'])
                report_lines.append(f"| {hour} | {errors} | {warnings} | {auth} | {others} |")
            report_lines.append("")
        
        # Recommandations
        report_lines.append("## 💡 Recommandations")
        report_lines.append("")
        
        recommendations = []
        
        if self.stats['auth_failures'] > 50:
            recommendations.append("- 🔐 **Sécurité** : Nombre élevé d'échecs d'auth. Envisager fail2ban ou configurer SSH par clés uniquement.")
        
        if self.ip_failures and self.ip_failures.most_common(1)[0][1] > 20:
            recommendations.append("- 🚫 **Blocage IP** : Envisager de bloquer les IPs suspectes via iptables ou fail2ban.")
        
        if self.stats['oom_events'] > 0:
            recommendations.append("- 💾 **Mémoire** : OOM events détectés. Surveiller la RAM et optimiser les processus gourmands.")
        
        if self.stats['errors'] > 100:
            recommendations.append("- 🔍 **Investigation** : Nombre élevé d'erreurs. Examiner les services concernés en détail.")
        
        if self.stats['service_restarts'] > 20:
            recommendations.append("- 🔄 **Stabilité** : Redémarrages fréquents de services. Vérifier la configuration et les dépendances.")
        
        if not recommendations:
            recommendations.append("- ✅ **Système stable** : Aucune action corrective majeure nécessaire.")
        
        for rec in recommendations:
            report_lines.append(rec)
        
        report_lines.append("")
        report_lines.append("---")
        report_lines.append(f"*Rapport généré le {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} par analyze_logs.py v1.0.0*")
        
        return '\n'.join(report_lines)
    
    def calculate_health_score(self):
        """Calcule un score de santé du système (0-100)."""
        score = 100
        
        # Pénalités
        score -= min(30, self.stats['errors'] // 5)  # -1 par 5 erreurs, max -30
        score -= min(20, self.stats['oom_events'] * 10)  # -10 par OOM
        score -= min(15, self.stats['auth_failures'] // 10)  # -1 par 10 auth fail
        score -= min(10, self.stats['service_restarts'] // 5)  # -1 par 5 restarts
        score -= min(10, self.stats['warnings'] // 20)  # -1 par 20 warnings
        
        return max(0, score)
    
    def save_report(self, report_text):
        """Sauvegarde le rapport."""
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_path = REPORT_DIR / f'log_analysis_{timestamp}.md'
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_text)
        
        return report_path


def main():
    """Point d'entrée principal."""
    analyzer = LogAnalyzer(hours=TIMELINE_HOURS)
    
    # Lancer l'analyse
    analyzer.run()
    
    # Générer le rapport
    report = analyzer.generate_report()
    
    # Afficher le rapport
    print(report)
    
    # Sauvegarder
    report_path = analyzer.save_report(report)
    print()
    print("=" * 70)
    print(f"💾 Rapport sauvegardé : {report_path}")
    print("=" * 70)
    
    # Résumé rapide
    print()
    print("📊 RÉSUMÉ RAPIDE :")
    print(f"   🔴 Erreurs : {analyzer.stats['errors']}")
    print(f"   🟡 Warnings : {analyzer.stats['warnings']}")
    print(f"   🔐 Auth failures : {analyzer.stats['auth_failures']}")
    print(f"   💀 OOM events : {analyzer.stats['oom_events']}")
    print(f"   🖥️  Score santé : {analyzer.calculate_health_score()}/100")


if __name__ == "__main__":
    main()