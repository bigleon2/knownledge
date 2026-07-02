#!/bin/bash
# Script d'installation des configurations mémoire pour z.ai et qwen
# Usage : bash install-memory-config.sh

echo "🧠 Installation des configurations mémoire"
echo "=========================================="
echo ""

# Vérifier que les fichiers existent
if [ ! -f "/home/z/my-project/memory-config-zai.md" ]; then
    echo "❌ Fichier memory-config-zai.md non trouvé"
    exit 1
fi

if [ ! -f "/home/z/my-project/memory-config-qwen.md" ]; then
    echo "❌ Fichier memory-config-qwen.md non trouvé"
    exit 1
fi

echo "✅ Fichiers de configuration trouvés"
echo ""

# Extraire le texte à copier pour z.ai
echo "📋 Configuration pour z.ai (Ingénieur Système)"
echo "----------------------------------------------"
echo "1. Va sur https://chat.z.ai/"
echo "2. Settings → Memory → Active"
echo "3. Copie le texte ci-dessous :"
echo ""
grep -A 1000 "TEXTE À COPIER DANS Z.AI" /home/z/my-project/memory-config-zai.md | grep -B 1000 "^---$" | head -n -1 | tail -n +2
echo ""
echo "4. Colle-le dans le chat"
echo "5. z.ai répondra : 'Mémoire configurée pour François...'"
echo ""
echo "=========================================="
echo ""

# Extraire le texte à copier pour qwen
echo "📋 Configuration pour qwen (Développement)"
echo "----------------------------------------------"
echo "1. Va sur https://chat.qwen.ai/"
echo "2. Settings → Personalization → Memory → Active"
echo "3. Copie le texte ci-dessous :"
echo ""
grep -A 1000 "TEXTE À COPIER DANS QWEN" /home/z/my-project/memory-config-qwen.md | grep -B 1000 "^---$" | head -n -1 | tail -n +2
echo ""
echo "4. Colle-le dans le chat"
echo "5. qwen répondra : 'Mémoire configurée pour François...'"
echo ""
echo "=========================================="
echo ""
echo "✅ Installation terminée"
echo ""
echo "📌 Pour tester :"
echo "   - z.ai : Dis 'gen-plan:' → doit appliquer les 11 étapes"
echo "   - qwen : Dis '<py script.py>' → doit créer un script Python"