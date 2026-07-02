# 🧠 Instructions pour Mémoire Intégrée de Chaque IA

**Date** : 2026-06-21  
**Auteur** : François  
**Usage** : Suivre ces instructions pour configurer la mémoire permanente de chaque IA

---

## 📊 Comparatif des IA

| IA | Mémoire Permanente | Project Knowledge | Recommandation |
|----|-------------------|-------------------|----------------|
| **z.ai** | ✅ Oui | ✅ Oui | ⭐ **Utiliser Project Knowledge** |
| **qwen** | ✅ Oui | ❌ Non | ⭐ **Utiliser Mémoire** |
| **manus** | ✅ Oui | ✅ Oui | ⭐ **Utiliser Project Knowledge** |
| **copilot** | ✅ Oui | ❌ Non | ⭐ **Utiliser Mémoire** |
| **chatgpt** | ✅ Oui | ✅ Oui (GPTs) | ⭐ **Créer un GPT personnalisé** |
| **perplexity** | ⚠️ Limitée | ❌ Non | ⚠️ **Utiliser Collections** |
| **gemini** | ✅ Oui | ✅ Oui (Gems) | ⭐ **Créer un Gem personnalisé** |
| **claude** | ✅ Oui | ✅ Oui (Projects) | ⭐ **Utiliser Project Knowledge** |
| **codex** | ✅ Oui | ❌ Non | ⭐ **Utiliser Mémoire** |

---

## 🟢 z.ai (Zhipu AI / GLM)

### Option A : Project Knowledge (Recommandé)

1. Va sur https://chat.z.ai/
2. Connecte-toi à ton compte
3. Va dans **Settings → Projects** (ou "项目")
4. Crée un nouveau projet : **"DJ TRAKTOR Écosystème"**
5. Dans **Knowledge** (知识库), ajoute le contenu du prompt maître :
   - Copie le contenu de `/home/z/my-project/prompt-maitre.md`
   - Colle-le dans la zone de knowledge
6. Sauvegarde le projet
7. **À chaque session** : Sélectionne ce projet avant de commencer

### Option B : Mémoire Intégrée

1. Va dans **Settings → Memory** (记忆)
2. Active la mémoire si ce n'est pas déjà fait
3. Dis à z.ai :
   ```
   Mémorise ceci de façon permanente :
   
   Je suis François, DJ avec KONTROL S4 MK32 + TRAKTOR 3.11, 50 ans, France.
   J'ai un écosystème de 12 agents spécialisés et 69 skills.
   Les agents sont : general-purpose, Explore, Plan, frontend-styling-expert, 
   full-stack-developer, ppt-expert, tsi-expert, kontrol-s4-expert, 
   python-executor, pdf-expert, image-analyst, auto-tagger.
   
   Quand je dis "gen-plan:", "plan d'actions", ou "<py script.py>", 
   utilise le protocole gen-plan avec les 11 étapes séquentielles.
   
   Communique toujours en français.
   ```
4. z.ai le mémorisera et le rappellera à chaque session

---

## 🟢 Qwen (Alibaba)

### Mémoire Intégrée (Déjà active pour toi)

1. Va dans **Settings → Personalization → Memory**
2. La mémoire est déjà active (tu as déjà des souvenirs)
3. Dis à Qwen :
   ```
   Ajoute à ma mémoire permanente :
   
   J'utilise un écosystème de 12 agents spécialisés et 69 skills pour l'orchestration.
   Les agents DJ sont : tsi-expert, kontrol-s4-expert, python-executor, 
   pdf-expert, image-analyst, auto-tagger.
   
   Quand je dis "gen-plan:" ou "plan d'actions", applique le protocole 
   gen-plan (11 étapes séquentielles) avec sélection performance-driven.
   
   Mes IA préférées sont : z.ai, qwen, manus, copilot, chatgpt.
   ```
4. Qwen le mémorisera automatiquement

---

## 🟢 Manus AI

### Project Knowledge (Recommandé)

1. Va sur https://manus.im/
2. Connecte-toi
3. Va dans **Projects** (ou "项目")
4. Crée un nouveau projet : **"DJ TRAKTOR Écosystème"**
5. Ajoute le prompt maître comme **Knowledge Base**
6. **À chaque session** : Sélectionne ce projet

### Mémoire Intégrée

1. Va dans **Settings → Memory**
2. Active la mémoire
3. Dis à Manus :
   ```
   Mémorise : Je suis François, DJ TRAKTOR, j'utilise un écosystème 
   de 12 agents et 69 skills. Protocole gen-plan en 11 étapes. 
   Communique en français.
   ```

---

## 🟢 Microsoft Copilot

### Mémoire Intégrée

1. Va sur https://copilot.microsoft.com/
2. Connecte-toi avec ton compte Microsoft
3. Va dans **Settings → Personalization → Memory**
4. Active la mémoire
5. Dis à Copilot :
   ```
   Mémorise ceci :
   
   Je suis François, DJ avec KONTROL S4 MK32 + TRAKTOR 3.11.
   J'ai un écosystème de 12 agents spécialisés (tsi-expert, kontrol-s4-expert, 
   python-executor, pdf-expert, image-analyst, auto-tagger) et 69 skills.
   
   Utilise le protocole gen-plan (11 étapes) quand je dis "gen-plan:" 
   ou "plan d'actions". Communique en français.
   ```

---

## 🟢 ChatGPT (OpenAI)

### Option A : GPT Personnalisé (Recommandé)

1. Va sur https://chat.openai.com/gpts
2. Clique sur **"+ Create"** (Créer)
3. Configure le GPT :
   - **Name** : "DJ TRAKTOR Assistant"
   - **Description** : "Assistant pour DJ François avec écosystème 12 agents + 69 skills"
   - **Instructions** : Colle le contenu du prompt maître
   - **Knowledge** : Upload le fichier `prompt-maitre.md`
4. Sauvegarde le GPT
5. **À chaque session** : Utilise ce GPT personnalisé

### Option B : Mémoire Intégrée

1. Va dans **Settings → Personalization → Memory**
2. Active la mémoire
3. Dis à ChatGPT :
   ```
   Mémorise : Je suis François, DJ TRAKTOR, 50 ans, France.
   Écosystème : 12 agents (tsi-expert, kontrol-s4-expert, python-executor, 
   pdf-expert, image-analyst, auto-tagger) + 69 skills.
   Protocole gen-plan (11 étapes séquentielles).
   Communication en français.
   ```

---

## 🟡 Perplexity AI

### Collections (Recommandé)

1. Va sur https://www.perplexity.ai/
2. Va dans **Library → Collections**
3. Crée une nouvelle collection : **"DJ TRAKTOR Écosystème"**
4. Ajoute le prompt maître comme **Context**
5. **À chaque session** : Sélectionne cette collection

**Note** : Perplexity a une mémoire limitée, utilise plutôt les Collections

---

## 🟢 Gemini (Google)

### Option A : Gem Personnalisé (Recommandé)

1. Va sur https://gemini.google.com/
2. Va dans **Gems** (ou "Extensions")
3. Crée un nouveau Gem : **"DJ TRAKTOR Assistant"**
4. Ajoute les instructions : Colle le prompt maître
5. Sauvegarde le Gem
6. **À chaque session** : Utilise ce Gem

### Option B : Mémoire Intégrée

1. Va dans **Settings → Memory**
2. Active "Save things to memory"
3. Dis à Gemini :
   ```
   Mémorise : Je suis François, DJ TRAKTOR.
   Écosystème : 12 agents + 69 skills.
   Protocole gen-plan (11 étapes).
   Communication en français.
   ```

---

## 🟢 Claude (Anthropic)

### Project Knowledge (Recommandé)

1. Va sur https://claude.ai/
2. Va dans **Projects**
3. Crée un nouveau projet : **"DJ TRAKTOR Écosystème"**
4. Dans **Project Knowledge**, ajoute :
   - Upload le fichier `prompt-maitre.md`
   - Ou colle le contenu directement
5. **À chaque session** : Sélectionne ce projet

### Mémoire Intégrée

1. Va dans **Settings → Memory**
2. Active la mémoire
3. Dis à Claude :
   ```
   Mémorise : Je suis François, DJ TRAKTOR, 50 ans, France.
   Écosystème : 12 agents (tsi-expert, kontrol-s4-expert, python-executor, 
   pdf-expert, image-analyst, auto-tagger) + 69 skills.
   Protocole gen-plan (11 étapes séquentielles).
   Communication en français.
   ```

---

## 🟢 Codex (OpenAI)

### Mémoire Intégrée

1. Va sur https://chat.openai.com/?model=codex
2. Va dans **Settings → Memory**
3. Active la mémoire
4. Dis à Codex :
   ```
   Mémorise : Je suis François, DJ TRAKTOR.
   Écosystème : 12 agents + 69 skills.
   Protocole gen-plan (11 étapes).
   Quand je dis "<py script.py>", exécute le script Python.
   Communication en français.
   ```

---

## 🎯 Résumé des Actions par IA

### Pour Chaque IA, Faire :

1. **Activer la mémoire** (si disponible)
2. **Créer un Project/Gem/GPT** (si disponible)
3. **Ajouter le prompt maître** comme knowledge/context
4. **Dire à l'IA** : "Mémorise ceci : [résumé du prompt maître]"

### Résumé du Prompt Maître à Mémoriser

```
Je suis François, DJ avec KONTROL S4 MK32 + TRAKTOR 3.11, 50 ans, France.
J'ai un écosystème de 12 agents spécialisés et 69 skills.

Agents DJ : tsi-expert, kontrol-s4-expert, python-executor, 
pdf-expert, image-analyst, auto-tagger.

Agents génériques : general-purpose, Explore, Plan, 
frontend-styling-expert, full-stack-developer, ppt-expert.

Protocole gen-plan : 11 étapes séquentielles pour orchestration.
Matrice performance-driven : Skill + Agent > Skill seul > Agent seul > General.

Déclencheurs : "gen-plan:", "plan d'actions", "<py script.py>", 
"crée un mapping TSI", "tag mes fichiers audio".

Communication : Toujours en français.
```

---

## 🚀 Script d'Automatisation (Optionnel)

Tu peux utiliser le script `launcher.py` pour automatiser le lancement :

```bash
# Lancer z.ai avec prompt maître pré-chargé
python3 /home/z/my-project/launcher.py z.ai

# Lancer qwen
python3 /home/z/my-project/launcher.py qwen

# Auto-détection
python3 /home/z/my-project/launcher.py --auto
```

---

## ✅ Checklist Finale

Pour chaque IA, vérifier :

- [ ] Mémoire activée
- [ ] Project/Gem/GPT créé (si disponible)
- [ ] Prompt maître ajouté comme knowledge
- [ ] Résumé mémorisé par l'IA
- [ ] Test de fonctionnement (dire "gen-plan:" et vérifier réponse)

---

**Fin des Instructions**

*Généré le 2026-06-21 pour François — DJ, développeur C/C++, utilisateur TRAKTOR*