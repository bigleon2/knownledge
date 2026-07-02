# SKILL : correct-work

> Skill de verification du travail realise. Aussi connu sous le nom "verify-work".

---

```yaml
---
name: correct-work
aka: verify-work
version: 1.0.0
date: 2026-06-14
authors: [Z AI]
description: >
  Skill de verification du travail realise. Declenche a chaque fois que l'utilisateur ecrit
  "verifie ton travail", "verifie tes resultats" ou "verifie ton code". Execute 5 etapes systematiques : plan d'actions
  robuste adapte au projet pour optimiser la verification, detection et correction des erreurs/oublis,
  verification de la structure du code et des conflits, verification des interactions entre composants
  (API frontend-backend, props, state, data flow), verification de la coherence des raisonnements
  et des resultats. S'applique a toute tache anterieure completee (code, documents, PDF, analyses,
  web dev, etc.). Supporte deux modes : correct_work(projet) pour une verification complete du projet
  avec gestion du prompt-maitre, et correct_work() / correct_work(cible) pour une verification
  ciblee sans gestion du prompt-maitre.

  Note : ce skill est aussi connu sous le nom "verify-work". Les deux noms font reference
  au meme skill. Dans ce document, nous utilisons "correct-work" comme nom principal.
---
```

---

## Table des matieres

1. [Presentation](#presentation)
2. [Mots-cles de declenchement](#mots-cles-de-declenchement)
3. [Modes d'appel](#modes-dappel)
4. [Protocol (5 etapes sequentielles)](#protocol-5-etapes-sequentielles)
   - [Etape 1 — Plan d'actions (appel au skill gen-plan)](#etape-1--plan-dactions-appel-au-skill-gen-plan)
   - [Etape 2 — Erreurs et omissions](#etape-2--erreurs-et-omissions)
   - [Etape 3 — Structure du code et conflits](#etape-3--structure-du-code-et-conflits)
   - [Etape 4 — Verification des interactions](#etape-4--verification-des-interactions)
   - [Etape 5 — Coherence des raisonnements et des resultats](#etape-5--coherence-des-raisonnements-et-des-resultats)
5. [Format du rapport de verification](#format-du-rapport-de-verification)
6. [Relations avec les autres skills](#relations-avec-les-autres-skills)
7. [Installation et utilisation](#installation-et-utilisation)
8. [Historique des versions](#historique-des-versions)

---

## Presentation

Ce skill declenche une verification complete en 5 etapes du travail realise dans la session
courante. Il doit etre execute systematiquement lorsque l'utilisateur ecrit "verifie ton travail",
"verifie tes resultats", "verifie ton code" ou toute variante similaire.

Le skill s'applique a tout type de tache anterieure completee : code, documents, PDF, analyses,
developpement web, scripts, etc. Les criteres de verification sont systematiquement adaptes
au type de projet detecte lors de l'Etape 1.

---

## Mots-cles de declenchement

- `verifie ton travail`
- `verifie tes resultats`
- `verifie ton code`
- `correct_work`
- `verify_work`

---

## Modes d'appel

Le comportement du skill depend du mode d'appel :

### Mode PROJET : correct_work(projet)

Verification sur l'ensemble du projet. Gen-plan gere le **prompt-maitre** du projet
(fichier MD de reference). A la premiere analyse, l'integralite du projet est analysee
et le prompt-maitre est genere. Aux appels suivants, seule la derniere version du
prompt-maitre est lue. A la fin, le prompt-maitre est mis a jour si le projet a ete
modifie. Ce mode est optimise pour la performance : l'analyse complete n'est faite
qu'une seule fois.

### Mode CIBLE : correct_work(cible)

Verification sur une tache specifique ou un livrable particulier. Le prompt-maitre n'est
**pas** gere dans ce mode. L'analyse se limite aux fichiers pertinents pour la tache verifiee.

### Mode DIRECT : correct_work()

Identique au mode CIBLE, avec une portee encore plus restreinte. Utile pour une verification
rapide sans analyse approfondie du projet.

---

## Protocol (5 etapes sequentielles)

Le skill s'execute **apres** qu'une tache a ete completee. Il analyse les demandes de
l'utilisateur, genere un plan d'actions robuste, puis parcourt l'integralite du travail
produit dans la session et applique les 5 etapes sequentielles ci-dessous.

---

### Etape 1 — Plan d'actions (appel au skill gen-plan)

**Objectif** : Analyser toutes les demandes de l'utilisateur, lire et analyser le projet
(selon le mode d'appel), puis generer un plan d'actions robuste (structure, logique et
detaille) **adapte au projet** pour optimiser l'execution des taches necessaires pour
repondre a ces demandes.

**Sous-protocole** : Cette etape est realisee en appelant le skill **gen-plan**.
Le skill gen-plan est un skill autonome qui peut aussi etre invoque independamment
par l'utilisateur. Il execute les etapes suivantes :

1. Collecter et analyser les demandes de l'utilisateur (et determiner le mode d'appel)
2. Analyser le projet :
   - **Mode PROJET** : premiere analyse → analyser l'integralite + generer le prompt-maitre ;
     appels suivants → lire la derniere version du prompt-maitre existant
   - **Mode CIBLE/DIRECT** : analyse ponctuelle des fichiers pertinents, pas de prompt-maitre
3. Identifier la nature du projet
4. Identifier les objectifs
5. Decomposer en sous-taches adaptees
6. Detecter les dependances
7. Prioriser
8. Estimer les risques
9. Structurer le plan
10. Valider le plan
11. Mettre a jour le prompt-maitre du projet (uniquement en mode PROJET, si des modifications
    ont ete apportees au projet)

**Principe cle** : Le plan d'actions DOIT etre specifiquement adapte au projet verifie.
Un projet web Next.js n'a pas les memes points de verification qu'un projet Python, un document
PDF ou une analyse de donnees. Le plan doit refleter la nature, la complexite et les specificites
techniques du projet concerne. Les sous-taches, les risques et les criteres de validation
doivent etre calibres en fonction du type de projet (frontend, backend, fullstack, document,
script, etc.).

**Comment appeler gen-plan** :

- **Depuis verify-work(projet)** : executer le skill `gen-plan` en mode PROJET au
  debut de l'Etape 1, puis utiliser le plan genere comme base pour les etapes 2 a 5.
  Gen-plan gerera le prompt-maitre automatiquement.
- **Depuis verify-work(cible)** : executer le skill `gen-plan` en mode CIBLE. Gen-plan
  analysera uniquement les fichiers pertinents sans gerer le prompt-maitre.
- **Depuis l'utilisateur (mode DIRECT)** : l'utilisateur peut invoquer `gen-plan` directement
  pour generer un plan d'actions sans lancer la verification complete et sans gestion du
  prompt-maitre.

**Methode** :

- Appeler le skill **gen-plan** pour generer le plan d'actions adapte au projet.
- Le plan genere par gen-plan sert de base pour les etapes suivantes (2 a 5) de verify-work.
- Si le plan est invalide ou incomplet, ajuster avant de continuer.

---

### Etape 2 — Erreurs et omissions

**Objectif** : Identifier tout ce qui est incorrect, incomplet ou manquant, puis corriger.
Les criteres de verification doivent etre adaptes au type de projet (cf. Etape 1).

**Checklist** :

1. **Relire les specifications initiales** de l'utilisateur et verifier que chaque exigence
   a ete satisfaite. Si une exigence a ete oubliee, la realiser maintenant.
2. **Verifier les donnees factuelles** : noms, chemins, numeros de version, tailles de fichiers,
   counts, etc. — tout chiffre ou valeur assertee doit etre verifie contre la source reelle.
3. **Verifier la coherence linguistique** : la langue utilisee doit etre identique a celle
   de la demande initiale de l'utilisateur. Pas de melange incoherent.
4. **Verifier les fichiers de sortie** : chaque fichier promis existe-t-il ? Est-il lisible ?
   Pas de fichier vide ou corrompu.
5. **Verifier les dependances** : les imports, les chemins de skill, les references croisees
   entre fichiers sont-ils corrects ?
6. **Adapter la verification au projet** : les erreurs et omissions sont evaluees relativement
   au type de projet. Par exemple, une erreur de schema BDD est critique pour un projet fullstack
   mais inexistante pour un document PDF ; une erreur de mise en page est critique pour un PDF
   mais secondaire pour un script.
7. **Corriger** chaque erreur ou omission identifiee.

**Methode** :

- Relire le fichier de travail (`worklog.md`) si disponible pour lister les taches completees.
- Pour chaque livrable (fichier, code, PDF, etc.), l'ouvrir et l'inspecter.
- Comparer le contenu produit aux attentes definies dans la conversation.
- Evaluer les erreurs et omissions en fonction du type de projet identifie a l'Etape 1.

---

### Etape 3 — Structure du code et conflits

**Objectif** : Verifier que le code ou le document est bien structure, qu'il n'y a pas de conflits
entre modules ou de problemes d'architecture. Utilise les tableaux de Karnaugh si necessaire pour
resoudre les conflits logiques ou les conditions contradictoires.

**Adaptation au projet** : Les points de verification ci-dessous s'appliquent differemment
selon le type de projet. Pour du code, verifier les imports, variables, etc. Pour un document
ou une specification, verifier la structure des sections, la coherence des references croisees,
et l'absence de contradictions internes.

**Checklist** :

1. **Imports circulaires** (code) : verifier qu'aucun module n'importe un autre qui l'importe.
2. **Conflits de noms** : deux fonctions/classes/variables avec le meme nom dans des scopes
   qui pourraient interferer. Pour un document, verifier les definitions en double.
3. **Variables non initialisees** ou utilisees avant d'etre definies (code).
4. **Chemins en dur** qui ne fonctionneraient pas dans un autre environnement (code/config).
5. **Gestion des erreurs** : les cas d'erreur sont-ils traites ou le code echouerait silencieusement ?
6. **Doublons** : du code duplique qui devrait etre factorise, ou du contenu duplique dans un document.
7. **Convention de nommage** : coherence dans le style (snake_case, PascalCase, etc.).
8. **Conflits logiques et conditions contradictoires** : si des conditions booleennes
   complexes sont identifiees (ex : XOR, exclusions mutuelles, guard clauses multiples),
   utiliser un **tableau de Karnaugh** pour simplifier, detecter les contradictions
   ou verifier la couverture complete des cas. Cela permet de :
   - Detecter des branches mortes (cas jamais atteints).
   - Simplifier des conditions redondantes.
   - Verifier que des contraintes du type "DRY_RUN XOR LIVE" couvrent bien
     tous les cas sans chevauchement.
   - Pour un document, detecter les contradictions entre sections.
9. **Corriger** chaque probleme de structure ou conflit identifie.

**Methode** :

- Lister tous les fichiers de code modifies ou crees dans la session.
- Pour chaque fichier, verifier les imports, les dependances, les conventions.
- Executer un linter ou des tests si disponibles.
- Verifier que les appels entre modules sont compatibles (bonnes signatures, bons types).
- Si des conditions booleennes complexes ou des exclusions mutuelles sont presentes,
  construire un tableau de Karnaugh pour valider la logique.
- Pour un document/specification, verifier la coherence entre sections et l'absence
  de contradictions internes.

---

### Etape 4 — Verification des interactions

**Objectif** : Verifier que toutes les interactions entre les composants du systeme
fonctionnent correctement. Les points de verification ci-dessous s'appliquent selon le type
de projet. Si c'est necessaire pour verifier les interactions, il faut utiliser les tableaux
de Karnaugh (notamment pour valider des conditions d'activation multiples, des exclusions
mutuelles entre composants, ou des etats de transition contradictoires).

**Adaptation au projet** : Cette etape doit etre adaptee au type de projet verifie :
- **Projet fullstack** : verifier les 5 categories ci-dessous (API, props, state, data flow, services).
- **Projet frontend only** : accent sur les props, le state management et le data flow.
- **Projet backend/API** : accent sur les endpoints, la validation, les communications entre services.
- **Document/PDF/analyse** : verifier les references croisees entre sections, la coherence des
  donnees citees, et les liens entre livrables.
- **Script/automatisation** : verifier les interfaces d'entree/sortie, les appels systeme,
  et les dependances externes.

**Checklist** :

1. **API frontend-backend** (projets fullstack/web) :
   - Chaque endpoint API appele par le frontend existe-t-il cote backend ?
   - Les parametres envoyes par le frontend correspondent-ils a ce que le backend attend
     (noms, types, formats) ?
   - Les reponses du backend sont-elles correctement parsees et utilisees par le frontend ?
   - Les codes d'erreur HTTP sont-ils geres cote frontend (400, 404, 500, etc.) ?
   - Les champs JSON renvoyes par l'API correspondent-ils aux champs attendus par le frontend ?

2. **Props et communication inter-composants** (projets frontend/fullstack) :
   - Les props passees d'un composant parent a un enfant correspondent-elles a l'interface
     attendue par l'enfant (types, noms, optionnalite) ?
   - Les callbacks (onXxx) sont-ils appeles avec les bons arguments et traites correctement ?
   - Y a-t-il des props obligatoires manquantes ou des props non utilisees ?
   - Les valeurs par defaut sont-elles coherentes entre le parent et l'enfant ?

3. **State management (Zustand, Redux, Context, etc.)** (projets frontend/fullstack) :
   - Le store expose-t-il toutes les donnees necessaires aux composants qui l'utilisent ?
   - Les actions du store sont-elles appelees aux bons moments dans le cycle de vie ?
   - Y a-t-il des donnees du store qui ne sont jamais lues (state mort) ?
   - Les transformations de donnees entre l'API et le store sont-elles fideles
     (pas de perte de champs, pas de conversion incorrecte) ?

4. **Flux de donnees bout en bout (data flow)** (tous projets avec flux de donnees) :
   - Tracer un scenario complet (ex : clic utilisateur → appel API → reponse → mise a jour store →
     re-render composant) et verifier que chaque maillon fonctionne.
   - Les donnees affichees a l'ecran proviennent-elles de la bonne source
     (API live vs cache vs state local) ?
   - Les donnees sont-elles rafrachies apres une mutation (POST/PUT/DELETE) ?
   - Les conditions de course (race conditions) sont-elles evitees dans les appels asynchrones ?

5. **Communications entre services (si applicable)** (projets micro-services/distribues) :
   - Les appels entre micro-services ou mini-services passent-ils par les bons ports/URLs ?
   - Le parametre XTransformPort est-il correctement utilise pour les requetes cross-services ?
   - Les WebSockets se connectent-ils au bon endpoint avec les bons parametres ?
   - Les timeouts et reessais sont-ils geres pour les appels reseau ?

6. **References croisees et coherence entre livrables** (documents, specifications, analyses) :
   - Les references d'une section a une autre sont-elles correctes (numeros de section, noms) ?
   - Les donnees citees dans un livrable correspondent-elles aux donnees source ?
   - Les liens entre fichiers (imports, inclusions, dependances) sont-ils valides ?
   - Y a-t-il des contradictions entre differents livrables du meme projet ?

7. **Corriger** chaque probleme d'interaction identifie.

---

### Etape 5 — Coherence des raisonnements et des resultats

**Objectif** : Verifier que la logique suivie est coherente de bout en bout et que les
resultats finaux correspondent aux conclusions intermediaires.

**Checklist** :

1. **Coherence logique** : les etapes de raisonnement s'enchainent-elles logiquement ?
   Pas de saut non justifie, pas de conclusion qui contredit une premissse.
2. **Coherence numerique** : les chiffres s'additionnent-ils ? Les pourcentages sont-ils
   coherents avec les valeurs absolues ? Les tailles de fichiers correspondent-elles ?
3. **Coherence temporelle** : les dates, versions, chronologies sont-elles coherentes
   entre elles et avec le contexte ?
4. **Resultat attendu vs resultat obtenu** : ce qui a ete promis correspond-il a ce
   qui a ete livre ? Si un ecart existe, l'expliquer.
5. **Coherence entre fichiers** : si plusieurs livrables ont ete produits, sont-ils
   coherents entre eux (pas de contradiction entre le contenu de deux fichiers) ?
6. **Corriger** toute incoherence identifiee.

**Methode** :

- Reconstituer le fil logique de la session : demande utilisateur → plan → execution → resultats.
- Pointer chaque assertion et verifier qu'elle est justifiee.
- Pour les donnees numeriques, refaire les calculs si necessaire.
- Comparer les sorties reelles aux sorties attendues.

---

## Format du rapport de verification

Apres les 5 etapes, produire un rapport structure :

```
## Verification du travail

### Mode d'appel
- correct_work(projet) / correct_work() / correct_work(cible)

### Etape 1 — Plan d'actions (gen-plan)
- [x] / [!] Objectif 1 : statut
- [x] / [!] Objectif 2 : statut
- ...
**Plan valide** : OUI / NON (si non, ajuster avant de continuer)
**Prompt-maitre** : genere / lu / non applicable (selon le mode)

### Etape 2 — Erreurs et omissions
- [x] / [!] Exigence 1 : statut
- [x] / [!] Exigence 2 : statut
- ...
**Corrections appliquees** : (liste des corrections faites, ou "aucune")

### Etape 3 — Structure et conflits
- [x] / [!] Point 1 : statut
- [x] / [!] Point 2 : statut
- ...
**Corrections appliquees** : (liste des corrections faites, ou "aucune")

### Etape 4 — Verification des interactions
- [x] / [!] API frontend-backend : statut
- [x] / [!] Props inter-composants : statut
- [x] / [!] State management : statut
- [x] / [!] Flux de donnees bout en bout : statut
- [x] / [!] Communications entre services : statut
- ...
**Corrections appliquees** : (liste des corrections faites, ou "aucune")

### Etape 5 — Coherence des raisonnements
- [x] / [!] Point 1 : statut
- [x] / [!] Point 2 : statut
- ...
**Corrections appliquees** : (liste des corrections faites, ou "aucune")

### Bilan
- Erreurs corrigees : N
- Omissions comblees : N
- Conflits resolus : N
- Interactions corrigees : N
- Incoherences corrigees : N
- Adaptation au projet : OK / A AJUSTER
- Prompt-maitre : mis a jour / non modifie / non applicable
- Statut global : OK / CORRIGE
```

---

## Relations avec les autres skills

| Skill | Relation |
|-------|----------|
| **gen-plan** | Correct-work appelle gen-plan a son Etape 1 pour generer le plan de verification |
| **fullstack-dev** | Correct-work peut verifier un projet fullstack produit par ce skill |

---

## Installation et utilisation

### Integration dans une IA cible

Pour integrer ce skill dans une IA cible (ChatGPT, Claude, Mistral, etc.), deux methodes sont possibles :

#### Methode 1 — Copier-coller dans le system prompt

1. Ouvrir le fichier `skill-correct-work.md`.
2. Copier l'integralite du contenu.
3. Coller dans la section "System prompt" ou "Instructions personnalisees" de l'IA cible.
4. L'IA reconnaitra les mots-cles de declenchement (`verifie ton travail`, `correct_work`, etc.)
   et executera le protocole automatiquement.

#### Methode 2 — Fichier SKILL.md dans un repertoire de skills

Si l'IA cible dispose d'un systeme de skills (comme Z AI) :

1. Creer le repertoire `skills/correct-work/`.
2. Copier ce fichier sous le nom `SKILL.md` dans ce repertoire.
3. Le systeme de skills detectera automatiquement le frontmatter YAML et enregistrera le skill.

### Dependance

Ce skill depend du skill **gen-plan** pour son Etape 1. Pour un fonctionnement complet,
assurez-vous que gen-plan est egalement integre dans l'IA cible. Si gen-plan n'est pas
disponible, l'Etape 1 devra etre realisee manuellement en suivant le protocole de gen-plan.

### Utilisation

Une fois le skill integre, l'utilisateur peut declencher la verification en ecrivant :
- `verifie ton travail` — declenchement naturel
- `verifie tes resultats` — variante
- `verifie ton code` — variante
- `correct_work` — commande directe
- `verify_work` — alias anglais

Pour choisir le mode d'appel :
- `correct_work(projet)` — verification complete du projet avec gestion du prompt-maitre
- `correct_work(cible)` — verification ciblee sur un livrable specifique
- `correct_work()` — verification rapide sans analyse approfondie

---

## Historique des versions

| Version | Date | Auteurs | Modifications |
|---------|------|---------|---------------|
| 1.0.0 | 2026-06-14 | Z AI | Version initiale — protocole complet en 5 etapes |
