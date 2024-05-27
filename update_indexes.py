import os
import yaml

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

# Función para generar el contenido de los subíndices
def generate_sub_index(category, base_path):
    content = f"# {category.capitalize()}\n\n"

    # Crear una lista de tuplas (title, file) para ordenar por title
    files_with_titles = []
    files = sorted(os.listdir(base_path))
    for file in files:
        if file.endswith('.md'):
            file_path = os.path.join(base_path, file)
            header = extract_yaml_header(file_path)
            title = header.get('title', os.path.splitext(file)[0].replace('_', ' ').title())
            files_with_titles.append((title, file))
    
    # Ordenar la lista de tuplas por el título
    files_with_titles.sort(key=lambda x: x[0].lower())

    for title, file in files_with_titles:
        link = f"pezas/{file}"
        content += f"- [{title}]({link})\n"

    content += "\n"
    return content

# Ruta base para los géneros
genres_path = 'docs/pezas'
genres = [d for d in os.listdir(genres_path) if os.path.isdir(os.path.join(genres_path, d))]

# Generar y guardar los subíndices
for genre in genres:
    base_path = os.path.join(genres_path, genre, 'pezas')
    sub_index_content = generate_sub_index(genre, base_path)
    sub_index_path = os.path.join('docs', 'pezas', genre, 'index.md')
    os.makedirs(os.path.dirname(sub_index_path), exist_ok=True)
    with open(sub_index_path, 'w', encoding='utf-8') as file:
        file.write(sub_index_content)

print('Índices de los géneros actualizados.')
