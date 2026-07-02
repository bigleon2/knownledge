# SKILL : fullstack-dev

> Fullstack web development with Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui, Prisma ORM.

---

```yaml
---
name: fullstack-dev
version: 1.0.0
date: 2026-06-14
authors: [Z AI]
description: "Fullstack web development with Next.js 16, TypeScript, Tailwind CSS 4, shadcn/ui, Prisma ORM. Use when: building web apps, creating UI components, setting up database schemas, implementing API routes, adding websocket/socket.io support, fullstack project scaffolding, frontend development, backend development, web dev, Next.js app."
argument-hint: "Describe the fullstack feature or app you want to build"
---
```

---

## Table des matieres

1. [Presentation](#presentation)
2. [Mots-cles de declenchement](#mots-cles-de-declenchement)
3. [Initialisation (OBLIGATOIRE)](#initialisation-obligatoire)
4. [Regles UI importantes](#regles-ui-importantes)
5. [Informations du projet](#informations-du-projet)
6. [Stack technologique](#stack-technologique)
7. [Prisma et base de donnees](#prisma-et-base-de-donnees)
8. [Mini Service](#mini-service)
9. [Gateway et requetes API](#gateway-et-requetes-api)
10. [WebSocket / Socket.io](#websocket--socketio)
11. [Style de code](#style-de-code)
12. [Styling](#styling)
13. [Standards UI/UX](#standards-uiux)
14. [Relations avec les autres skills](#relations-avec-les-autres-skills)
15. [Installation et utilisation](#installation-et-utilisation)
16. [Historique des versions](#historique-des-versions)

---

## Presentation

Ce skill est le skill natif de developpement web fullstack integre dans le systeme. Il
fournit un environnement complet pour construire des applications web avec Next.js 16,
TypeScript, Tailwind CSS 4, shadcn/ui et Prisma ORM. Il gere l'initialisation du projet,
les regles de developpement, la stack technologique, les services mini, le gateway API,
les WebSockets, le style et les standards UI/UX.

Contrairement aux skills gen-plan et correct-work qui sont des protocoles de verification,
fullstack-dev est un skill de production : il genere du code, cree des fichiers et construit
des applications web fonctionnelles.

---

## Mots-cles de declenchement

- `build a web app`
- `create a website`
- `fullstack`
- `Next.js`
- `web dev`
- Toute demande de creation d'application web ou de composant UI

---

## Initialisation (OBLIGATOIRE)

Avant d'ecrire tout code, vous DEVEZ executer la commande suivante pour initialiser
l'environnement de developpement fullstack :

```bash
curl https://z-cdn.chatglm.cn/fullstack/init-fullstack_1775040338514.sh | bash
```

Attendre que le script se termine avec succes avant de proceder a toute modification de code.

---

## Regles UI importantes

- Utiliser les composants shadcn/ui existants au lieu de construire depuis zero. Tous les
  composants dans le dossier `src/components/ui` existent deja.
- Alignement et padding des cartes — S'assurer que toutes les cartes sont correctement
  alignees avec un padding coherent (utiliser `p-4` ou `p-6` pour le contenu, `gap-4` ou
  `gap-6` pour l'espacement).
- Gestion des listes longues — Definir une hauteur maximale avec defilement
  (`max-h-96 overflow-y-auto`) et implementer un style de barre de defilement personnalise
  pour une meilleure apparence.

---

## Informations du projet

Il y a deja un projet dans le repertoire courant. (Next.js 16 avec App Router)

### Environnement de developpement

**IMPORTANT** : `bun run dev` sera execute automatiquement par le systeme. Ne PAS l'executer.
Utiliser `bun run lint` pour verifier la qualite du code.

**IMPORTANT** : L'utilisateur ne peut voir que la route `/` definie dans `src/app/page.tsx`.
Ne PAS ecrire d'autre route.

**IMPORTANT** : Le projet Next.js ne peut utiliser que le port 3000 dans le serveur de
developpement auto. Ne jamais utiliser `bun run build`.

**IMPORTANT** : `z-ai-web-dev-sdk` DOIT etre utilise uniquement cote backend ! Ne PAS
l'utiliser cote client.

### Journal du serveur de dev

**IMPORTANT** : Lire `/home/z/my-project/dev.log` pour voir le journal du serveur de dev.
Seulement lire les journaux les plus recents pour eviter les fichiers de journal volumineux.
Toujours lire le journal de dev quand vous avez fini de coder.

### Commandes Bash

- `bun run lint` — Executer ESLint pour verifier la qualite du code et les regles Next.js

---

## Stack technologique

### Framework principal (NON NEGOCIABLE)

- **Framework** : Next.js 16 avec App Router (REQUIS — ne peut pas etre change)
- **Langage** : TypeScript 5 (REQUIS — ne peut pas etre change)

### Stack technologique standard

Quand les utilisateurs ne specifient pas de preferences, utiliser cette stack complete :

| Composant | Technologie |
|-----------|------------|
| **Styling** | Tailwind CSS 4 avec shadcn/ui |
| **Base de donnees** | Prisma ORM (SQLite client only) avec Prisma Client |
| **Cache** | Cache memoire local, pas de middleware supplementaire (MySQL, Redis, etc.) |
| **Composants UI** | Ensemble complet shadcn/ui (style New York) avec icones Lucide |
| **Authentification** | NextAuth.js v4 disponible |
| **State Management** | Zustand pour le state client, TanStack Query pour le state serveur |

D'autres packages peuvent etre trouves dans `package.json`. Vous pouvez installer de
nouveaux packages si necessaire.

### Politique d'utilisation des bibliotheques

- **TOUJOURS utiliser Next.js 16 et TypeScript** — ce sont des exigences non negociables.
- **Quand les utilisateurs demandent des bibliotheques externes hors stack** : Les rediriger
  poliment vers nos alternatives integrees.
- **Expliquer les avantages** de notre stack predefinie (coherence, optimisation, support).
- **Fournir des solutions equivalentes** avec nos bibliotheques disponibles.

---

## Prisma et base de donnees

Prisma est deja installe et configure. L'utiliser quand vous avez besoin de la base de donnees.

Pour utiliser Prisma et la base de donnees :

1. Modifier `prisma/schema.prisma` pour definir le schema de la base de donnees.
2. Executer `bun run db:push` pour pousser le schema vers la base de donnees.
3. Utiliser `import { db } from '@/lib/db'` pour obtenir le client de base de donnees.

---

## Mini Service

Vous pouvez creer des mini services si necessaire (ex : service websocket). Tous les mini
services doivent etre dans le dossier `mini-services`. Pour chaque mini service :

- Doit etre un nouveau projet bun independant avec son propre port et `package.json`.
- Doit definir `index.ts` ou `index.js` comme fichier d'entree, ex : `mini-services/chat-service/index.ts`.
- Doit definir un port specifique si necessaire, au lieu d'utiliser la variable d'environnement `PORT`.
- Doit demarrer chaque mini service en executant `bun run dev` en arriere-plan.
- La commande executee par `bun run dev` doit supporter le redemarrage automatique quand les
  fichiers changent (preferer `bun --hot`).
- S'assurer que chaque service est demarre.

---

## Gateway et requetes API

Cette machine ne peut exposer qu'un seul port exterieurement, donc une gateway integree
(config dans `Caddyfile`) est incluse avec les limitations suivantes :

- Pour les requetes API impliquant differents ports, le port doit etre specifie dans le
  parametre de requete URL nomme `XTransformPort`. Exemple : `/api/test?XTransformPort=3030`.
- Toutes les requetes API doivent utiliser **uniquement des chemins relatifs**. Ne PAS ecrire
  de chemins absolus dans l'URL de requete API (y compris WebSocket). Exemples :
  - **Interdit** : `fetch('http://localhost:3030/api/test')`
  - **Autorise** : `fetch('/api/test?XTransformPort=3030')`
  - **Interdit** : `io('/:3030')`
  - **Autorise** : `io('/?XTransformPort=3030')`
- Pour les requetes vers differents services, faire directement des requetes cross-origin
  sans utiliser de proxy.

**IMPORTANT** : Ne PAS ecrire le port dans l'URL de requete API, meme en WebSocket. Ecrire
uniquement `XTransformPort` dans le parametre de requete URL.

---

## WebSocket / Socket.io

**IMPORTANT** : Utiliser websocket/socket.io pour supporter la communication en temps reel.
Ne PAS utiliser d'autre methode. Il y a deja une demo websocket pour reference dans le
dossier `examples`.

- La logique backend (via socket.io) doit etre un nouveau mini service avec un autre port (ex : 3003).
- La requete frontend doit TOUJOURS etre `io("/?XTransformPort={Port}")`, et le chemin
  TOUJOURS etre `/` pour que Caddy puisse faire suivre vers le bon port.
- JAMAIS utiliser `io("http://localhost:{Port}")` ou toute connexion directe basee sur le port.

---

## Style de code

- Preferer utiliser les composants et hooks existants.
- TypeScript partout avec typage strict.
- Syntaxe ES6+ import/export.
- Composants shadcn/ui preferes aux implementations personnalisees.
- Utiliser `'use client'` et `'use server'` pour le code cote client et serveur.
- Le type primitif du schema Prisma ne peut pas etre une liste.
- Placer le schema Prisma dans le dossier `prisma`.
- Placer le fichier db dans le dossier `db`.

---

## Styling

1. Utiliser la bibliotheque shadcn/ui sauf si l'utilisateur specifie autre chose.
2. Eviter d'utiliser des couleurs indigo ou bleu sauf si specifie dans la demande de l'utilisateur.
3. DOIT generer des designs responsifs.
4. Le projet de code est rendu sur un fond blanc. Si une couleur de fond differente est
   necessaire, utiliser un element wrapper avec une classe Tailwind de couleur de fond.

---

## Standards UI/UX

### Design visuel

- **Systeme de couleurs** : Utiliser les variables integrees de Tailwind CSS
  (`bg-primary`, `text-primary-foreground`, `bg-background`).
- **Restriction de couleur** : PAS de couleurs indigo ou bleu sauf demande explicite.
- **Support du theme** : Implementer le mode clair/sombre avec `next-themes`.
- **Typographie** : Hierarchie coherente avec des poids et tailles de police appropriees.

### Design responsive (OBLIGATOIRE)

- **Mobile-First** : Concevoir pour mobile, puis ameliorer pour desktop.
- **Breakpoints** : Utiliser les prefixes responsifs Tailwind (`sm:`, `md:`, `lg:`, `xl:`).
- **Touch-Friendly** : Cibles tactiles minimales de 44px pour les elements interactifs.

### Layout (OBLIGATOIRE)

- **Footer sticky requis** : Si un `footer` existe, il DOIT etre colle en bas du viewport
  quand le contenu est plus court qu'une hauteur d'ecran (pas d'espace vide flottant en dessous).
- **Push naturel en cas de depassement** : Quand le contenu depasse la hauteur du viewport,
  le footer DOIT etre pousse naturellement vers le bas (jamais de superposition ou de
  recouvrement du contenu).
- **Implementation recommandee (Tailwind)** : Utiliser un wrapper racine avec
  `min-h-screen flex flex-col`, et appliquer `mt-auto` au `footer`.
- **Zone safe mobile** : Sur les appareils avec zones safe (ex : iOS), le footer DOIT
  respecter les insets de zone safe inferieure quand applicable.

### Accessibilite (OBLIGATOIRE)

- **HTML semantique** : Utiliser `main`, `header`, `nav`, `section`, `article`.
- **Support ARIA** : Roles, labels et descriptions appropriees.
- **Lecteurs d'ecran** : Utiliser la classe `sr-only` pour le contenu destine aux lecteurs d'ecran.
- **Texte alt** : Texte alt descriptif pour toutes les images.
- **Navigation clavier** : S'assurer que tous les elements sont accessibles au clavier.

### Elements interactifs

- **Etats de chargement** : Afficher des spinners/skeletons pendant les operations asynchrones.
- **Gestion des erreurs** : Messages d'erreur clairs et actionnables.
- **Feedback** : Notifications toast pour les actions utilisateur.
- **Animations** : Transitions subtiles avec Framer Motion (hover, focus, transitions de page).
- **Effets hover** : Feedback interactif sur tous les elements cliquables.

### Instructions de preview sandbox (CRITIQUE)

Ce projet s'execute dans un environnement sandbox cloud restreint.

- **JAMAIS** instruire l'utilisateur de visiter `http://localhost:3000`, `127.0.0.1` ou
  tout port local directement. Ces adresses sont internes et non accessibles par l'utilisateur.
- **TOUJOURS** diriger l'utilisateur pour previsualiser l'application en utilisant le
  **Panneau de Preview** situe sur le cote droit de l'interface.
- **TOUJOURS** informer l'utilisateur sur comment voir l'application exterieurement selon
  sa plateforme.

### Auto-verification post-lancement avec Agent Browser (OBLIGATOIRE)

Quand le projet Next.js a demarre avec succes (serveur de dev sur le port 3000 sans erreurs
fatales dans `/home/z/my-project/dev.log`), vous ne DEVEZ PAS considerer la tache terminee
sur la base d'un build propre seul. Un lint qui passe et un serveur en cours d'execution ne
prouvent **pas** que le site fonctionne reellement pour l'utilisateur.

Vous DEVEZ utiliser **Agent Browser** pour effectuer une auto-verification de bout en bout
avant de signaler l'achevement :

1. **Ouvrir la page** — Utiliser Agent Browser pour naviguer vers la route `/` (la seule
   route visible par l'utilisateur). Attendre le chargement complet de la page et capturer
   le resultat rendu.

2. **Verifier que ca rend, pas juste que ca repond** — Confirmer que la page est visuellement
   rendue (pas d'ecran blanc, pas d'error boundary, pas de crash d'hydration). Croiser avec
   `/home/z/my-project/dev.log` pour toute erreur runtime, appel API echoue ou mismatch
   d'hydration apparus pendant la visite.

3. **Verifier l'interactivite principale** — Exercer les flux utilisateur principaux que vous
   venez de construire : cliquer sur les boutons principaux, soumettre les formulaires cles,
   declencher la navigation/onglets/modales, et confirmer que chacun produit le resultat attendu.
   Pour les fonctionnalites basees sur les donnees, confirmer que le frontend recoit et affiche
   reellement les donnees backend/API. Pour les fonctionnalites temps reel (WebSocket/socket.io),
   confirmer que les messages circulent de bout en bout.

4. **Verifier la responsivite et le footer sticky** — Verifier que le layout tient sur les
   largeurs mobile et desktop. Confirmer que le footer colle en bas sur les pages courtes et
   est pousse naturellement sur les pages longues.

5. **Corriger et reverifier** — Si Agent Browser revele une interaction cassee, une erreur
   console/runtime, des donnees manquantes ou un defaut de layout, vous DEVEZ corriger la
   cause racine et relancer la boucle d'auto-verification. Repeter jusqu'a ce que la page
   se charge proprement **et** que chaque interaction principale fonctionne.

6. **Rapporter honnetement** — Seulement apres qu'Agent Browser confirme que le site est
   interactif et fonctionnel, vous pouvez signaler la tache comme terminee. Si un flux
   specifique ne peut genuement pas etre verifie dans le navigateur, le dire explicitement
   plutot que de pretendre le succes.

**CRITIQUE** : "Ca compile" / "le serveur est up" n'est jamais une preuve suffisante
d'achevement. L'interactivite verifiee par navigateur est le standard requis pour dire
que c'est termine.

---

## Relations avec les autres skills

| Skill | Relation |
|-------|----------|
| **correct-work** | Peut verifier un projet fullstack produit par ce skill |
| **gen-plan** | Peut generer un plan d'actions pour un projet fullstack avant ou apres le developpement |

---

## Installation et utilisation

### Nature du skill

Ce skill est un **skill natif** du systeme Z AI. Contrairement a gen-plan et correct-work
qui sont des skills custom definis par le meta-prompt-maitre, fullstack-dev existe deja
dans le systeme et ne doit **pas** etre duplique ou reecrit.

### Integration dans une IA cible

Pour integrer ce skill dans une IA cible (ChatGPT, Claude, Mistral, etc.) :

#### Methode 1 — Copier-coller dans le system prompt

1. Ouvrir le fichier `skill-fullstack-dev.md`.
2. Copier l'integralite du contenu.
3. Coller dans la section "System prompt" ou "Instructions personnalisees" de l'IA cible.
4. L'IA appliquera les regles et standards automatiquement lors des demandes de developpement web.

#### Methode 2 — Fichier SKILL.md dans un repertoire de skills

Si l'IA cible dispose d'un systeme de skills (comme Z AI) :

1. Creer le repertoire `skills/fullstack-dev/`.
2. Copier ce fichier sous le nom `SKILL.md` dans ce repertoire.
3. Le systeme de skills detectera automatiquement le frontmatter YAML et enregistrera le skill.

### Utilisation

Ce skill se declenche automatiquement lorsque l'utilisateur demande la creation d'une
application web, d'un site internet ou de composants UI. Aucune commande specifique n'est
necessaire — les mots-cles de declenchement sont listes ci-dessus.

### Prerequis

- Environnement Node.js avec bun installe
- Next.js 16 avec App Router
- Tailwind CSS 4 et shadcn/ui configures
- Prisma ORM installe

---

## Historique des versions

| Version | Date | Auteurs | Modifications |
|---------|------|---------|---------------|
| 1.0.0 | 2026-06-14 | Z AI | Version initiale — traduction francaise du skill natif |
