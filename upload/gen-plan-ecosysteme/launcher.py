#!/usr/bin/env python3
"""
🚀 Launcher Multi-Contexte IA avec Auto-Détection
===================================================

Ce script lance automatiquement une session IA avec le prompt maître adapté
au contexte (système ou codage). Il supporte l'auto-détection du contexte.

Contextes supportés :
    - system  : Ingénieur système (z.ai par défaut)
                Administration, orchestration, hardware DJ, TSI, automatisation
    - code    : Développement (qwen par défaut)
                Python, C/C++, Next.js, APIs, scripts audio

IA Supportées (par ordre de préférence) :
    1. z.ai       (Zhipu AI / GLM)
    2. qwen       (Alibaba Qwen)
    3. manus      (Manus AI)
    4. copilot    (Microsoft Copilot)
    5. chatgpt    (OpenAI ChatGPT)
    6. perplexity (Perplexity AI)
    7. gemini     (Google Gemini)
    8. claude     (Anthropic Claude)
    9. codex      (OpenAI Codex)

Usage :
    python3 launcher.py [contexte] [ia] [--auto]
    
    contexte : system | code (optionnel, défaut: auto-détection)
    ia       : Nom de l'IA (optionnel, défaut: selon contexte)
    --auto   : Force l'auto-détection
    --list   : Liste les contextes et IA
    --config : Configure les IA par défaut par contexte

Exemples :
    python3 launcher.py                    # Auto-détection contexte + IA
    python3 launcher.py system             # Contexte système, IA auto
    python3 launcher.py code               # Contexte codage, IA auto
    python3 launcher.py system qwen        # Système sur qwen
    python3 launcher.py code chatgpt       # Codage sur ChatGPT
    python3 launcher.py --config           # Configure IA par défaut

Configuration par défaut :
    - system → z.ai (ingénieur système)
    - code   → qwen (développement)

Auteur : François (orchestré par Qwen3.7)
Date : 2026-06-21
Version : 3.0.0
"""

import sys
import os
import webbrowser
import json
from pathlib import Path
from datetime import datetime

# === Configuration ===
PROJECT_DIR = Path('/home/z/my-project')
PROMPT_SYSTEM = PROJECT_DIR / 'prompt-maitre-system.md'
PROMPT_CODE = PROJECT_DIR / 'prompt-maitre-code.md'
PROMPT_UNIVERSAL = PROJECT_DIR / 'prompt-maitre.md'

CONFIG_DIR = Path.home() / '.config' / 'ai-launcher'
CONFIG_FILE = CONFIG_DIR / 'config.json'
HISTORY_FILE = CONFIG_DIR / 'history.json'

# === URLs des IA ===
IA_URLS = {
    'z.ai': 'https://chat.z.ai/',
    'qwen': 'https://chat.qwen.ai/',
    'manus': 'https://manus.im/',
    'copilot': 'https://copilot.microsoft.com/',
    'chatgpt': 'https://chat.openai.com/',
    'perplexity': 'https://www.perplexity.ai/',
    'gemini': 'https://gemini.google.com/',
    'claude': 'https://claude.ai/new',
    'codex': 'https://chat.openai.com/?model=codex'
}

# === Contextes ===
CONTEXTS = {
    'system': {
        'name': 'Ingénieur Système',
        'description': 'Administration, orchestration, hardware DJ, TSI, automatisation',
        'default_ia': 'z.ai',
        'prompt_file': 'prompt-maitre-system.md'
    },
    'code': {
        'name': 'Développement',
        'description': 'Python, C/C++, Next.js, APIs, scripts audio',
        'default_ia': 'qwen',
        'prompt_file': 'prompt-maitre-code.md'
    }
}

# === Ordre de préférence ===
IA_PREFERENCE = [
    'z.ai', 'qwen', 'manus', 'copilot', 'chatgpt',
    'perplexity', 'gemini', 'claude', 'codex'
]


def ensure_config_dir():
    """Crée le répertoire de configuration s'il n'existe pas."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def load_config():
    """Charge la configuration utilisateur."""
    ensure_config_dir()
    default_config = {
        'contexts': {
            'system': {'default_ia': 'z.ai'},
            'code': {'default_ia': 'qwen'}
        },
        'last_context': None,
        'last_ia': None
    }
    
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
                config = json.load(f)
                # Merge avec défauts
                for key, value in default_config.items():
                    if key not in config:
                        config[key] = value
                return config
        except Exception as e:
            print(f"⚠️  Erreur lecture config: {e}")
    
    return default_config


def save_config(config):
    """Sauvegarde la configuration utilisateur."""
    ensure_config_dir()
    try:
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️  Erreur sauvegarde config: {e}")


def load_history():
    """Charge l'historique des sessions."""
    ensure_config_dir()
    if HISTORY_FILE.exists():
        try:
            with open(HISTORY_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            pass
    return {'sessions': []}


def save_history(history):
    """Sauvegarde l'historique des sessions."""
    ensure_config_dir()
    try:
        with open(HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️  Erreur sauvegarde historique: {e}")


def add_to_history(context, ia_name):
    """Ajoute une session à l'historique."""
    history = load_history()
    history['sessions'].append({
        'context': context,
        'ia': ia_name,
        'timestamp': datetime.now().isoformat()
    })
    history['sessions'] = history['sessions'][-50:]
    save_history(history)


def get_most_used_ia_for_context(context):
    """Retourne l'IA la plus utilisée pour un contexte donné."""
    history = load_history()
    if not history['sessions']:
        return None
    
    counts = {}
    for session in history['sessions'][-20:]:
        if session.get('context') == context:
            ia = session['ia']
            counts[ia] = counts.get(ia, 0) + 1
    
    if counts:
        return max(counts, key=counts.get)
    return None


def detect_context():
    """Détecte automatiquement le contexte."""
    # 1. Variable d'environnement
    env_context = os.environ.get('IA_CONTEXT')
    if env_context and env_context in CONTEXTS:
        return env_context
    
    # 2. Configuration utilisateur (dernier contexte)
    config = load_config()
    if config.get('last_context') and config['last_context'] in CONTEXTS:
        return config['last_context']
    
    # 3. Historique (contexte le plus utilisé)
    history = load_history()
    if history['sessions']:
        context_counts = {}
        for session in history['sessions'][-20:]:
            ctx = session.get('context')
            if ctx:
                context_counts[ctx] = context_counts.get(ctx, 0) + 1
        if context_counts:
            return max(context_counts, key=context_counts.get)
    
    # 4. Défaut : system
    return 'system'


def detect_ia(context):
    """Détecte automatiquement l'IA pour un contexte donné."""
    config = load_config()
    
    # 1. Variable d'environnement
    env_ia = os.environ.get('IA_DEFAULT')
    if env_ia and env_ia in IA_URLS:
        return env_ia
    
    # 2. Configuration du contexte
    context_config = config.get('contexts', {}).get(context, {})
    default_ia = context_config.get('default_ia')
    if default_ia and default_ia in IA_URLS:
        return default_ia
    
    # 3. Historique pour ce contexte
    most_used = get_most_used_ia_for_context(context)
    if most_used:
        return most_used
    
    # 4. Défaut du contexte
    return CONTEXTS[context]['default_ia']


def get_prompt_path(context):
    """Retourne le chemin du prompt maître pour un contexte."""
    context_info = CONTEXTS.get(context)
    if not context_info:
        return PROMPT_UNIVERSAL
    
    prompt_file = PROJECT_DIR / context_info['prompt_file']
    if prompt_file.exists():
        return prompt_file
    
    # Fallback vers prompt universel
    if PROMPT_UNIVERSAL.exists():
        return PROMPT_UNIVERSAL
    
    return None


def charger_prompt(context):
    """Charge le prompt maître depuis le fichier."""
    prompt_path = get_prompt_path(context)
    
    if not prompt_path or not prompt_path.exists():
        print(f"❌ Fichier prompt maître non trouvé pour contexte '{context}'")
        print(f"   Chemin attendu: {prompt_path}")
        sys.exit(1)
    
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Erreur lecture prompt maître: {e}")
        sys.exit(1)


def copier_presse_papier(texte):
    """Copie le texte dans le presse-papier."""
    try:
        import pyperclip
        pyperclip.copy(texte)
        return True
    except ImportError:
        print("⚠️  pyperclip non installé. Installation...")
        os.system('pip install pyperclip')
        try:
            import pyperclip
            pyperclip.copy(texte)
            return True
        except Exception as e:
            print(f"❌ Erreur copie presse-papier: {e}")
            return False
    except Exception as e:
        print(f"❌ Erreur copie presse-papier: {e}")
        return False


def ouvrir_navigateur(url):
    """Ouvre l'URL dans le navigateur par défaut."""
    try:
        webbrowser.open(url)
        return True
    except Exception as e:
        print(f"❌ Erreur ouverture navigateur: {e}")
        return False


def menu_contexte():
    """Affiche un menu pour choisir le contexte."""
    print("\n🎯 Choisissez le contexte :")
    print("-" * 60)
    
    for i, (key, ctx) in enumerate(CONTEXTS.items(), 1):
        config = load_config()
        default_ia = config.get('contexts', {}).get(key, {}).get('default_ia', CONTEXTS[key]['default_ia'])
        print(f"  {i}. {ctx['name']:20} ({key:6}) → {default_ia}")
        print(f"     {ctx['description']}")
    
    print("-" * 60)
    print("  0. Annuler")
    print()
    
    while True:
        try:
            choix = input("Votre choix (0-2) : ").strip()
            
            if choix == '0':
                return None
            
            if choix.isdigit():
                index = int(choix) - 1
                keys = list(CONTEXTS.keys())
                if 0 <= index < len(keys):
                    return keys[index]
            
            print("❌ Choix invalide. Essayez encore.")
        except KeyboardInterrupt:
            print("\n\nAnnulation.")
            return None
        except EOFError:
            return None


def menu_ia():
    """Affiche un menu pour choisir l'IA."""
    print("\n🤖 Choisissez l'IA :")
    print("-" * 50)
    
    for i, ia in enumerate(IA_PREFERENCE, 1):
        url = IA_URLS[ia]
        print(f"  {i}. {ia:15} → {url}")
    
    print("-" * 50)
    print("  0. Annuler")
    print()
    
    while True:
        try:
            choix = input("Votre choix (0-9) : ").strip()
            
            if choix == '0':
                return None
            
            if choix.isdigit():
                index = int(choix) - 1
                if 0 <= index < len(IA_PREFERENCE):
                    return IA_PREFERENCE[index]
            
            print("❌ Choix invalide. Essayez encore.")
        except KeyboardInterrupt:
            print("\n\nAnnulation.")
            return None
        except EOFError:
            return None


def configurer_ia_defaut():
    """Configure les IA par défaut pour chaque contexte."""
    print("\n⚙️  Configuration des IA par défaut par contexte")
    print("=" * 60)
    
    config = load_config()
    
    for context_key, context_info in CONTEXTS.items():
        print(f"\n📋 Contexte : {context_info['name']} ({context_key})")
        print(f"   Description : {context_info['description']}")
        print(f"   IA actuelle : {config['contexts'].get(context_key, {}).get('default_ia', 'non définie')}")
        
        choix = input(f"   Changer l'IA par défaut ? (o/N) : ").strip().lower()
        if choix == 'o':
            ia = menu_ia()
            if ia:
                if 'contexts' not in config:
                    config['contexts'] = {}
                if context_key not in config['contexts']:
                    config['contexts'][context_key] = {}
                config['contexts'][context_key]['default_ia'] = ia
                print(f"   ✅ IA par défaut configurée : {ia}")
    
    save_config(config)
    print("\n✅ Configuration sauvegardée")


def lister_config():
    """Liste les contextes et IA configurés."""
    print("\n🎯 Contextes et IA Supportées")
    print("=" * 70)
    
    config = load_config()
    
    print("\n📋 CONTEXTES :")
    print("-" * 70)
    for key, ctx in CONTEXTS.items():
        default_ia = config.get('contexts', {}).get(key, {}).get('default_ia', ctx['default_ia'])
        last_used = config.get('last_context') == key
        marker = " ← DERNIER UTILISÉ" if last_used else ""
        
        print(f"\n{ctx['name']} ({key}){marker}")
        print(f"  Description : {ctx['description']}")
        print(f"  IA par défaut : {default_ia} ({IA_URLS.get(default_ia, 'N/A')})")
        print(f"  Prompt : {ctx['prompt_file']}")
    
    print("\n\n🤖 IA SUPPORTÉES :")
    print("-" * 70)
    for i, ia in enumerate(IA_PREFERENCE, 1):
        url = IA_URLS[ia]
        print(f"{i}. {ia:15} {url}")
    
    print("=" * 70)
    
    # Statistiques d'utilisation
    history = load_history()
    if history['sessions']:
        print(f"\n📊 Statistiques (20 dernières sessions) :")
        context_counts = {}
        ia_counts = {}
        for session in history['sessions'][-20:]:
            ctx = session.get('context', 'inconnu')
            ia = session.get('ia', 'inconnu')
            context_counts[ctx] = context_counts.get(ctx, 0) + 1
            ia_counts[ia] = ia_counts.get(ia, 0) + 1
        
        print(f"  Contextes : {', '.join(f'{k} ({v})' for k, v in context_counts.items())}")
        print(f"  IA : {', '.join(f'{k} ({v})' for k, v in ia_counts.items())}")


def lancer_session(context, ia_name):
    """Lance une session avec le contexte et l'IA spécifiés."""
    context_info = CONTEXTS.get(context, {})
    context_name = context_info.get('name', context)
    
    print(f"\n🚀 Lancement session")
    print(f"   Contexte : {context_name} ({context})")
    print(f"   IA       : {ia_name}")
    print(f"   URL      : {IA_URLS.get(ia_name, 'N/A')}")
    
    # Charger le prompt maître
    prompt_path = get_prompt_path(context)
    print(f"   Prompt   : {prompt_path.name if prompt_path else 'N/A'}")
    print()
    
    prompt = charger_prompt(context)
    
    # Copier dans le presse-papier
    if copier_presse_papier(prompt):
        print("✅ Prompt maître copié dans le presse-papier")
    else:
        print("❌ Échec copie presse-papier")
        return False
    
    # Ouvrir le navigateur
    url = IA_URLS[ia_name]
    if ouvrir_navigateur(url):
        print(f"🌐 Navigateur ouvert : {url}")
    else:
        print("❌ Échec ouverture navigateur")
        return False
    
    # Mettre à jour l'historique et la config
    add_to_history(context, ia_name)
    config = load_config()
    config['last_context'] = context
    config['last_ia'] = ia_name
    save_config(config)
    
    print()
    print("=" * 70)
    print("👉 Instructions :")
    print("   1. Allez dans le navigateur (onglet ouvert)")
    print("   2. Collez le prompt maître (Ctrl+V ou Cmd+V)")
    print("   3. L'IA dira 'Yes' ou 'Compris'")
    print("   4. Vous pouvez commencer à travailler !")
    print()
    print(f"💡 Astuce : Utilisez les alias pour plus de rapidité :")
    print(f"   - 'sys'     → Lance {context_name} sur {ia_name}")
    print(f"   - 'code'    → Lance Développement sur qwen")
    print(f"   - 'sys qwen' → Lance Système sur qwen")
    print("=" * 70)
    
    return True


def main():
    """Fonction principale."""
    args = sys.argv[1:]
    
    # Commandes spéciales
    if '--list' in args:
        lister_config()
        return
    
    if '--config' in args:
        configurer_ia_defaut()
        return
    
    # Parser les arguments
    force_auto = '--auto' in args
    args_clean = [a for a in args if not a.startswith('--')]
    
    contexte_specifie = None
    ia_specifiee = None
    
    # Premier argument = contexte (si valide)
    if len(args_clean) >= 1 and args_clean[0] in CONTEXTS:
        contexte_specifie = args_clean[0]
        args_clean = args_clean[1:]
    
    # Deuxième argument = IA (si valide)
    if len(args_clean) >= 1 and args_clean[0] in IA_URLS:
        ia_specifiee = args_clean[0]
    
    # Détection automatique
    if force_auto or not contexte_specifie:
        contexte = detect_context()
        print(f"🔍 Auto-détection contexte : {contexte}")
    else:
        contexte = contexte_specifie
        print(f"📌 Contexte spécifié : {contexte}")
    
    if force_auto or not ia_specifiee:
        ia = detect_ia(contexte)
        print(f"🔍 Auto-détection IA : {ia}")
    else:
        ia = ia_specifiee
        print(f"📌 IA spécifiée : {ia}")
    
    # Lancer la session
    if lancer_session(contexte, ia):
        print("\n✅ Session lancée avec succès !")
    else:
        print("\n❌ Échec du lancement de session.")
        sys.exit(1)


if __name__ == "__main__":
    main()