import os
import yaml

# Función para generar el contenido de los subíndices
def generate_sub_index(category, base_path):
    content = f"# {category.capitalize()}\n\n"
    content += "- Y aquí una lista alfabética de todas las piezas\n\n"

    files = sorted(os.listdir(base_path))
    for file in files:
        if file.endswith('.md'):
            title = os.path.splitext(file)[0].replace('_', ' ').title()
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
