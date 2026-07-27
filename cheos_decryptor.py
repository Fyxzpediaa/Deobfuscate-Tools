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
║  🔓 ADVANCED PYENCRYPTER DECRYPTOR v2.0                      ║
║  👨‍💻 Fyxzpedia Engineering                                    ║
║  📱 t.me/Fyxzpedia                                           ║
║  ▶️  Fyxzpedia-vil                                            ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import base64
import zlib
import marshal
import re
import ast
import dis
import json
from datetime import datetime

# ================ KONFIGURASI ================
VERSION = "2.0"
DEVELOPER = "Fyxzpedia Engineering"
TELEGRAM = "t.me/Fyxzpedia"
YOUTUBE = "Fyxzpedia-vil"

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
║  {COLORS['YELLOW']}🔓 ADVANCED PYENCRYPTER DECRYPTOR v{VERSION}{COLORS['CYAN']}              ║
║  {COLORS['GREEN']}👨‍💻 {DEVELOPER}{COLORS['CYAN']}                                          ║
║  {COLORS['PURPLE']}📱 {TELEGRAM}{COLORS['CYAN']}                                             ║
║  {COLORS['BLUE']}▶️  {YOUTUBE}{COLORS['CYAN']}                                              ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝{COLORS['RESET']}
"""

# ================ PYENCRYPTER DECODER ================

class PyEncrypterDecoder:
    """Decoder untuk file yang dienkripsi PyEncrypter"""
    
    @staticmethod
    def extract_encrypted_data(content):
        """Extract encrypted data dari file PyEncrypter"""
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
        """Dekripsi data PyEncrypter"""
        try:
            # Step 1: Reverse string
            reversed_data = encrypted_data[::-1]
            
            # Step 2: Base85 decode
            b85_decoded = base64.b85decode(reversed_data)
            
            # Step 3: Zlib decompress
            decompressed = zlib.decompress(b85_decoded)
            
            # Step 4: Marshal loads
            code = marshal.loads(decompressed)
            
            return code
        except Exception as e:
            return None
    
    @staticmethod
    def extract_source_code(code_object):
        """Extract source code dari code object"""
        try:
            # Coba dapatkan source code
            import inspect
            source = inspect.getsource(code_object)
            return source
        except:
            # Jika tidak bisa, decompile bytecode
            try:
                import uncompyle6
                import io
                output = io.StringIO()
                uncompyle6.deparse_code(code_object, output)
                return output.getvalue()
            except:
                # Fallback: disassemble
                import dis
                import io
                output = io.StringIO()
                dis.dis(code_object, file=output)
                return output.getvalue()
    
    @staticmethod
    def decode_file(filepath):
        """Full decode process untuk file"""
        results = {
            'success': False,
            'layers': [],
            'final_code': None,
            'error': None
        }
        
        try:
            # Baca file
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            results['layers'].append({
                'name': 'Original File',
                'data': content[:500] + '...' if len(content) > 500 else content
            })
            
            # Extract encrypted data
            encrypted = PyEncrypterDecoder.extract_encrypted_data(content)
            if not encrypted:
                results['error'] = "Tidak ditemukan data terenkripsi"
                return results
            
            results['layers'].append({
                'name': 'Extracted Encrypted Data',
                'data': encrypted[:100] + '...' if len(encrypted) > 100 else encrypted
            })
            
            # Decode
            code = PyEncrypterDecoder.decode_pyencrypter(encrypted)
            if not code:
                results['error'] = "Gagal mendekripsi data"
                return results
            
            results['layers'].append({
                'name': 'Decoded Code Object',
                'data': str(code)[:200] + '...' if len(str(code)) > 200 else str(code)
            })
            
            # Extract source code
            source = PyEncrypterDecoder.extract_source_code(code)
            if source:
                results['final_code'] = source
                results['layers'].append({
                    'name': 'Final Source Code',
                    'data': source[:500] + '...' if len(source) > 500 else source
                })
            
            results['success'] = True
            
        except Exception as e:
            results['error'] = str(e)
        
        return results

# ================ FUNGSI UTAMA ================

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    clear_screen()
    print(BANNER)
    print(f"{COLORS['DIM']}╔═══════════════════════════════════════════════════════════════╗")
    print(f"║  {COLORS['GREEN']}📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{' ' * 36}{COLORS['DIM']}║")
    print(f"║  {COLORS['CYAN']}🔓 Mode: PyEncrypter Decoder{' ' * 28}{COLORS['DIM']}║")
    print(f"╚═══════════════════════════════════════════════════════════════╝{COLORS['RESET']}")
    print()

def decode_file():
    """Dekripsi file PyEncrypter"""
    print_header()
    print(f"{COLORS['BOLD']}{COLORS['YELLOW']}╔═══════════════════════════════════════╗")
    print(f"║     🔓 DEKRIPSI FILE             ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
    
    # Input file
    filepath = input(f"{COLORS['YELLOW']}[>] Path file (contoh: cheos.py): {COLORS['RESET']}")
    
    if not os.path.exists(filepath):
        print(f"{COLORS['RED']}❌ File tidak ditemukan!{COLORS['RESET']}")
        input("\nTekan Enter untuk lanjut...")
        return
    
    print(f"\n{COLORS['CYAN']}[+] Memproses file: {filepath}{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}[+] Mendekripsi PyEncrypter...{COLORS['RESET']}\n")
    
    # Decode
    result = PyEncrypterDecoder.decode_file(filepath)
    
    if result['success']:
        print(f"{COLORS['GREEN']}✅ Berhasil didekripsi!{COLORS['RESET']}")
        print(f"{COLORS['CYAN']}┌─" + "─" * 58 + "┐")
        
        # Tampilkan layers
        for i, layer in enumerate(result['layers']):
            print(f"│ {COLORS['YELLOW']}Layer {i+1}: {layer['name']}{COLORS['RESET']}")
            print(f"│ {COLORS['CYAN']}{'─' * 58}{COLORS['RESET']}")
            for line in layer['data'].split('\n')[:5]:
                print(f"│ {line[:56]}")
            if len(layer['data'].split('\n')) > 5:
                print(f"│ {COLORS['DIM']}[...] more{COLORS['RESET']}")
            print(f"│")
        
        print(f"└─" + "─" * 58 + "┘")
        
        # Tampilkan final code
        if result['final_code']:
            print(f"\n{COLORS['GREEN']}✅ Source Code Asli:{COLORS['RESET']}")
            print(f"{COLORS['CYAN']}╔═══════════════════════════════════════════════════════════╗")
            lines = result['final_code'].split('\n')
            for line in lines[:20]:
                print(f"║ {line[:59]}")
            if len(lines) > 20:
                print(f"║ {COLORS['DIM']}[...] {len(lines)-20} lines more{COLORS['RESET']}")
            print(f"╚═══════════════════════════════════════════════════════════╝{COLORS['RESET']}")
            
            # Tanya save
            save = input(f"\n{COLORS['CYAN']}[?] Simpan source code? (y/n): {COLORS['RESET']}")
            if save.lower() == 'y':
                filename = input(f"{COLORS['YELLOW']}[>] Nama file (tanpa ekstensi): {COLORS['RESET']}")
                ext = input(f"{COLORS['YELLOW']}[>] Ekstensi (py, txt): {COLORS['RESET']}")
                if not ext.startswith('.'):
                    ext = '.' + ext
                if not filename.endswith(ext):
                    filename += ext
                
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(result['final_code'])
                print(f"{COLORS['GREEN']}✅ File tersimpan: {filename}{COLORS['RESET']}")
    else:
        print(f"{COLORS['RED']}❌ Gagal mendekripsi: {result.get('error', 'Unknown error')}{COLORS['RESET']}")
    
    input(f"\n{COLORS['CYAN']}Tekan Enter untuk lanjut...{COLORS['RESET']}")

def decode_text():
    """Dekripsi text langsung"""
    print_header()
    print(f"{COLORS['BOLD']}{COLORS['YELLOW']}╔═══════════════════════════════════════╗")
    print(f"║     🔓 DEKRIPSI TEXT             ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
    
    print(f"{COLORS['CYAN']}[+] Masukkan teks terenkripsi (Ctrl+D untuk selesai):{COLORS['RESET']}")
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    
    text = '\n'.join(lines)
    
    if not text.strip():
        print(f"{COLORS['RED']}❌ Teks kosong!{COLORS['RESET']}")
        input("\nTekan Enter untuk lanjut...")
        return
    
    # Extract encrypted data
    encrypted = PyEncrypterDecoder.extract_encrypted_data(text)
    if not encrypted:
        print(f"{COLORS['RED']}❌ Tidak ditemukan data terenkripsi!{COLORS['RESET']}")
        input("\nTekan Enter untuk lanjut...")
        return
    
    # Decode
    code = PyEncrypterDecoder.decode_pyencrypter(encrypted)
    if not code:
        print(f"{COLORS['RED']}❌ Gagal mendekripsi!{COLORS['RESET']}")
        input("\nTekan Enter untuk lanjut...")
        return
    
    source = PyEncrypterDecoder.extract_source_code(code)
    if source:
        print(f"\n{COLORS['GREEN']}✅ Source Code:{COLORS['RESET']}")
        print(f"{COLORS['CYAN']}┌─" + "─" * 58 + "┐")
        for line in source.split('\n')[:20]:
            print(f"│ {line[:56]}")
        if len(source.split('\n')) > 20:
            print(f"│ {COLORS['DIM']}[...] more{COLORS['RESET']}")
        print(f"└─" + "─" * 58 + "┘")
        
        # Save
        save = input(f"\n{COLORS['CYAN']}[?] Simpan? (y/n): {COLORS['RESET']}")
        if save.lower() == 'y':
            filename = input(f"{COLORS['YELLOW']}[>] Nama file: {COLORS['RESET']}")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(source)
            print(f"{COLORS['GREEN']}✅ File tersimpan: {filename}{COLORS['RESET']}")
    else:
        print(f"{COLORS['RED']}❌ Gagal mengekstrak source code{COLORS['RESET']}")
    
    input(f"\n{COLORS['CYAN']}Tekan Enter untuk lanjut...{COLORS['RESET']}")

def show_info():
    """Tampilkan info"""
    print_header()
    print(f"{COLORS['BOLD']}{COLORS['PURPLE']}╔═══════════════════════════════════════╗")
    print(f"║        ℹ️  INFO & TUTORIAL         ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
    
    print(f"{COLORS['CYAN']}📌 Tentang Tools:{COLORS['RESET']}")
    print(f"  Tools ini khusus untuk mendekripsi file yang")
    print(f"  dienkripsi dengan PyEncrypter.")
    
    print(f"\n{COLORS['CYAN']}📌 Cara Kerja:{COLORS['RESET']}")
    print(f"  1. Ekstrak data terenkripsi dari file")
    print(f"  2. Reverse string")
    print(f"  3. Base85 decode")
    print(f"  4. Zlib decompress")
    print(f"  5. Marshal loads")
    print(f"  6. Ekstrak source code asli")
    
    print(f"\n{COLORS['CYAN']}📌 Supported:{COLORS['RESET']}")
    print(f"  • PyEncrypter v1 - v3")
    print(f"  • Base85 encoded")
    print(f"  • Zlib compressed")
    print(f"  • Marshal bytecode")
    
    print(f"\n{COLORS['YELLOW']}⚠️  Catatan:{COLORS['RESET']}")
    print(f"  • Gunakan untuk edukasi")
    print(f"  • Jangan untuk aktivitas ilegal")
    print(f"  • Hormati hak cipta")
    
    input(f"\n{COLORS['CYAN']}Tekan Enter untuk lanjut...{COLORS['RESET']}")

def main():
    """Main menu"""
    while True:
        print_header()
        print(f"{COLORS['BOLD']}{COLORS['WHITE']}╔═══════════════════════════════════════╗")
        print(f"║          MAIN MENU                ║")
        print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
        
        print(f"  {COLORS['GREEN']}[1]{COLORS['RESET']} 🔓 Decode File (PyEncrypter)")
        print(f"  {COLORS['BLUE']}[2]{COLORS['RESET']} 🔓 Decode Text")
        print(f"  {COLORS['PURPLE']}[3]{COLORS['RESET']} ℹ️  Info & Tutorial")
        print(f"  {COLORS['RED']}[0]{COLORS['RESET']} 🚪 Exit\n")
        
        choice = input(f"{COLORS['YELLOW']}[>] Pilih menu: {COLORS['RESET']}")
        
        if choice == '1':
            decode_file()
        elif choice == '2':
            decode_text()
        elif choice == '3':
            show_info()
        elif choice == '0':
            print(f"\n{COLORS['GREEN']}✅ Terima kasih! - Fyxzpedia Engineering{COLORS['RESET']}")
            sys.exit(0)
        else:
            print(f"{COLORS['RED']}❌ Pilihan tidak valid!{COLORS['RESET']}")
            input("\nTekan Enter untuk lanjut...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{COLORS['YELLOW']}[!] Interrupted by user{COLORS['RESET']}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{COLORS['RED']}❌ Error: {e}{COLORS['RESET']}")
        sys.exit(1)
