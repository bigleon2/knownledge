# SKILL : gen-plan

> Skill de generation de plan d'actions robuste et adapte au projet.

---

```yaml
---
name: gen-plan
version: 1.0.0
date: 2026-06-14
authors: [Z AI]
description: >
  Skill de generation de plan d'actions robuste et adapte au projet. Declenche a chaque fois
  que l'utilisateur ecrit "gen_plan" ou "genere un plan" ou "plan d'actions". Analyse les
  demandes de l'utilisateur, lit et analyse l'integralite du projet, identifie la nature du
  projet, puis genere un plan d'actions structure, logique et detaille adapte au type de
  projet (fullstack, frontend, backend, document, script, etc.). Peut etre appele par
  d'autres skills (ex : correct-work) en tant que sous-protocole.
---
```

---

## Table des matieres

1. [Presentation](#presentation)
2. [Mots-cles de declenchement](#mots-cles-de-declenchement)
3. [Modes d'execution](#modes-dexecution)
4. [Protocol (11 etapes sequentielles)](#protocol-11-etapes-sequentielles)
   - [Etape 1 — Collecter et analyser les demandes](#etape-1--collecter-et-analyser-les-demandes)
   - [Etape 2 — Lire et analyser l'integralite du projet](#etape-2--lire-et-analyser-lintegralite-du-projet)
   - [Etape 3 — Identifier la nature du projet](#etape-3--identifier-la-nature-du-projet)
   - [Etape 4 — Identifier les objectifs](#etape-4--identifier-les-objectifs)
   - [Etape 5 — Decomposer en sous-taches adaptees](#etape-5--decomposer-en-sous-taches-adaptees)
   - [Etape 6 — Detecter les dependances](#etape-6--detecter-les-dependances)
   - [Etape 7 — Prioriser](#etape-7--prioriser)
   - [Etape 8 — Estimer les risques](#etape-8--estimer-les-risques)
   - [Etape 9 — Structurer le plan](#etape-9--structurer-le-plan)
   - [Etape 10 — Valider le plan](#etape-10--valider-le-plan)
   - [Etape 11 — Mettre a jour le prompt-maitre (mode PROJET)](#etape-11--mettre-a-jour-le-prompt-maitre-mode-projet)
5. [Format de sortie du plan](#format-de-sortie-du-plan)
6. [Relations avec les autres skills](#relations-avec-les-autres-skills)
7. [Installation et utilisation](#installation-et-utilisation)
8. [Historique des versions](#historique-des-versions)

---

## Presentation

Ce skill genere un plan d'actions robuste, structure et adapte au projet. Il peut etre
invoque directement par l'utilisateur (`gen_plan`, `genere un plan`, `plan d'actions`) ou
appele par d'autres skills en tant que sous-protocole (ex : etape 1 de `correct-work`).

Le plan produit est systematiquement adapte au type de projet detecte : un projet web
Next.js n'a pas les memes points de verification qu'un projet Python, un document PDF
ou une analyse de donnees. Le plan reflechit la nature, la complexite et les specificites
techniques du projet concerne.

---

## Mots-cles de declenchement

- `gen_plan`
- `genere un plan`
- `plan d'actions`

---

## Modes d'execution

| Mode | Declencheur | Comportement |
|------|------------|--------------|
| **DIRECT** | L'utilisateur ecrit "gen_plan" | Genere un plan d'actions sans gestion du prompt-maitre |
| **PROJET** | Appele par correct-work(projet) | Analyse l'integralite du projet + genere/gere le prompt-maitre |
| **CIBLE** | Appele par correct-work(cible) | Analyse ponctuelle des fichiers pertinents, pas de prompt-maitre |

---

## Protocol (11 etapes sequentielles)

Le skill s'execute en suivant les etapes sequentielles ci-dessous. L'ordre est important :
il faut **lire le projet avant de le classifier**, et **classifier le projet avant de planifier**.

---

### Etape 1 — Collecter et analyser les demandes

**Objectif** : Relire l'integralite des demandes de l'utilisateur dans la session pour
extraire chaque demande explicite et implicite.

**Checklist** :

1. Relire tous les messages de l'utilisateur (messages initiaux, specifications, contraintes,
   corrections demandees).
2. Identifier les demandes explicites (ce que l'utilisateur a directement demande).
3. Identifier les demandes implicites (ce qui decoule logiquement des demandes explicites,
   les prerequis necessaires, les effets de bord a anticiper).
4. Lister chaque demande de maniere non ambigue.

**Methode** :

- Relire toute la conversation pour extraire chaque demande.
- Si un fichier de travail (`worklog.md`) existe, l'utiliser pour comprendre le contexte.

---

### Etape 2 — Lire et analyser l'integralite du projet

**Objectif** : Parcourir l'ensemble des fichiers du projet pour comprendre sa structure,
son architecture, ses dependances et son etat actuel. Cette analyse est indispensable
avant toute planification — on ne peut pas planifier ce qu'on n'a pas lu.

**Principe cle** : Un plan sans connaissance du projet est un plan generique et probablement
inadapte. La lecture exhaustive est un investissement necessaire.

**Checklist** :

1. **Structure des fichiers** : parcourir l'arborescence, l'organisation des dossiers,
   les fichiers de config (package.json, tsconfig, next.config, tailwind, etc.).
2. **Code source** : lire chaque fichier source significatif (composants, routes, API,
   modeles, utilitaires, scripts) pour comprendre la logique implementee.
3. **Schema de base de donnees** (si applicable) : lire le schema Prisma ou equivalent.
4. **Dependances** : analyser package.json, les imports croises entre modules, les
   dependances externes et leurs versions.
5. **Configuration** : lire les fichiers de config pertinents.
6. **Documentation** : README, worklog.md, specifications, fichiers de reference.
7. **Assets et ressources** : images, templates, fichiers statiques pertinents.

**Methode** :

- Utiliser les outils de lecture de fichiers (Read, Glob, Grep) pour parcourir chaque
  fichier significatif du projet.
- Ne pas se limiter aux fichiers recemment modifies — lire tout ce qui est pertinent
  pour comprendre le projet dans son ensemble.
- Prendre des notes mentales ou ecrites sur les points cles : architecture, dependances,
  points d'attention, zones a risque.
- Si le projet est tres volumineux, prioriser la lecture des fichiers principaux et
  utiliser Grep pour les recherches ciblees.

---

### Etape 3 — Identifier la nature du projet

**Objectif** : Determiner le type de projet, ses technologies, son architecture et sa
complexite. Cette identification conditionne l'ensemble du plan d'actions.

**Checklist** :

1. **Type de projet** : application web, API, script, document, analyse, skill, etc.
2. **Technologies** : framework, langage, base de donnees, outils de build.
3. **Architecture** : monolithe, micro-services, fullstack, frontend only, backend only.
4. **Complexite** : nombre de fichiers, profondeur de l'arborescence, nombre de
   dependances, surface d'interaction.

**Methode** :

- Croiser les informations collectees aux etapes 1 et 2 pour determiner la nature du projet.
- La classification n'est pas mutuellement exclusive : un projet peut etre "fullstack + micro-services"
  ou "document + script d'automatisation".

---

### Etape 4 — Identifier les objectifs

**Objectif** : Lister explicitement chaque objectif a atteindre, sans ambiguite ni omission.
Les objectifs doivent etre specifiques au projet verifie.

**Checklist** :

1. Lister chaque objectif derive des demandes de l'utilisateur.
2. Lister les objectifs implicites (prerequis, effets de bord, contraintes).
3. Verifier que chaque objectif est mesurable (on peut dire s'il est atteint ou non).
4. Eliminer les doublons et les redondances.

**Methode** :

- Reprendre la liste des demandes (Etape 1) et la transformer en objectifs.
- Valider que chaque objectif est specifique au projet identifie (Etape 3).

---

### Etape 5 — Decomposer en sous-taches adaptees

**Objectif** : Decomposer chaque objectif en sous-taches atomiques, avec un ordre logique
d'execution. Les sous-taches doivent refleter les specificites du projet.

**Checklist** :

1. Pour chaque objectif, identifier les sous-taches atomiques necessaires.
2. Ordonner les sous-taches logiquement (prerequis d'abord, puis execution, puis validation).
3. Adapter les sous-taches au type de projet :
   - **Projet fullstack** : inclure la verification API frontend-backend, schema BDD, auth.
   - **Projet frontend only** : inclure la verification responsive, accessibilite, composants.
   - **Projet backend/API** : inclure la verification endpoints, validation, securite.
   - **Document/PDF** : inclure la verification contenu, mise en page, coherence des donnees.
   - **Script/automatisation** : inclure la verification edge cases, robustesse, gestion des erreurs.

**Methode** :

- Partir de chaque objectif et le decomposer en etapes concretes.
- Verifier que chaque sous-tache est suffisamment precise pour etre executee
  de maniere autonome.

---

### Etape 6 — Detecter les dependances

**Objectif** : Identifier les dependances entre sous-taches et les contraintes de precedence,
en tenant compte de l'architecture du projet.

**Checklist** :

1. Identifier les dependances sequentielles (A doit etre termine avant B).
2. Identifier les dependances paralleles (A et B peuvent etre executees en meme temps).
3. Identifier les dependances conditionnelles (B n'est executee que si A echoue/reussit).
4. Verifier qu'il n'y a pas de dependances circulaires.

**Methode** :

- Construire un graphe de dependances (mental ou ecrit).
- Identifier les chemins critiques (sequence la plus longue de dependances sequentielles).

---

### Etape 7 — Prioriser

**Objectif** : Classer les sous-taches par priorite en fonction de leur impact sur le
resultat final et de la nature du projet.

**Checklist** :

1. **Critique** : les sous-taches dont l'echec invalide tout le resultat.
2. **Importante** : les sous-taches qui ont un impact significatif sur la qualite du resultat.
3. **Secondaire** : les sous-taches qui ameliorent le resultat mais ne sont pas bloquantes.

**Methode** :

- Evaluer l'impact de chaque sous-tache sur le resultat final.
- Prioriser en fonction du type de projet (ex : pour un projet avec BDD, la verification
  du schema est critique ; pour un document, la coherence du contenu est critique).

---

### Etape 8 — Estimer les risques

**Objectif** : Pour chaque sous-tache, identifier les risques potentiels et prevoir des
solutions de secours. Les risques doivent etre specifiques au contexte du projet.

**Checklist** :

1. **Complexite technique** : la sous-tache requiert-elle des competences ou des
   connaissances specifiques ?
2. **Ambiguite** : la sous-tache est-elle clairement definie ou sujette a interpretation ?
3. **Dependance externe** : la sous-tache depend-elle d'un service, d'une API ou d'un
   outil externe qui pourrait echouer ?
4. **Solution de secours** : que faire si la sous-tache echoue ? Contourner, reporter,
   simplifier ?

**Methode** :

- Pour chaque risque identifie, definir une strategie d'attenuation.
- Les risques doivent etre specifiques au contexte du projet (ex : risques de migration
  de schema pour un projet avec BDD, risques de compatibilite navigateur pour un frontend,
  risques de formatage pour un document).

---

### Etape 9 — Structurer le plan

**Objectif** : Produire un plan d'actions formel, complet et adapte au projet.

**Format du plan** :

Le plan doit comprendre :

1. **En-tete** :
   - Nature du projet (type, technologies, architecture)
   - Objectifs principaux
   - Contraintes et hypotheses

2. **Liste ordonnee des etapes** avec identifiants (1, 2-a, 2-b, 3...) :
   - Pour chaque etape : objectif, fichiers/concernes, dependances, priorite
   - Indication du parallelisme possible (etapes independantes executables en parallele)
   - Critere de validation pour chaque etape (comment savoir si l'etape est reussie)
   - **Adaptation au projet** : pour chaque etape, indiquer en quoi elle est specifique
     au type de projet verifie et quels points de verification particuliers s'appliquent

3. **Carte des dependances** : resume des relations entre etapes.

4. **Matrice des risques** : resume des risques et solutions de secours.

**Methode** :

- Structurer le plan selon le format ci-dessus.
- Verifier que le plan couvre tous les objectifs identifies.
- Verifier que l'ordre d'execution respecte les dependances.

---

### Etape 10 — Valider le plan

**Objectif** : Verifier que le plan est complet, coherent et adapte au projet.

**Checklist** :

1. Le plan couvre-t-il toutes les demandes de l'utilisateur ?
2. Y a-t-il des etapes manquantes ?
3. L'ordre d'execution est-il logique (pas de dependance non respectee) ?
4. Le plan est-il adapte au projet (pas de verification generique ignorant les specificites) ?
5. Chaque etape a-t-elle un critere de validation clair ?
6. Les risques principaux sont-ils couverts par des solutions de secours ?

**Methode** :

- Relire le plan en entier et verifier chaque point de la checklist.
- Si un probleme est detecte, revenir a l'etape concernee et corriger.

---

### Etape 11 — Mettre a jour le prompt-maitre du projet (mode PROJET uniquement)

**Objectif** : Si le skill est appele en mode PROJET (via correct-work), mettre a jour
le fichier prompt-maitre du projet si des modifications ont ete apportees.

**Checklist** :

1. Verifier si le projet a ete modifie depuis la derniere analyse.
2. Si oui, mettre a jour le prompt-maitre avec les nouvelles informations.
3. Si non, conserver le prompt-maitre existant sans modification.

**Methode** :

- Comparer l'etat actuel du projet avec les informations du prompt-maitre.
- Mettre a jour uniquement les sections concernees par les modifications.

---

## Format de sortie du plan

```
## Plan d'actions — [Nom du projet]

### Nature du projet
- Type : [fullstack / frontend / backend / document / script / ...]
- Technologies : [framework, langage, BDD, ...]
- Architecture : [monolithe / micro-services / ...]
- Complexite : [faible / moyenne / elevee]

### Objectifs
1. [Objectif 1]
2. [Objectif 2]
...

### Etapes

#### 1. [Titre de l'etape]
- **Objectif** : ...
- **Fichiers concernes** : ...
- **Dependances** : aucune / apres etape X
- **Priorite** : critique / importante / secondaire
- **Critere de validation** : ...
- **Adaptation au projet** : ...

#### 2-a. [Titre] (parallele avec 2-b)
- ...

#### 2-b. [Titre] (parallele avec 2-a)
- ...

...

### Carte des dependances
[Schema ou description des dependances entre etapes]

### Matrice des risques
| Etape | Risque | Probabilite | Impact | Solution de secours |
|-------|--------|-------------|--------|---------------------|
| ...   | ...    | ...         | ...    | ...                 |

### Validation du plan
- [x] Couverture des demandes : OUI/NON
- [x] Absence d'etapes manquantes : OUI/NON
- [x] Ordre logique : OUI/NON
- [x] Adaptation au projet : OUI/NON
- [x] Criteres de validation : OUI/NON
- [x] Couverture des risques : OUI/NON
**Plan valide** : OUI / NON (si non, ajuster avant de continuer)
```

---

## Relations avec les autres skills

| Skill | Relation |
|-------|----------|
| **correct-work** | Appelle gen-plan a son Etape 1 pour generer le plan de verification |
| **fullstack-dev** | Aucune relation directe, mais gen-plan peut produire un plan pour un projet fullstack |

---

## Installation et utilisation

### Integration dans une IA cible

Pour integrer ce skill dans une IA cible (ChatGPT, Claude, Mistral, etc.), deux methodes sont possibles :

#### Methode 1 — Copier-coller dans le system prompt

1. Ouvrir le fichier `skill-gen-plan.md`.
2. Copier l'integralite du contenu.
3. Coller dans la section "System prompt" ou "Instructions personnalisees" de l'IA cible.
4. L'IA reconnaitra les mots-cles de declenchement (`gen_plan`, `genere un plan`, `plan d'actions`)
   et executera le protocole automatiquement.

#### Methode 2 — Fichier SKILL.md dans un repertoire de skills

Si l'IA cible dispose d'un systeme de skills (comme Z AI) :

1. Creer le repertoire `skills/gen-plan/`.
2. Copier ce fichier sous le nom `SKILL.md` dans ce repertoire.
3. Le systeme de skills detectera automatiquement le frontmatter YAML et enregistrera le skill.

### Utilisation

Une fois le skill integre, l'utilisateur peut declencher la generation de plan en ecrivant :
- `gen_plan` — declenchement direct
- `genere un plan` — variante naturelle
- `plan d'actions` — variante naturelle

Le skill peut aussi etre appele par le skill `correct-work` en tant que sous-protocole
(lors de l'Etape 1 de correct-work, gen-plan est appele pour generer le plan de verification).

---

## Historique des versions

| Version | Date | Auteurs | Modifications |
|---------|------|---------|---------------|
| 1.0.0 | 2026-06-14 | Z AI | Version initiale — protocole complet en 11 etapes |
