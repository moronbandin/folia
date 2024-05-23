import os
import shutil

# Ruta base de los archivos markdown
base_dir = 'docs/pezas'

# Categorías originales y sus archivos correspondientes
categories = {
    "cantos": ["axudaime.md"],
    "dansas": ["pereiras.md"],
    "foliadas": ["route.md", "zanfoga.md"],
    "maneos": ["abelenda.md", "agoraque.md", "cabaleiros.md", "caion.md", "imende.md", "rosinha.md", "silvan.md"],
    "muinheiras": ["esgos.md", "golpes.md", "lerole.md", "maronda.md", "m_linhares.md", "sansalvador.md", "zaragoza.md"],
    "rumbas": ["montealegre.md", "rumba.md"],
    "valses": ["alumeame.md"],
    "xotas": ["bazar.md", "caroi.md", "carolina.md", "ferrinhas.md", "linhares.md"]
}

# Crear carpetas de categorías si no existen y mover los archivos correspondientes
for category, files in categories.items():
    category_path = os.path.join(base_dir, category)
    os.makedirs(category_path, exist_ok=True)
    for file in files:
        src_path = os.path.join(base_dir, os.path.splitext(file)[0], file)
        dest_path = os.path.join(category_path, file)
        if os.path.exists(src_path):
            shutil.move(src_path, dest_path)

# Función para limpiar las líneas que contienen '[Descargar PDF]' en un archivo .md
def clean_md_file(md_path):
    with open(md_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open(md_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if '[Descargar PDF]' not in line:
                file.write(line)

# Limpiar los archivos .md de los botones de descarga y eliminar carpetas vacías
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.md'):
            md_path = os.path.join(root, file)
            clean_md_file(md_path)
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        try:
            os.rmdir(dir_path)
        except OSError:
            pass

print('Estructura revertida, archivos .md limpiados y carpetas innecesarias eliminadas.')
