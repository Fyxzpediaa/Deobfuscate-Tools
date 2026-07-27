#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║  ██████╗ ██████╗  ██████╗ ████████╗███████╗ ██████╗████████╗ ║
║  ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝ ║
║  ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║        ██║    ║
║  ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══╝  ██║        ██║    ║
║  ██║     ██║  ██║╚██████╔╝   ██║   ███████╗╚██████╗   ██║    ║
║  ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝   ╚═╝    ║
║                                                               ║
║  🔐 SOURCE PROTECTOR v1.0 - Zero-Width Encryption            ║
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
import hashlib
import random
import json
from datetime import datetime

# ================ ZERO-WIDTH ENGINE ================

class ZeroWidthEngine:
    """Zero-Width Encryption Engine untuk proteksi source code"""
    
    # Zero-Width Characters
    ZW = {
        '0': '\u200b',      # Zero Width Space
        '1': '\u200c',       # Zero Width Non-Joiner
        'sep': '\u200d',     # Zero Width Joiner
        'mark': '\u2060',    # Word Joiner
        'start': '\uFEFF',   # Zero Width No-Break Space
        'end': '\u200e',     # Left-to-Right Mark
    }
    
    @staticmethod
    def text_to_binary(text):
        """Convert text to binary"""
        return ''.join(format(ord(c), '08b') for c in text)
    
    @staticmethod
    def binary_to_text(binary):
        """Convert binary to text"""
        text = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                text += chr(int(byte, 2))
        return text
    
    @staticmethod
    def encrypt(text, secret, key=None):
        """Encrypt text with zero-width and optional key"""
        # Add key if provided
        if key:
            secret = f"KEY:{key}|DATA:{secret}"
        
        # Convert secret to binary
        binary = ZeroWidthEngine.text_to_binary(secret)
        
        # Convert to zero-width
        zw = ''
        for bit in binary:
            zw += ZeroWidthEngine.ZW['0'] if bit == '0' else ZeroWidthEngine.ZW['1']
        
        # Add markers
        zw = ZeroWidthEngine.ZW['start'] + zw + ZeroWidthEngine.ZW['end']
        
        # Insert at random position
        pos = random.randint(0, len(text))
        return text[:pos] + zw + text[pos:]
    
    @staticmethod
    def decrypt(text):
        """Decrypt zero-width hidden data"""
        # Find zero-width chars
        zw_chars = ''.join([ZeroWidthEngine.ZW['0'], ZeroWidthEngine.ZW['1'],
                           ZeroWidthEngine.ZW['start'], ZeroWidthEngine.ZW['end']])
        
        zw_text = ''.join(c for c in text if c in zw_chars)
        
        # Remove markers
        zw_text = zw_text.replace(ZeroWidthEngine.ZW['start'], '')
        zw_text = zw_text.replace(ZeroWidthEngine.ZW['end'], '')
        
        if zw_text:
            binary = ''
            for char in zw_text:
                if char == ZeroWidthEngine.ZW['0']:
                    binary += '0'
                elif char == ZeroWidthEngine.ZW['1']:
                    binary += '1'
            
            return ZeroWidthEngine.binary_to_text(binary)
        return None

# ================ PROTECT SOURCE ================

def protect_source():
    """Protect source code dengan zero-width"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print(f"""
{COLORS['CYAN']}╔═══════════════════════════════════════════════════════════════╗
║                                                                   ║
║  ██████╗ ██████╗  ██████╗ ████████╗███████╗ ██████╗████████╗     ║
║  ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝     ║
║  ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║        ██║        ║
║  ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══╝  ██║        ██║        ║
║  ██║     ██║  ██║╚██████╔╝   ██║   ███████╗╚██████╗   ██║        ║
║  ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝   ╚═╝        ║
║                                                                   ║
║  {COLORS['YELLOW']}🔐 SOURCE PROTECTOR v1.0{COLORS['CYAN']}                                     ║
║  {COLORS['GREEN']}👨‍💻 Fyxzpedia Engineering{COLORS['CYAN']}                                    ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝{COLORS['RESET']}
""")
    
    print(f"\n{COLORS['BOLD']}{COLORS['YELLOW']}╔═══════════════════════════════════════╗")
    print(f"║     🔐 PROTECT SOURCE CODE        ║")
    print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
    
    # Pilih file
    print(f"{COLORS['CYAN']}📌 File yang akan diproteksi:{COLORS['RESET']}")
    print(f"  1. cheos_decryptor.py")
    print(f"  2. Input manual")
    
    choice = input(f"\n{COLORS['YELLOW']}[>] Pilih: {COLORS['RESET']}")
    
    if choice == '1':
        source_file = 'cheos_decryptor.py'
    else:
        source_file = input(f"{COLORS['YELLOW']}[>] Path file: {COLORS['RESET']}")
    
    if not os.path.exists(source_file):
        print(f"{COLORS['RED']}❌ File tidak ditemukan!{COLORS['RESET']}")
        input("\nTekan Enter untuk lanjut...")
        return
    
    # Baca source
    with open(source_file, 'r', encoding='utf-8') as f:
        source = f.read()
    
    print(f"\n{COLORS['GREEN']}✅ Source loaded: {len(source)} characters{COLORS['RESET']}")
    
    # Generate key
    key = hashlib.sha256(f"{DEVELOPER}{datetime.now()}".encode()).hexdigest()[:16]
    
    # Pilih mode
    print(f"\n{COLORS['CYAN']}📌 Mode Proteksi:{COLORS['RESET']}")
    print(f"  {COLORS['GREEN']}1.{COLORS['RESET']} Light - Hidden Signature")
    print(f"  {COLORS['YELLOW']}2.{COLORS['RESET']} Medium - Signature + Checksum (Recommended)")
    print(f"  {COLORS['RED']}3.{COLORS['RESET']} Heavy - Multi-layer + Key Protection")
    
    mode = input(f"\n{COLORS['YELLOW']}[>] Pilih (1-3): {COLORS['RESET']}")
    
    # Prepare secret
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    signature = f"FYXZPEDIA_{timestamp}"
    checksum = hashlib.sha256(source.encode()).hexdigest()
    
    if mode == '1':
        secret = f"SIG:{signature}"
        layers = 1
    elif mode == '2':
        secret = f"SIG:{signature}|CHK:{checksum[:16]}"
        layers = 2
    elif mode == '3':
        # Compress + encrypt
        compressed = zlib.compress(source.encode())
        compressed_b64 = base64.b64encode(compressed).decode()
        secret = f"ZIP:{compressed_b64}|KEY:{key}|CHK:{checksum}"
        layers = 3
    else:
        print(f"{COLORS['RED']}❌ Pilihan tidak valid!{COLORS['RESET']}")
        input("\nTekan Enter untuk lanjut...")
        return
    
    # Encrypt
    print(f"\n{COLORS['CYAN']}[+] Mengenkripsi dengan {layers} layer...{COLORS['RESET']}")
    
    encrypted = source
    for i in range(layers):
        encrypted = ZeroWidthEngine.encrypt(encrypted, secret, key if mode == '3' else None)
    
    # Add protection header
    header = f'''# -*- coding: utf-8 -*-
"""
🔒 PROTECTED SOURCE CODE
👨‍💻 {DEVELOPER}
📱 {TELEGRAM}
🔑 Protected: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🔐 Mode: {['Light', 'Medium', 'Heavy'][int(mode)-1]}
🔢 Layers: {layers}
⚠️  DO NOT MODIFY THIS FILE! Modification will break the code.
"""

'''
    
    # Add footer with integrity check
    footer = f'''
# ================ INTEGRITY CHECK ================
import hashlib
import sys

def _check_integrity():
    """Check if source has been modified"""
    try:
        with open(__file__, 'r', encoding='utf-8') as f:
            content = f.read()
        current_hash = hashlib.sha256(content.encode()).hexdigest()
        expected_hash = "{checksum}"
        if current_hash != expected_hash:
            print("\\033[91m⚠️  WARNING: Source code has been modified!\\033[0m")
            print("\\033[91m⚠️  This tool may not work correctly!\\033[0m")
            return False
        return True
    except:
        return False

# Auto-check on import
if not _check_integrity():
    print("\\033[91m❌ Integrity check failed! Exiting...\\033[0m")
    sys.exit(1)
# =================================================
'''
    
    # Combine
    protected = header + encrypted + footer
    
    # Save
    output_file = f'protected_{source_file}'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(protected)
    
    print(f"\n{COLORS['GREEN']}✅ Source berhasil diproteksi!{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}📁 File: {output_file}{COLORS['RESET']}")
    print(f"{COLORS['CYAN']}📊 Size: {len(protected)} characters{COLORS['RESET']}")
    print(f"{COLORS['GREEN']}🔒 Protected: Yes{COLORS['RESET']}")
    
    # Verification
    print(f"\n{COLORS['CYAN']}[+] Verifikasi...{COLORS['RESET']}")
    extracted = ZeroWidthEngine.decrypt(encrypted)
    if extracted:
        print(f"{COLORS['GREEN']}✅ Hidden data detected!{COLORS['RESET']}")
        print(f"{COLORS['DIM']}   {extracted[:100]}...{COLORS['RESET']}")
    else:
        print(f"{COLORS['RED']}❌ Verification failed!{COLORS['RESET']}")
    
    print(f"\n{COLORS['YELLOW']}📌 Cara menggunakan:{COLORS['RESET']}")
    print(f"  python {output_file}")
    
    input(f"\n{COLORS['CYAN']}Tekan Enter untuk lanjut...{COLORS['RESET']}")

def main():
    """Main menu"""
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(f"""
{COLORS['CYAN']}╔═══════════════════════════════════════════════════════════════╗
║                                                                   ║
║  ██████╗ ██████╗  ██████╗ ████████╗███████╗ ██████╗████████╗     ║
║  ██╔══██╗██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝     ║
║  ██████╔╝██████╔╝██║   ██║   ██║   █████╗  ██║        ██║        ║
║  ██╔═══╝ ██╔══██╗██║   ██║   ██║   ██╔══╝  ██║        ██║        ║
║  ██║     ██║  ██║╚██████╔╝   ██║   ███████╗╚██████╗   ██║        ║
║  ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝   ╚═╝        ║
║                                                                   ║
║  {COLORS['YELLOW']}🔐 SOURCE PROTECTOR v1.0{COLORS['CYAN']}                                     ║
║  {COLORS['GREEN']}👨‍💻 Fyxzpedia Engineering{COLORS['CYAN']}                                    ║
║  {COLORS['PURPLE']}📱 t.me/Fyxzpedia{COLORS['CYAN']}                                           ║
║  {COLORS['BLUE']}▶️  Fyxzpedia-vil{COLORS['CYAN']}                                            ║
║                                                                   ║
╚═══════════════════════════════════════════════════════════════════╝{COLORS['RESET']}
""")
        
        print(f"\n{COLORS['BOLD']}{COLORS['WHITE']}╔═══════════════════════════════════════╗")
        print(f"║          MAIN MENU                ║")
        print(f"╚═══════════════════════════════════════╝{COLORS['RESET']}\n")
        
        print(f"  {COLORS['GREEN']}[1]{COLORS['RESET']} 🔐 Protect Source Code")
        print(f"  {COLORS['BLUE']}[2]{COLORS['RESET']} 🔓 Verify Protected Source")
        print(f"  {COLORS['RED']}[0]{COLORS['RESET']} 🚪 Exit\n")
        
        choice = input(f"{COLORS['YELLOW']}[>] Pilih menu: {COLORS['RESET']}")
        
        if choice == '1':
            protect_source()
        elif choice == '2':
            print(f"\n{COLORS['YELLOW']}[!] Fitur verify segera hadir!{COLORS['RESET']}")
            input("\nTekan Enter untuk lanjut...")
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
