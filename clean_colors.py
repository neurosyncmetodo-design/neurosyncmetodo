import os
import re

target_dir = r"C:\Users\dimitri\Documents\HIPNOSIS\web"
html_files = [f for f in os.listdir(target_dir) if f.endswith('.html')]

replacements = [
    # Fondos (sólo reemplazar clases enteras)
    (r'\bbg-white(?:/[0-9]+)?\b', 'glass-panel '),
    (r'\bbg-gray-[0-9]{2,3}(?:/[0-9]+)?\b', 'bg-transparent '),
    (r'\bbg-blue-[0-9]{2,3}(?:/[0-9]+)?\b', 'glass-panel '),
    (r'\bfrom-white\b', 'from-transparent '),
    (r'\bvia-gray-[0-9]+\b', 'via-transparent '),
    (r'\bto-white\b', 'to-transparent '),
    
    # Textos
    (r'\btext-gray-[5-9]00\b', 'text-[#E0E0E0] '),
    (r'\btext-black\b', 'text-[#E0E0E0] '),
    
    # Bordes
    (r'\bborder-gray-[0-9]{2,3}(?:/[0-9]+)?\b', 'border-white/5 '),
    (r'\bborder-blue-[0-9]{2,3}(?:/[0-9]+)?\b', 'border-white/5 '),
    
    # Sombras
    (r'\bshadow-lg\b', 'shadow-[0_10px_30px_rgba(0,0,0,0.5)] '),
    (r'\bshadow-2xl\b', 'shadow-[0_20px_50px_rgba(0,0,0,0.5)] '),
    
    # Remover dark mode prefix, as we are permanently dark
    (r'\bdark:[a-zA-Z0-9\-\/]+\b', '')
]

for file_name in html_files:
    file_path = os.path.join(target_dir, file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for pattern, new_str in replacements:
        content = re.sub(pattern, new_str, content)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML limpiado y convertido a Obsidian Elite en", len(html_files), "archivos.")
