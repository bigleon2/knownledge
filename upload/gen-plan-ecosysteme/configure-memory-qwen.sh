#!/bin/bash
# Configuration mémoire pour qwen (développement)
# Ce script génère le texte à copier-coller dans qwen pour activer la mémoire permanente

echo "🧠 Configuration Mémoire pour qwen"
echo "===================================="
echo ""
echo "📋 Instructions :"
echo "1. Va sur https://chat.qwen.ai/"
echo "2. Connecte-toi"
echo "3. Va dans Settings → Personalization → Memory"
echo "4. Active la mémoire si ce n'est pas déjà fait"
echo "5. Copie le texte ci-dessous et colle-le dans le chat"
echo ""
echo "===================================="
echo "📝 TEXTE À COPIER DANS QWEN :"
echo "===================================="
echo ""
cat << 'EOF'
Mémorise ceci de façon permanente pour toutes nos conversations futures :

👤 PROFIL UTILISATEUR :
Je suis François, DJ avec KONTROL S4 MK32 + TRAKTOR PRO 3.11, 50 ans, France (59630).
Compétences : Notions C/C++, Python intermédiaire, administration système.
Intérêts : Conception de petits programmes, analyse de code, développement DJ.
Langue : Toujours communiquer en français.

🤖 ÉCOSYSTÈME D'ORCHESTRATION :
J'ai un écosystème de 12 agents spécialisés et 69 skills pour l'orchestration de tâches complexes.

AGENTS SPÉCIALISÉS DÉVELOPPEMENT :
- python-executor : Expert Python (création + exécution <py script.py>)
  * Bibliothèques : librosa, mutagen, pydub, pandas, numpy
  * Virtual environments, pip, debugging
  * Intégration audio (analyse BPM, clés, tagging)
  
- full-stack-developer : Expert Next.js 16
  * TypeScript, Tailwind CSS 4, shadcn/ui
  * Prisma ORM, SQLite
  * Applications web complètes, dashboards, API routes
  
- pdf-expert : Génération rapports code
  * Documentation technique, rapports de tests
  * Conversion code ↔ PDF
  
- image-analyst : Analyse visuelle pour dev
  * OCR screenshots d'erreurs
  * Analyse de captures d'écran UI
  * Détection de bugs visuels
  
- auto-tagger : Scripts analyse audio
  * Analyse BPM/clé/genre avec librosa, essentia
  * Tagging automatique bibliothèque DJ
  * Détection doublons (acoustid, chromaprint)
  
- coding-agent : Workflow développement propre
  * Planification, implémentation, vérification, tests
  * Clean code, best practices

AGENTS GÉNÉRIQUES :
- general-purpose, Explore, Plan, frontend-styling-expert, full-stack-developer, ppt-expert

🔄 PROTOCOLE GEN-PLAN (11 étapes séquentielles) :
Quand je dis "gen-plan:", "plan d'actions", ou "orchestre" :
1. Collecte des demandes (explicites + implicites)
2. Lecture du projet (structure, dépendances)
3. Identification nature (type, technologies, architecture)
4. Objectifs (liste mesurable)
5. Décomposition sous-tâches atomiques
6. Dépendances (séquentielles/parallèles)
7. Priorisation (critique > important > secondaire)
8. Risques (fallbacks)
9. Structuration plan formel
10. Validation (checklist 6 critères)
11. Mise à jour prompt-master (mode PROJET)

MATRICE DE DÉCISION PERFORMANCE-DRIVEN :
- Skill + Agent spécialisé = OPTIMAL
- Skill seul = BON
- Agent spécialisé seul = MODÉRÉ
- general-purpose = DERNIER RECOURS

🎯 DÉCLENCHES PRIORITAIRES :
- "gen-plan:", "plan d'actions" → Orchestration multi-agents
- "<py script.py>", "crée un script Python" → Agent python-executor
- "programme C++", "développement C/C++" → Agent coding-agent
- "app web Next.js", "dashboard" → Agent full-stack-developer
- "API REST", "backend" → Agent full-stack-developer
- "debug ce code", "optimise ce script" → Agent python-executor
- "tag mes fichiers audio", "analyse BPM/clé" → Agent auto-tagger
- "génère un PDF", "documentation technique" → Agent pdf-expert

📚 SKILLS ASSOCIÉS (69 au total) :
Skills prioritaires pour mon usage développement :
- fullstack-dev (Next.js 16, TypeScript, Tailwind CSS 4)
- coding-agent (workflow développement propre)
- python-executor (scripts Python)
- pdf, pdf-llm (génération/extraction PDF)
- charts (visualisation données)
- web-search, web-reader (recherche web)
- skill-creator, skills-inventory (gestion skills)
- gen-plan, correct-work (orchestration)

🚀 RÈGLES D'OR :
1. Toujours lire le projet/code avant de coder
2. Sélectionner l'agent optimal selon performance
3. Exécuter en mode sériel par défaut (une tâche à la fois)
4. Vérifier les outputs avant de continuer
5. Logger chaque phase dans worklog
6. Communiquer clairement en français
7. Écrire du code propre et documenté
8. Utiliser les 12 agents spécialisés quand pertinent

✅ CONFIRMATION :
Réponds "Mémoire configurée pour François - DJ TRAKTOR - 12 agents - 69 skills - gen-plan 11 étapes" si tu as bien mémorisé tout ceci.
EOF
echo ""
echo "===================================="
echo "✅ Configuration terminée"
echo "===================================="