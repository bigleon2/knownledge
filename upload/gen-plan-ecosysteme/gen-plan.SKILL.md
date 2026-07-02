---
name: gen-plan
version: 1.1.0
date: 2026-06-21
description: >
  Planification et orchestration multi-étapes de tâches complexes.
  Analyse la conversation/projet, décompose en sous-tâches, sélectionne
  l'agent ou skill optimal pour chaque phase, et exécute en mode sériel.
  Intègre automatiquement les fichiers de skills/éco-système dans z.ai.
  Use when the user says "gen-plan", "plan d'actions", "correct-work",
  "orchestre", or requests structured multi-step execution.
---

# gen-plan

Skill d'orchestration et de planification structurée pour tâches complexes multi-étapes.

## Déclencheurs

- `gen-plan:` suivi d'une description de tâche
- `gen-plan:correct-work(projet)` — vérification et correction d'un projet complet
- `plan d'actions` — demande explicite de planification
- `orchestre` — orchestration multi-agents
- Toute demande impliquant plusieurs étapes séquentielles avec des livrables

## Modes

| Mode | Déclencheur | Comportement |
|------|-------------|--------------|
| **TÂCHE** | `gen-plan: <description>` | Planifie et exécute une tâche spécifique |
| **PROJET** | `gen-plan:correct-work(projet)` | Analyse complète du projet, corrections, mise à jour prompt-master |
| **CIBLE** | `gen-plan:correct-work(<cible>)` | Vérification/correction d'un élément spécifique |

## Protocole — 13 Étapes Séquentielles

### Étape 1 — Collecte et Analyse des Demandes
**Objectif** : Relire toute la conversation pour extraire chaque demande explicite et implicite.
- Relire tous les messages utilisateur (demandes initiales, specs, contraintes, corrections)
- Identifier demandes explicites (ce que l'utilisateur a directement demandé)
- Identifier demandes implicites (prérequis, effets de bord, conséquences logiques)
- Lister chaque demande sans ambiguïté
- **Méthode** : Lire conversation complète. Utiliser `worklog.md` si disponible.

### Étape 2 — Lecture et Analyse du Projet
**Objectif** : Traverser tous les fichiers du projet pour comprendre structure, architecture, dépendances, état actuel.
- **Principe** : Un plan sans connaissance du projet est générique et probablement inadéquat.
- Structure fichiers : arborescence, configs (package.json, tsconfig, etc.)
- Code source : chaque fichier significatif
- Schéma base de données (si applicable)
- Dépendances : imports inter-modules, dépendances externes
- Configuration : fichiers config pertinents
- Documentation : README, worklog, specs, fichiers référence
- **Méthode** : Utiliser Read, Glob, Grep pour traverser chaque fichier significatif.

### Étape 3 — Identification de la Nature du Projet
**Objectif** : Déterminer type projet, technologies, architecture, complexité.
- Type projet : web app, API, script, document, analyse, skill, etc.
- Technologies : framework, langage, base de données, build tools
- Architecture : monolithe, micro-services, fullstack, frontend only, backend only
- Complexité : nombre fichiers, profondeur arborescence, dépendances

### Étape 4 — Identification des Objectifs
**Objectif** : Lister chaque objectif explicitement, sans ambiguïté ni omission.
- Lister objectifs dérivés des demandes utilisateur
- Lister objectifs implicites (prérequis, effets de bord, contraintes)
- Vérifier que chaque objectif est mesurable (atteint ou non)
- Supprimer doublons

### Étape 5 — Décomposition en Sous-tâches
**Objectif** : Décomposer chaque objectif en sous-tâches atomiques avec ordre logique.
- Pour chaque objectif, identifier sous-tâches atomiques
- Ordonner logiquement (prérequis d'abord, puis exécution, puis validation)
- Adapter au type projet (fullstack, document, script, skill, etc.)

### Étape 6 — Détection des Dépendances
**Objectif** : Identifier dépendances entre sous-tâches et contraintes de précédence.
- Dépendances séquentielles (A doit finir avant B)
- Dépendances parallèles (A et B peuvent tourner simultanément)
- Dépendances conditionnelles (B tourne seulement si A réussit/échoue)
- Vérifier absence de dépendances circulaires

### Étape 7 — Priorisation

| Priorité | Définition |
|----------|------------|
| **Critique** | Échec invalide le résultat entier |
| **Importante** | Impact significatif sur qualité |
| **Secondaire** | Améliore résultat mais non bloquant |

### Étape 8 — Estimation des Risques
- Complexité technique : connaissance spécialisée requise ?
- Ambiguïté : clairement définie ou ouverte à interprétation ?
- Dépendance externe : repose sur API, service, outil qui pourrait échouer ?
- Fallback : que faire si sous-tâche échoue ?

### Étape 9 — Structuration du Plan
**Objectif** : Produire un plan d'actions formel, complet, adapté au projet.

Le plan doit inclure :
- **En-tête** : nature projet, objectifs, contraintes
- **Liste ordonnée d'étapes** avec IDs (1, 2-a, 2-b, 3...) :
  - Pour chaque étape : objectif, fichiers concernés, dépendances, priorité
  - Indication parallélisme où applicable
  - Critères de validation par étape
- **Carte dépendances** : résumé relations étapes
- **Matrice risques** : risques et plans fallback

### Étape 10 — Validation du Plan
**Checklist** :
- [ ] Le plan couvre-t-il toutes les demandes utilisateur ?
- [ ] Y a-t-il des étapes manquantes ?
- [ ] L'ordre d'exécution est-il logique (aucune dépendance violée) ?
- [ ] Le plan est-il adapté au projet (pas générique) ?
- [ ] Chaque étape a-t-elle un critère de validation clair ?
- [ ] Les risques principaux sont-ils couverts par des plans fallback ?

Si problème trouvé, retourner à l'étape pertinente et corriger.

### Étape 11 — Test et Correction Pré-Intégration
**Objectif** : Tester chaque fichier généré ou modifié AVANT de l'intégrer à l'éco-système.

Pour chaque fichier candidat à l'intégration :

1. **Classifier le fichier** :
   - **Skill** : Fichier avec YAML frontmatter (name, description) ou contenu définissant un protocole/routine réutilisable
   - **Éco-système** : Fichier de configuration, prompt maître, contexte, mémoire, agent, ou tout fichier qui étend les capacités du système
   - **Utilitaire** : Script, outil, fichier temporaire — ne pas intégrer

2. **Tester le fichier** :
   - **Skill (.md avec YAML)** : Vérifier que le YAML frontmatter est valide (name, description présents), que le contenu est cohérent et complet (> 200 chars), qu'il ne contient pas de fragments ou de placeholders non résolus
   - **Python (.py)** : Compiler avec `compile()` ou `ast.parse()` pour vérifier la syntaxe. Vérifier les imports, les fonctions principales, l'absence de code mort évident
   - **Shell (.sh)** : Vérifier le shebang (`#!/bin/bash`), la syntaxe avec `bash -n`, l'absence de commandes destructrices non gardées
   - **Markdown (.md)** : Vérifier la structure (titres `#`, sections cohérentes), l'absence de contenu tronqué ou de fragments de code incomplets
   - **Configuration (.json, .yaml)** : Valider le format JSON/YAML, vérifier les clés obligatoires

3. **Corriger les anomalies détectées** :
   - Si un test échoue, corriger le fichier immédiatement
   - Si le fichier est un fragment trop petit (< 100 chars) ou incomplet, le marquer comme "invalide" et ne pas l'intégrer
   - Si le fichier contient des artefacts de parsing (XML tags, balises `<parameter>`, etc.), les nettoyer
   - Documenter chaque correction dans le worklog

4. **Valider la cohérence entre fichiers** :
   - Vérifier que les références croisées entre fichiers sont valides
   - Vérifier qu'un skill référencé dans le prompt-maître existe bien
   - Vérifier qu'un agent mentionné dans la matrice de décision est bien défini

### Étape 12 — Intégration Éco-Système (SPÉCIFIQUE z.ai)
**Objectif** : Si les fichiers concernent des skills ou l'éco-système, les intégrer à l'éco-système de z.ai.

**Prérequis** : Étape 11 (Test et Correction) doit être terminée avec succès.

1. **Si le fichier est un Skill** :
   - Créer le répertoire `/home/z/my-project/skills/<skill-name>/` s'il n'existe pas
   - Y placer le fichier `SKILL.md` avec le contenu validé
   - Vérifier la conformité du YAML frontmatter (name, description obligatoires)
   - Ne pas écraser un skill existant sans confirmation utilisateur
   - Si le skill existe déjà, proposer un diff ou une mise à jour

2. **Si le fichier est un fichier d'Éco-système** :
   - **Prompt maître / Contexte** : Sauvegarder dans `/home/z/my-project/skills/gen-plan/references/`
   - **Configuration mémoire** : Sauvegarder dans `/home/z/my-project/skills/gen-plan/references/`
   - **Définitions d'agents** : Intégrer dans la section agents du prompt maître ou créer un fichier de référence
   - **Matrices de décision** : Sauvegarder dans `/home/z/my-project/skills/gen-plan/references/`

3. **Validation post-intégration** :
   - Vérifier que chaque fichier intégré ne casse pas les skills existants
   - Vérifier qu'il n'y a pas de conflit de noms
   - Mettre à jour l'inventaire des skills si nécessaire
   - Logger l'intégration dans `/home/z/my-project/worklog.md`

### Étape 13 — Auto-Réapplication si gen-plan.skill Mis à Jour
**Objectif** : Si le fichier `gen-plan.skill` (ce fichier) est lui-même mis à jour pendant l'exécution du plan, réappliquer la nouvelle version aux tâches restantes.

**Règle de réapplication** :
1. Après toute modification de ce fichier `SKILL.md` (mise à jour, correction, ajout de règles) :
   - Marquer les tâches restantes comme "à réévaluer"
   - Recharger le skill mis à jour
   - Pour chaque tâche restante non encore exécutée :
     - Vérifier si la nouvelle version du skill modifie la manière dont la tâche doit être exécutée
     - Si oui : réécrire le plan de la tâche selon les nouvelles règles
     - Si non : exécuter tel quel
2. **Cas d'usage typiques de réapplication** :
   - Ajout d'une nouvelle règle de classification (ex: nouveau type de fichier à intégrer)
   - Modification de la matrice de décision agent/skill
   - Ajout d'un nouveau critère de test dans l'étape 11
   - Correction d'un bug dans le protocole
3. **Logging** : Documenter chaque réapplication dans le worklog avec l'ID de la tâche affectée et la raison de la réévaluation

## Matrice de Décision Agent/Skill

Pour chaque sous-tâche, évaluer quelle combinaison produit le meilleur résultat :

```
1. Existe-t-il un SKILL correspondant ?
   ├─ OUI → Charger le skill
   │   └─ Le skill bénéficie-t-il d'un agent spécialisé ?
   │       ├─ OUI → Skill + Agent Spécialisé (OPTIMAL)
   │       └─ NON → Skill seul via agent général (BON)
   └─ NON → Existe-t-il un agent spécialisé ?
       ├─ OUI → Agent Spécialisé seul
       └─ NON → Agent général (DERNIER RECOURS)
```

**Critères de sélection (ordonnés par impact performance)** :
1. **Skill + agent spécialisé** (meilleure performance)
2. **Skill seul** (bonne performance)
3. **Agent spécialisé seul** (performance modérée)
4. **Agent général** (fallback)

## Règles d'Exécution

- **Sérielle par défaut** : Une tâche à la fois, dans l'ordre défini
- **Quality gates** : Validation après chaque phase avant de continuer
- **Worklog** : Mettre à jour `/home/z/my-project/worklog.md` après chaque phase
- **Communications** : L'utilisateur sait toujours où on en est (progression visible)
- **Tester avant d'intégrer** : Aucun fichier n'est intégré à l'éco-système sans avoir passé les tests de l'Étape 11
- **Auto-réapplication** : Si ce skill est mis à jour en cours d'exécution, les tâches restantes sont réévaluées à la lumière de la nouvelle version (Étape 13)

## Template de Phase

```markdown
## ▶️ PHASE [ID] — [Titre]

**Objectif** : [Ce que cette phase accomplit]
**Mode** : [Skill+Agent / Skill / Agent / General]
**Dépendances** : [Phases précédentes requises]
**Priorité** : [Critique / Importante / Secondaire]

**Tâche :**
[Description claire]

**Skill à charger (si applicable) :**
- Nom : [skill-name]
- Chemin : /home/z/my-project/skills/[skill-name]/SKILL.md

**Fichiers concernés :**
- [Liste des fichiers à lire/écrire/modifier]

**Outputs attendus :**
- [Artefacts spécifiques à produire]

**Critères de validation :**
- [Comment vérifier que cette phase a réussi]
```