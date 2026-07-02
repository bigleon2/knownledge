# 🎯 Écosystème DJ/Python/PDF/Image/Audio — François

**Version** : 1.0.0  
**Date** : 2026-06-21  
**Auteur** : François (orchestré par Qwen3.7)

---

## 📋 Description

Écosystème complet d'orchestration multi-agents pour :
- **DJing** : TRAKTOR PRO 3.11, KONTROL S4 MK2, fichiers TSI, analyse audio
- **Développement** : Python, C/C++, Next.js 16, APIs
- **Documents** : PDF, Word, Excel, PowerPoint
- **Media** : Images, vidéo, audio, OCR
- **Automatisation** : Scripts, workflows, intégrations

---

## 🏗️ Architecture

```
/home/z/my-project/
├── README.md                    ← Ce fichier
├── prompt-maitre.md             ← Prompt maître universel
├── prompt-maitre-system.md      ← Prompt ingénieur système (z.ai)
├── prompt-maitre-code.md        ← Prompt développement (qwen)
├── launcher.py                  ← Launcher multi-contexte v3.0
├── setup-aliases.sh             ← Installation alias shell
├── skills.md                    ← Inventaire 69 skills
├── gen-plan.skill.md            ← Protocole gen-plan
├── gen-plan-agent-types.md      ← Matrice agents
├── MEMORY-INSTRUCTIONS.md       ← Config mémoire IA
├── context.md                   ← Contexte universel
├── worklog.md                   ← Log d'exécution
│
├── skills/                      ← 69 skills
│   ├── gen-plan/SKILL.md
│   ├── fullstack-dev/SKILL.md
│   ├── pdf/SKILL.md
│   └── ... (69 au total)
│
└── agents/                      ← 12 agents
    ├── tsi-expert/AGENT.md
    ├── kontrol-s4-expert/AGENT.md
    ├── python-executor/AGENT.md
    ├── pdf-expert/AGENT.md
    ├── image-analyst/AGENT.md
    ├── auto-tagger/AGENT.md
    └── ... (12 au total)
```

---

## 🚀 Utilisation Rapide

### Installation

```bash
# 1. Installer les alias shell
bash /home/z/my-project/setup-aliases.sh
source ~/.bashrc

# 2. Installer les dépendances Python
pip install pyperclip
```

### Commandes Principales

```bash
# Auto-détection contexte + IA
ai

# Contexte système (z.ai par défaut)
sys
system

# Contexte codage (qwen par défaut)
code
dev

# Combinaisons spécifiques
sys-zai         # Système sur z.ai
sys-qwen        # Système sur qwen
code-qwen       # Codage sur qwen
code-chatgpt    # Codage sur ChatGPT

# Configuration
ai-config       # Configurer IA par défaut
ai-list         # Lister contextes et IA
```

---

## 🤖 Agents Disponibles (12)

### Agents Génériques (6)
1. `general-purpose` — Polyvalent
2. `Explore` — Recherche rapide
3. `Plan` — Architecture
4. `frontend-styling-expert` — CSS/UI/UX
5. `full-stack-developer` — Next.js 16
6. `ppt-expert` — Présentations

### Agents Spécialisés DJ/Audio/Python/PDF/Image (6)
7. `tsi-expert` — Fichiers TSI (TRAKTOR)
8. `kontrol-s4-expert` — KONTROL S4 MK2
9. `python-executor` — Scripts Python
10. `pdf-expert` — PDF
11. `image-analyst` — Images (VLM, OCR)
12. `auto-tagger` — Tagging audio

---

## 📚 Skills (69)

### Catégories
1. **Méta (Skills & Plans)** — 6 skills
2. **Développement** — 3 skills
3. **Documents & Contenu** — 5 skills
4. **IA & Media** — 12 skills
5. **Web & Recherche** — 6 skills
6. **Visualisation & Design** — 5 skills
7. **Contenu & Marketing** — 6 skills
8. **Finance & Recherche** — 7 skills
9. **Carrière & Emploi** — 4 skills
10. **Éducation** — 8 skills
11. **Lifestyle & Bien-être** — 5 skills
12. **Autres** — 2 skills

---

## 🎯 Cas d'Usage DJ

### Analyse Collection Vinyles
```bash
# Demande : "Analyse ma collection de vinyles, détecte BPM/clé, génère rapport PDF"
# Plan :
1. auto-tagger → Scan + analyse BPM/clé
2. image-analyst → Analyse pochettes
3. pdf-expert → Génération rapport PDF
```

### Création Mapping TSI
```bash
# Demande : "Crée un mapping TSI pour hot cues deck A"
# Plan :
1. kontrol-s4-expert → Specs MIDI
2. tsi-expert → Création mapping
3. python-executor → Test
```

### Script Python Analyse Audio
```bash
# Demande : <py analyze_bpm.py> "Analyse BPM de tous mes MP3"
# Plan :
1. python-executor → Création script
2. python-executor → Exécution
3. pdf-expert → Rapport
```

---

## 🔄 Protocole gen-plan

### 11 Étapes Séquentielles
1. Collecte des demandes
2. Lecture du projet
3. Identification nature
4. Objectifs
5. Décomposition sous-tâches
6. Dépendances
7. Priorisation
8. Risques
9. Structuration plan
10. Validation
11. Mise à jour prompt-master

### Matrice de Décision
```
1. Skill existe ? → Charger + agent spécialisé
2. Pas de skill → Agent spécialisé seul
3. Rien → general-purpose (dernier recours)
```

---

## 🧠 Persistance du Prompt Maître

### Solution 1 : Launcher (Recommandée)
```bash
python3 /home/z/my-project/launcher.py
```

### Solution 2 : Mémoire IA
Suivre les instructions dans `MEMORY-INSTRUCTIONS.md`

### Solution 3 : Fichier de Contexte
Copier-coller `context.md` au début de chaque session

---

## 📖 Documentation

- **Prompt maître** : `prompt-maitre.md`
- **Launcher** : `launcher.py --help`
- **Alias** : `setup-aliases.sh`
- **Mémoire IA** : `MEMORY-INSTRUCTIONS.md`
- **Skills** : `skills.md`
- **Agents** : `gen-plan-agent-types.md`
- **Protocole** : `gen-plan.skill.md`

---

## 🎯 Profil Utilisateur

- **Nom** : François
- **Âge** : 50 ans
- **Localisation** : France (59630)
- **Compétences** : C/C++, Python
- **Activité** : DJ avec KONTROL S4 MK32 + TRAKTOR 3.11
- **Intérêts** : Conception programmes, analyse code
- **Langue** : Français

---

## 🚀 Démarrage Rapide

```bash
# 1. Installation
bash /home/z/my-project/setup-aliases.sh
source ~/.bashrc
pip install pyperclip

# 2. Premier lancement
sys    # Système sur z.ai
code   # Codage sur qwen

# 3. Configuration mémoire IA
# Suivre MEMORY-INSTRUCTIONS.md
```

---

## 📊 Statistiques

- **Agents** : 12 (6 génériques + 6 spécialisés)
- **Skills** : 69 (12 catégories)
- **IA supportées** : 9 (z.ai, qwen, manus, copilot, chatgpt, perplexity, gemini, claude, codex)
- **Contextes** : 2 (système, code)

---

**Fin du README**

*Généré le 2026-06-21 pour François — DJ, développeur C/C++, utilisateur TRAKTOR*