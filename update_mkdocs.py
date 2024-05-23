import os
import yaml

# Ruta del archivo mkdocs.yml
mkdocs_path = 'mkdocs.yml'

# Función para construir el diccionario de navegación
def build_nav(base_dir):
    nav = {}
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.md'):
                category = os.path.basename(root)
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, 'docs')
                page_title = os.path.splitext(file)[0].replace('_', ' ').title()
                if category not in nav:
                    nav[category] = []
                nav[category].append({page_title: rel_path.replace(os.sep, '/')})
    
    # Ordenar las entradas dentro de cada categoría
    for key in nav.keys():
        nav[key] = sorted(nav[key], key=lambda x: list(x.keys())[0])

    return nav

# Cargar el archivo mkdocs.yml
with open(mkdocs_path, 'r', encoding='utf-8') as file:
    mkdocs_data = yaml.safe_load(file)

# Construir la nueva estructura de navegación
base_dir = 'docs/pezas'
new_nav = build_nav(base_dir)

# Actualizar la sección 'nav' de 'Pezas' en mkdocs_data manteniendo el formato original
for section in mkdocs_data['nav']:
    if 'Pezas' in section:
        section['Pezas'] = []
        for category, pages in new_nav.items():
            section['Pezas'].append({category.capitalize(): pages})

# Guardar los cambios en el archivo mkdocs.yml
with open(mkdocs_path, 'w', encoding='utf-8') as file:
    yaml.dump(mkdocs_data, file, allow_unicode=True, sort_keys=False)

print('Archivo mkdocs.yml actualizado.')
