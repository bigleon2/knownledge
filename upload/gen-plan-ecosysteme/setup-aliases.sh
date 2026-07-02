#!/bin/bash
# Script d'installation des alias shell pour le launcher multi-contexte
# Usage : source setup-aliases.sh

echo "🔧 Installation des alias shell pour le launcher IA..."

# Détection du shell
SHELL_RC=""
if [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
    echo "   Shell détecté : zsh"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
    echo "   Shell détecté : bash"
else
    SHELL_RC="$HOME/.bashrc"
    echo "   Shell par défaut : bash"
fi

# Backup du fichier RC
if [ -f "$SHELL_RC" ]; then
    cp "$SHELL_RC" "$SHELL_RC.backup.$(date +%Y%m%d_%H%M%S)"
    echo "   ✅ Backup créé : $SHELL_RC.backup.*"
fi

# Alias à ajouter
ALIASES='
# === Alias Launcher IA Multi-Contexte ===
# Ajouté le '"$(date +%Y-%m-%d)"' par setup-aliases.sh

# Lance le launcher (auto-détection)
alias ai="python3 /home/z/my-project/launcher.py"

# Contexte SYSTÈME (z.ai par défaut)
alias sys="python3 /home/z/my-project/launcher.py system"
alias system="python3 /home/z/my-project/launcher.py system"

# Contexte CODAGE (qwen par défaut)
alias code="python3 /home/z/my-project/launcher.py code"
alias dev="python3 /home/z/my-project/launcher.py code"

# Combinaisons populaires
alias sys-zai="python3 /home/z/my-project/launcher.py system z.ai"
alias sys-qwen="python3 /home/z/my-project/launcher.py system qwen"
alias code-qwen="python3 /home/z/my-project/launcher.py code qwen"
alias code-chatgpt="python3 /home/z/my-project/launcher.py code chatgpt"

# Configuration et liste
alias ai-config="python3 /home/z/my-project/launcher.py --config"
alias ai-list="python3 /home/z/my-project/launcher.py --list"

# === Fin des alias Launcher IA ===
'

# Vérifier si les alias existent déjà
if grep -q "# === Alias Launcher IA Multi-Contexte ===" "$SHELL_RC" 2>/dev/null; then
    echo "   ⚠️  Les alias existent déjà dans $SHELL_RC"
    echo "   Supprimer manuellement la section si vous voulez réinstaller"
else
    # Ajouter les aliases
    echo "" >> "$SHELL_RC"
    echo "$ALIASES" >> "$SHELL_RC"
    echo "   ✅ Alias ajoutés à $SHELL_RC"
fi

echo ""
echo "📋 Alias installés :"
echo "   ai              → Auto-détection contexte + IA"
echo "   sys / system    → Contexte Système (z.ai par défaut)"
echo "   code / dev      → Contexte Codage (qwen par défaut)"
echo "   sys-zai         → Système sur z.ai"
echo "   sys-qwen        → Système sur qwen"
echo "   code-qwen       → Codage sur qwen"
echo "   code-chatgpt    → Codage sur ChatGPT"
echo "   ai-config       → Configurer les IA par défaut"
echo "   ai-list         → Lister contextes et IA"
echo ""
echo "🔄 Pour activer immédiatement, exécutez :"
echo "   source $SHELL_RC"
echo ""
echo "✅ Installation terminée !"