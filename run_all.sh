#!/bin/bash

# ============================================
# DECRYPTOR PRO - Fyxzpedia Engineering
# ============================================

clear

echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║  ██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ║"
echo "║  ██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝ ║"
echo "║  ██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║    ║"
echo "║  ██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔══██╗   ██║    ║"
echo "║  ██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║  ██║   ██║    ║"
echo "║  ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ║"
echo "║                                                               ║"
echo "║  🔓 DECRYPTOR PRO + SOURCE PROTECTOR                         ║"
echo "║  👨‍💻 Fyxzpedia Engineering                                    ║"
echo "║  📱 t.me/Fyxzpedia                                           ║"
echo "║  ▶️  Fyxzpedia-vil                                            ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""
echo "📌 Pilih Menu:"
echo "  1. 🔓 Decode PyEncrypter File (cheos.py)"
echo "  2. 🔐 Protect Source Code (Zero-Width)"
echo "  3. ℹ️  Info Tools"
echo "  0. 🚪 Exit"
echo ""
read -p "[>] Pilih: " choice

case $choice in
    1)
        python3 cheos_decryptor.py
        ;;
    2)
        python3 protect_tools.py
        ;;
    3)
        echo ""
        echo "📌 Tools ini terdiri dari:"
        echo "  1. cheos_decryptor.py - Untuk mendekripsi file PyEncrypter"
        echo "  2. protect_tools.py - Untuk memproteksi source code"
        echo ""
        echo "📌 Cara Penggunaan:"
        echo "  1. Jalankan cheos_decryptor.py untuk decode file"
        echo "  2. Jalankan protect_tools.py untuk proteksi source"
        echo ""
        echo "📌 Developer: Fyxzpedia Engineering"
        echo "   Telegram: t.me/Fyxzpedia"
        echo "   YouTube: Fyxzpedia-vil"
        read -p "Tekan Enter untuk lanjut..."
        ;;
    0)
        echo "✅ Terima kasih!"
        exit 0
        ;;
    *)
        echo "❌ Pilihan tidak valid!"
        sleep 1
        ;;
esac

bash run_all.sh
