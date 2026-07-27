#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  ██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ║
║  ██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝ ║
║  ██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║    ║
║  ██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔══██╗   ██║    ║
║  ██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║  ██║   ██║    ║
║  ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝    ║
║                                                               ║
║  🔓 DEOBFUSCATE TOOLS v3.0 - ALL IN ONE                      ║
║  👨‍💻 Fyxzpedia Engineering                                    ║
║  📱 t.me/Fyxzpedia                                           ║
║  ▶️  Fyxzpedia-vil                                            ║
║                                                               ║
║  📂 Auto Clone | 🔍 Find File | 💾 Save to Internal          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import subprocess
import base64
import zlib
import marshal
import re
import shutil
import time
from datetime import datetime
from pathlib import Path

# ================ KONFIGURASI ================
VERSION = "3.0"
DEVELOPER = "Fyxzpedia Engineering"
TELEGRAM = "t.me/Fyxzpedia"
YOUTUBE = "Fyxzpedia-vil"
GITHUB_REPO = "https://github.com/Fyxzpediaa/Deobfuscate-Tools.git"
APP_NAME = "Deobfuscate-Tools"

# Storage Paths
INTERNAL_BASE = "/sdcard"
APP_DIR = f"{INTERNAL_BASE}/Deobfuscate"
DECODED_DIR = f"{APP_DIR}/Decoded"
PROTECTED_DIR = f"{APP_DIR}/Protected"
LOG_DIR = f"{APP_DIR}/Logs"

COLORS = {
    'RED': '\033[91m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'BLUE': '\033[94m',
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'WHITE': '\033[97m',
    'BOLD': '\033[1m',
    'DIM': '\033[2m',
    'BLINK': '\033[5m',
    'RESET': '\033[0m'
}

BANNER = f"""
{COLORS['CYAN']}╔═══════════════════════════════════════════════════════════════╗
║                                                                   ║
║  ██████╗ ███████╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗     ║
║  ██╔══██╗██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝     ║
║  ██║  ██║█████╗  ██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║        ║
║  ██║  ██║██╔══╝  ██║     ██╔══██╗  ╚██╔╝  ██╔══██╗   ██║        ║
║  ██████╔╝███████╗╚██████╗██║  ██║   ██║   ██║  ██║   ██║        ║
║  ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝        ║
║                                                                   ║
║  {COLORS['YELLOW']}🔓 DEOBFUSCATE TOOLS v{VERSION}{COLORS['CYAN']}                                 ║
║  {COLORS['GREEN']}👨‍💻 {DEVELOPER}{COLORS['CYAN']}                                          ║
║  {COLORS['PURPLE']}📱 {TELEGRAM}{COLORS['CYAN']}                                             ║
║  {COLORS['BLUE']}▶️  {YOUTUBE}{COLORS['CYAN']}                                              ║
║  {COLORS['GREEN']}📂 Save: {DECODED_DIR}{COLORS['CYAN']}   ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝{COLORS['RESET']}
"""

# ================ ANIMATION ================

def loading_animation(message, duration=2):
    """Animasi loading keren"""
    frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
    for i in range(duration * 10):
        frame = frames[i % len(frames)]
        sys.stdout.write(f"\r{COLORS['CYAN']}{frame} {message}{' ' * 20}{COLORS['RESET']}")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\r{COLORS['GREEN']}✅ {message}{' ' * 20}{COLORS['RESET']}\n")

def progress_bar(current, total, message=""):
    """Progress bar keren"""
    bar_length = 40
    progress = current / total
    filled = int(bar_length * progress)
    bar = "█" * filled + "░" * (bar_length - filled)
    percent = progress * 100
    sys.stdout.write(f"\r{COLORS['CYAN']}{message} [{bar}] {percent:.1f}%{COLORS['RESET']}")
    sys.stdout.flush()

# ================ STORAGE SETUP ================

def setup_storage():
    """Setup Termux Storage dengan visual keren"""
    print(f"\n{COLORS['BOLD']}{COLORS['YELLOW']}╔═══════════════════════════════════════╗")
    print(f"║     📂 SETUP STORAGE TERMUX        ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
    
    # Cek Termux
    is_termux = os.path.exists('/data/data/com.termux')
    
    if not is_termux:
        print(f"{COLORS['YELLOW']}⚠️  Bukan lingkungan Termux, menggunakan local storage{COLORS['RESET']}")
        return False
    
    # Cek storage
    if os.path.exists(INTERNAL_BASE):
        print(f"{COLORS['GREEN']}✅ Internal Storage terdeteksi: {INTERNAL_BASE}{COLORS['RESET']}")
    else:
        print(f"{COLORS['YELLOW']}⚠️  Storage belum di-setup!{COLORS['RESET']}")
        print(f"{COLORS['CYAN']}[+] Menjalankan termux-setup-storage...{COLORS['RESET']}")
        
        loading_animation("Setup storage", 2)
        
        try:
            subprocess.run(['termux-setup-storage'], check=True)
            print(f"{COLORS['GREEN']}✅ Storage berhasil di-setup!{COLORS['RESET']}")
            time.sleep(1)
        except Exception as e:
            print(f"{COLORS['RED']}❌ Gagal setup storage: {e}{COLORS['RESET']}")
            return False
    
    # Buat folder aplikasi
    print(f"\n{COLORS['CYAN']}[+] Membuat folder aplikasi...{COLORS['RESET']}")
    
    folders = [APP_DIR, DECODED_DIR, PROTECTED_DIR, LOG_DIR]
    for folder in folders:
        try:
            os.makedirs(folder, exist_ok=True)
            print(f"{COLORS['GREEN']}✅ {folder}{COLORS['RESET']}")
        except Exception as e:
            print(f"{COLORS['RED']}❌ Gagal buat {folder}: {e}{COLORS['RESET']}")
    
    # Buat file info
    info_file = f"{APP_DIR}/README.txt"
    with open(info_file, 'w') as f:
        f.write(f"""
╔═══════════════════════════════════════════════════════════════╗
║  📂 DEOBFUSCATE TOOLS - Folder Structure                      ║
║  👨‍💻 Fyxzpedia Engineering                                    ║
║  📱 t.me/Fyxzpedia                                           ║
║  📅 Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}   ║
╚═══════════════════════════════════════════════════════════════╝

📁 Folder Structure:
├── Decoded/     # Hasil deobfuscate
├── Protected/   # Hasil proteksi source
└── Logs/        # Log aktivitas

📌 Cara Mengakses:
- Via Termux: cd /sdcard/Deobfuscate
- Via File Manager: Internal Storage > Deobfuscate
- Via PC: USB Transfer > Internal Storage > Deobfuscate

🔗 GitHub: https://github.com/Fyxzpediaa/Deobfuscate-Tools
""")
    
    print(f"\n{COLORS['GREEN']}✅ Setup storage selesai!{COLORS['RESET']}")
    return True

# ================ CLONE REPOSITORY ================

def clone_repository():
    """Clone repository dari GitHub"""
    print(f"\n{COLORS['BOLD']}{COLORS['BLUE']}╔═══════════════════════════════════════╗")
    print(f"║     📥 CLONE REPOSITORY           ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
    
    # Cek apakah sudah ada
    if os.path.exists(APP_NAME):
        print(f"{COLORS['YELLOW']}⚠️  Folder {APP_NAME} sudah ada!{COLORS['RESET']}")
        choice = input(f"{COLORS['CYAN']}[?] Update/Clone ulang? (y/n): {COLORS['RESET']}")
        if choice.lower() != 'y':
            return True
    
    print(f"{COLORS['CYAN']}[+] Mengclone repository...{COLORS['RESET']}")
    print(f"{COLORS['DIM']}   {GITHUB_REPO}{COLORS['RESET']}")
    
    loading_animation("Cloning repository", 3)
    
    try:
        # Hapus jika ada
        if os.path.exists(APP_NAME):
            shutil.rmtree(APP_NAME)
        
        # Clone
        subprocess.run(['git', 'clone', GITHUB_REPO], check=True)
        
        print(f"{COLORS['GREEN']}✅ Repository berhasil di-clone!{COLORS['RESET']}")
        print(f"{COLORS['CYAN']}📁 Lokasi: {os.getcwd()}/{APP_NAME}{COLORS['RESET']}")
        return True
    except Exception as e:
        print(f"{COLORS['RED']}❌ Gagal clone: {e}{COLORS['RESET']}")
        return False

# ================ FIND FILE ================

def find_file():
    """Cari file untuk di-deobfuscate"""
    print(f"\n{COLORS['BOLD']}{COLORS['PURPLE']}╔═══════════════════════════════════════╗")
    print(f"║     🔍 FIND FILE                  ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
    
    # Pilihan pencarian
    print(f"{COLORS['CYAN']}📌 Pilih metode pencarian:{COLORS['RESET']}")
    print(f"  {COLORS['GREEN']}1.{COLORS['RESET']} Cari di Internal Storage (/sdcard)")
    print(f"  {COLORS['BLUE']}2.{COLORS['RESET']} Cari di Folder Saat Ini")
    print(f"  {COLORS['YELLOW']}3.{COLORS['RESET']} Input Manual Path")
    print(f"  {COLORS['PURPLE']}4.{COLORS['RESET']} Scan Semua File .py")
    
    choice = input(f"\n{COLORS['YELLOW']}[>] Pilih (1-4): {COLORS['RESET']}")
    
    found_files = []
    
    if choice == '1':
        # Cari di internal storage
        print(f"\n{COLORS['CYAN']}[+] Mencari di Internal Storage...{COLORS['RESET']}")
        search_dir = INTERNAL_BASE
        loading_animation("Scanning files", 2)
        
        for root, dirs, files in os.walk(search_dir):
            for file in files:
                if file.endswith('.py') and 'encrypt' in file.lower():
                    found_files.append(os.path.join(root, file))
            if len(found_files) >= 10:
                break
    
    elif choice == '2':
        # Cari di folder saat ini
        print(f"\n{COLORS['CYAN']}[+] Mencari di folder saat ini...{COLORS['RESET']}")
        for file in os.listdir('.'):
            if file.endswith('.py'):
                found_files.append(file)
    
    elif choice == '3':
        # Manual input
        filepath = input(f"\n{COLORS['YELLOW']}[>] Masukkan path file: {COLORS['RESET']}")
        if os.path.exists(filepath):
            found_files = [filepath]
        else:
            print(f"{COLORS['RED']}❌ File tidak ditemukan!{COLORS['RESET']}")
            return None
    
    elif choice == '4':
        # Scan semua .py
        print(f"\n{COLORS['CYAN']}[+] Scanning semua file .py...{COLORS['RESET']}")
        loading_animation("Scanning", 3)
        
        # Cari di internal
        if os.path.exists(INTERNAL_BASE):
            for root, dirs, files in os.walk(INTERNAL_BASE):
                for file in files:
                    if file.endswith('.py'):
                        found_files.append(os.path.join(root, file))
                    if len(found_files) >= 20:
                        break
                if len(found_files) >= 20:
                    break
        
        # Cari di local
        for file in os.listdir('.'):
            if file.endswith('.py') and file not in found_files:
                found_files.append(file)
    
    if not found_files:
        print(f"{COLORS['RED']}❌ Tidak ada file ditemukan!{COLORS['RESET']}")
        return None
    
    # Tampilkan hasil
    print(f"\n{COLORS['GREEN']}✅ Ditemukan {len(found_files)} file:{COLORS['RESET']}")
    for i, file in enumerate(found_files[:15], 1):
        size = os.path.getsize(file) if os.path.exists(file) else 0
        size_kb = size / 1024
        print(f"  {COLORS['CYAN']}{i}.{COLORS['RESET']} {os.path.basename(file)} {COLORS['DIM']}({size_kb:.1f} KB){COLORS['RESET']}")
        print(f"     {COLORS['DIM']}{file}{COLORS['RESET']}")
    
    if len(found_files) > 15:
        print(f"  {COLORS['DIM']}... dan {len(found_files)-15} file lainnya{COLORS['RESET']}")
    
    # Pilih file
    if len(found_files) == 1:
        print(f"\n{COLORS['GREEN']}✅ Memilih: {found_files[0]}{COLORS['RESET']}")
        return found_files[0]
    
    while True:
        try:
            choice = input(f"\n{COLORS['YELLOW']}[>] Pilih nomor file (0 untuk batal): {COLORS['RESET']}")
            if choice == '0':
                return None
            idx = int(choice) - 1
            if 0 <= idx < len(found_files):
                selected = found_files[idx]
                print(f"{COLORS['GREEN']}✅ Memilih: {selected}{COLORS['RESET']}")
                return selected
            else:
                print(f"{COLORS['RED']}❌ Pilihan tidak valid!{COLORS['RESET']}")
        except:
            print(f"{COLORS['RED']}❌ Input tidak valid!{COLORS['RESET']}")

# ================ DEOBFUSCATE ENGINE ================

class DeobfuscateEngine:
    """Engine untuk deobfuscate PyEncrypter"""
    
    @staticmethod
    def extract_encrypted_data(content):
        """Extract encrypted data"""
        patterns = [
            r"_1nf3r10r_\s*=\s*lambda.*?b'([^']+)'",
            r"exec\s*\(\s*_1nf3r10r_\s*\(\s*b'([^']+)'\s*\)\s*\)",
            r"b'([A-Za-z0-9!#$%&()*+,-./:;<=>?@[\]^_`{|}~]+)'"
        ]
        for pattern in patterns:
            match = re.search(pattern, content, re.DOTALL)
            if match:
                return match.group(1)
        return None
    
    @staticmethod
    def decode_pyencrypter(encrypted_data):
        """Decode PyEncrypter"""
        try:
            reversed_data = encrypted_data[::-1]
            b85_decoded = base64.b85decode(reversed_data)
            decompressed = zlib.decompress(b85_decoded)
            code = marshal.loads(decompressed)
            return code
        except Exception as e:
            return None
    
    @staticmethod
    def extract_source(code_object):
        """Extract source code"""
        try:
            import inspect
            return inspect.getsource(code_object)
        except:
            try:
                import dis
                import io
                output = io.StringIO()
                dis.dis(code_object, file=output)
                return output.getvalue()
            except:
                return str(code_object)
    
    @staticmethod
    def deobfuscate_file(filepath):
        """Full deobfuscate process"""
        results = {
            'success': False,
            'file': filepath,
            'source': None,
            'error': None,
            'layers': []
        }
        
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            results['layers'].append({
                'name': 'Original File',
                'size': len(content)
            })
            
            encrypted = DeobfuscateEngine.extract_encrypted_data(content)
            if not encrypted:
                results['error'] = "Tidak ditemukan data terenkripsi"
                return results
            
            results['layers'].append({
                'name': 'Encrypted Data',
                'size': len(encrypted)
            })
            
            code = DeobfuscateEngine.decode_pyencrypter(encrypted)
            if not code:
                results['error'] = "Gagal mendekripsi"
                return results
            
            results['layers'].append({
                'name': 'Decoded Code Object'
            })
            
            source = DeobfuscateEngine.extract_source(code)
            if source:
                results['source'] = source
                results['layers'].append({
                    'name': 'Final Source Code',
                    'size': len(source)
                })
            
            results['success'] = True
            
        except Exception as e:
            results['error'] = str(e)
        
        return results

# ================ SAVE RESULT ================

def save_result(source, filename, original_path):
    """Save hasil deobfuscate ke internal storage"""
    print(f"\n{COLORS['BOLD']}{COLORS['GREEN']}╔═══════════════════════════════════════╗")
    print(f"║     💾 SAVE TO INTERNAL           ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
    
    # Generate nama file
    base_name = os.path.splitext(os.path.basename(original_path))[0]
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    save_name = f"{base_name}_deobfuscated_{timestamp}.py"
    
    # Path internal
    internal_path = f"{DECODED_DIR}/{save_name}"
    
    print(f"{COLORS['CYAN']}[+] Menyimpan file...{COLORS['RESET']}")
    loading_animation(f"Saving to {DECODED_DIR}", 1)
    
    try:
        # Simpan ke internal
        with open(internal_path, 'w', encoding='utf-8') as f:
            f.write(source)
        
        # Copy ke local backup
        os.makedirs('saved', exist_ok=True)
        local_path = f"saved/{save_name}"
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(source)
        
        print(f"\n{COLORS['GREEN']}✅ File berhasil disimpan!{COLORS['RESET']}")
        print(f"\n{COLORS['CYAN']}╔═══════════════════════════════════════════════════════════╗")
        print(f"║  📂 LOKASI FILE                                                ║")
        print(f"╠═══════════════════════════════════════════════════════════════╣")
        print(f"║  {COLORS['GREEN']}Internal Storage:{COLORS['RESET']}                                               ║")
        print(f"║  {COLORS['YELLOW']}{internal_path}{COLORS['RESET']}")
        print(f"║                                                                   ║")
        print(f"║  {COLORS['BLUE']}Local Backup:{COLORS['RESET']}                                                  ║")
        print(f"║  {COLORS['DIM']}{local_path}{COLORS['RESET']}")
        print(f"╚═══════════════════════════════════════════════════════════════╝{COLORS['RESET']}")
        
        # Info akses
        print(f"\n{COLORS['YELLOW']}📌 Cara Mengakses File:{COLORS['RESET']}")
        print(f"  {COLORS['GREEN']}1.{COLORS['RESET']} Termux: cd {DECODED_DIR}")
        print(f"  {COLORS['GREEN']}2.{COLORS['RESET']} File Manager: Internal Storage > Deobfuscate > Decoded")
        print(f"  {COLORS['GREEN']}3.{COLORS['RESET']} Buka Langsung: termux-open {internal_path}")
        
        return internal_path
    except Exception as e:
        print(f"{COLORS['RED']}❌ Gagal menyimpan: {e}{COLORS['RESET']}")
        return None

# ================ DISPLAY RESULT ================

def display_result(results):
    """Tampilkan hasil deobfuscate dengan keren"""
    print(f"\n{COLORS['BOLD']}{COLORS['PURPLE']}╔═══════════════════════════════════════╗")
    print(f"║     🔓 DEOBFUSCATE RESULT          ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
    
    if not results['success']:
        print(f"{COLORS['RED']}❌ Gagal: {results.get('error', 'Unknown error')}{COLORS['RESET']}")
        return
    
    print(f"{COLORS['GREEN']}✅ Berhasil dideobfuscate!{COLORS['RESET']}")
    print(f"\n{COLORS['CYAN']}📊 Detail:{COLORS['RESET']}")
    print(f"  📁 File: {results['file']}")
    print(f"  📏 Source Size: {len(results['source'])} characters")
    print(f"  🔢 Layers: {len(results['layers'])}")
    
    # Tampilkan layers
    print(f"\n{COLORS['CYAN']}📊 Layers:{COLORS['RESET']}")
    for i, layer in enumerate(results['layers'], 1):
        size_info = f" ({layer['size']} chars)" if 'size' in layer else ""
        print(f"  {COLORS['YELLOW']}{i}.{COLORS['RESET']} {layer['name']}{size_info}")
    
    # Tampilkan preview source
    if results['source']:
        print(f"\n{COLORS['CYAN']}📝 Preview Source Code:{COLORS['RESET']}")
        print(f"{COLORS['DIM']}┌─" + "─" * 58 + "┐")
        lines = results['source'].split('\n')
        for line in lines[:15]:
            print(f"│ {line[:56]}")
        if len(lines) > 15:
            print(f"│ {COLORS['DIM']}[...] {len(lines)-15} lines more{COLORS['RESET']}")
        print(f"{COLORS['DIM']}└─" + "─" * 58 + "┘")

# ================ OPEN FILE ================

def open_file(filepath):
    """Buka file dengan termux-open"""
    if os.path.exists('/data/data/com.termux'):
        try:
            print(f"\n{COLORS['CYAN']}[+] Membuka file...{COLORS['RESET']}")
            subprocess.run(['termux-open', filepath])
            print(f"{COLORS['GREEN']}✅ File dibuka!{COLORS['RESET']}")
        except:
            print(f"{COLORS['YELLOW']}📂 File: {filepath}{COLORS['RESET']}")

# ================ MAIN MENU ================

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    clear_screen()
    print(BANNER)
    print(f"{COLORS['DIM']}╔═══════════════════════════════════════════════════════════════╗")
    print(f"║  {COLORS['GREEN']}📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{' ' * 36}{COLORS['DIM']}║")
    print(f"║  {COLORS['CYAN']}🔓 Mode: All-in-One Deobfuscate{' ' * 22}{COLORS['DIM']}║")
    print(f"║  {COLORS['YELLOW']}📂 Save: {DECODED_DIR}{COLORS['DIM']} ║")
    print(f"╚═══════════════════════════════════════════════════════════════╝{COLORS['RESET']}")
    print()

def main():
    """Main program with full flow"""
    print_header()
    
    # ===== STEP 1: SETUP STORAGE =====
    print(f"\n{COLORS['BOLD']}{COLORS['WHITE']}╔═══════════════════════════════════════╗")
    print(f"║  📌 STEP 1: SETUP STORAGE        ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}")
    
    if not setup_storage():
        print(f"{COLORS['RED']}❌ Storage gagal di-setup!{COLORS['RESET']}")
        input("\nTekan Enter untuk keluar...")
        sys.exit(1)
    
    input(f"\n{COLORS['CYAN']}Tekan Enter untuk lanjut ke Step 2...{COLORS['RESET']}")
    
    # ===== STEP 2: CLONE REPOSITORY =====
    print_header()
    print(f"\n{COLORS['BOLD']}{COLORS['WHITE']}╔═══════════════════════════════════════╗")
    print(f"║  📌 STEP 2: CLONE REPOSITORY     ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}")
    
    if not clone_repository():
        print(f"{COLORS['RED']}❌ Gagal clone repository!{COLORS['RESET']}")
        choice = input(f"{COLORS['YELLOW']}[?] Lanjutkan tanpa clone? (y/n): {COLORS['RESET']}")
        if choice.lower() != 'y':
            sys.exit(1)
    
    input(f"\n{COLORS['CYAN']}Tekan Enter untuk lanjut ke Step 3...{COLORS['RESET']}")
    
    # ===== STEP 3: FIND FILE =====
    print_header()
    print(f"\n{COLORS['BOLD']}{COLORS['WHITE']}╔═══════════════════════════════════════╗")
    print(f"║  📌 STEP 3: FIND FILE            ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}")
    
    file_path = find_file()
    if not file_path:
        print(f"{COLORS['RED']}❌ Tidak ada file dipilih!{COLORS['RESET']}")
        sys.exit(1)
    
    input(f"\n{COLORS['CYAN']}Tekan Enter untuk lanjut ke Step 4...{COLORS['RESET']}")
    
    # ===== STEP 4: DEOBFUSCATE =====
    print_header()
    print(f"\n{COLORS['BOLD']}{COLORS['WHITE']}╔═══════════════════════════════════════╗")
    print(f"║  📌 STEP 4: DEOBFUSCATE          ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}")
    
    print(f"\n{COLORS['CYAN']}[+] Memproses file: {file_path}{COLORS['RESET']}")
    loading_animation("Deobfuscating", 3)
    
    results = DeobfuscateEngine.deobfuscate_file(file_path)
    display_result(results)
    
    if not results['success'] or not results['source']:
        print(f"{COLORS['RED']}❌ Gagal deobfuscate!{COLORS['RESET']}")
        sys.exit(1)
    
    input(f"\n{COLORS['CYAN']}Tekan Enter untuk lanjut ke Step 5...{COLORS['RESET']}")
    
    # ===== STEP 5: SAVE TO INTERNAL =====
    print_header()
    print(f"\n{COLORS['BOLD']}{COLORS['WHITE']}╔═══════════════════════════════════════╗")
    print(f"║  📌 STEP 5: SAVE TO INTERNAL     ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}")
    
    saved_path = save_result(results['source'], results['file'], results['file'])
    
    if saved_path:
        print(f"\n{COLORS['GREEN']}✅ Selesai! File tersimpan di Internal Storage!{COLORS['RESET']}")
        
        # Tanya buka file
        open_choice = input(f"\n{COLORS['CYAN']}[?] Buka file sekarang? (y/n): {COLORS['RESET']}")
        if open_choice.lower() == 'y':
            open_file(saved_path)
    
    print(f"\n{COLORS['GREEN']}╔═══════════════════════════════════════════════════════════╗")
    print(f"║  🎉 PROSES SELESAI!                                             ║")
    print(f"║                                                                   ║")
    print(f"║  📂 Hasil Deobfuscate:                                            ║")
    print(f"║  {COLORS['YELLOW']}{saved_path}{COLORS['RESET']}")
    print(f"║                                                                   ║")
    print(f"║  📌 Lokasi:                                                       ║")
    print(f"║  {COLORS['CYAN']}Internal Storage > Deobfuscate > Decoded{COLORS['RESET']}          ║")
    print(f"╚═══════════════════════════════════════════════════════════════╝{COLORS['RESET']}")
    
    input(f"\n{COLORS['CYAN']}Tekan Enter untuk kembali ke menu...{COLORS['RESET']}")

# ================ RUN ================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{COLORS['YELLOW']}[!] Interrupted by user{COLORS['RESET']}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{COLORS['RED']}❌ Error: {e}{COLORS['RESET']}")
        sys.exit(1)
