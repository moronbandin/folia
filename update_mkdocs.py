import os
import yaml

# Ruta del archivo mkdocs.yml
mkdocs_path = 'mkdocs.yml'

# Función para extraer el encabezado YAML de un archivo Markdown
def extract_yaml_header(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    yaml_lines = []
    in_yaml = False
    for line in lines:
        if line.strip() == '---':
            if in_yaml:
                break
            else:
                in_yaml = True
        elif in_yaml:
            yaml_lines.append(line)
    
    if yaml_lines:
        return yaml.safe_load(''.join(yaml_lines))
    return {}

# Función para generar la entrada de navegación para cada género
def generate_nav_entry(category, base_path):
    nav_entry = {category.capitalize(): []}

    files_with_titles = []
    files = sorted(os.listdir(base_path))
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(base_path, file)
            header = extract_yaml_header(file_path)
            title = header.get('title', os.path.splitext(file)[0].replace('_', ' ').title())
            path = file_path.replace('docs/', '')
            files_with_titles.append((title, path))
    
    # Ordenar alfabéticamente por título
    files_with_titles.sort(key=lambda x: x[0].lower())

    for title, path in files_with_titles:
        nav_entry[category.capitalize()].append({title: path})

    return nav_entry

# Cargar el archivo mkdocs.yml
with open(mkdocs_path, 'r', encoding='utf-8') as file:
    mkdocs_data = yaml.safe_load(file)

# Generar la nueva estructura de navegación para 'Pezas'
new_nav = []
genres_path = 'docs/pezas'
genres = [d for d in os.listdir(genres_path) if os.path.isdir(os.path.join(genres_path, d, 'pezas'))]

for genre in genres:
    base_path = os.path.join(genres_path, genre, 'pezas')
    nav_entry = generate_nav_entry(genre, base_path)
    new_nav.append(nav_entry)

# Actualizar la sección 'nav' de 'Pezas' en mkdocs_data
for section in mkdocs_data['nav']:
    if 'Pezas' in section:
        section['Pezas'] = new_nav

# Guardar los cambios en el archivo mkdocs.yml
with open(mkdocs_path, 'w', encoding='utf-8') as file:
    yaml.dump(mkdocs_data, file, allow_unicode=True, sort_keys=False)

print('Sección de navegación "Pezas" actualizada en mkdocs.yml.')
