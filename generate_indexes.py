import yaml
import os

# Ruta del archivo mkdocs.yml
mkdocs_path = 'mkdocs.yml'

# Función para generar el contenido de los subíndices
def generate_sub_index(category, pages):
    content = f"# {category.capitalize()}\n\n"
    
    for page in sorted(pages, key=lambda x: list(x.keys())[0]):
        for title, path in page.items():
            # Crear enlace al directorio de la pieza
            base_name = os.path.splitext(os.path.basename(path))[0]
            category_path = category.lower().replace(' ', '_')
            link = f"/pezas/{category_path}/{base_name}/"
            content += f"- [{title}]({link})\n"
    
    content += "\n"
    return content

# Cargar el archivo mkdocs.yml
with open(mkdocs_path, 'r', encoding='utf-8') as file:
    mkdocs_data = yaml.safe_load(file)

# Generar y guardar los subíndices
for section in mkdocs_data['nav']:
    for key, value in section.items():
        if key == 'Pezas':
            for category in value:
                for cat_name, pages in category.items():
                    sub_index_content = generate_sub_index(cat_name, pages)
                    sub_index_path = os.path.join('docs', 'pezas', cat_name.lower(), 'index.md')
                    os.makedirs(os.path.dirname(sub_index_path), exist_ok=True)
                    with open(sub_index_path, 'w', encoding='utf-8') as file:
                        file.write(sub_index_content)

print('Índices de los géneros actualizados.')
