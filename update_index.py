import yaml

# Ruta del archivo mkdocs.yml
mkdocs_path = 'mkdocs.yml'
# Ruta del archivo index.md
index_md_path = 'docs/index.md'

# Función para crear el contenido de index.md basado en la estructura de mkdocs.yml
def generate_index_md(mkdocs_data):
    index_md_content = "# Foliada Cheatsheet\n\n"

    for section in mkdocs_data['nav']:
        for key, value in section.items():
            if key == 'Pezas':
                index_md_content += f"## {key}\n\n"
                for category in value:
                    for cat_name, pages in category.items():
                        index_md_content += f"### {cat_name}\n"
                        for page in pages:
                            for page_title, page_path in page.items():
                                index_md_content += f"- [{page_title}]({page_path})\n"
                        index_md_content += "\n"
    
    return index_md_content

# Cargar el archivo mkdocs.yml
with open(mkdocs_path, 'r', encoding='utf-8') as file:
    mkdocs_data = yaml.safe_load(file)

# Generar el contenido de index.md
index_md_content = generate_index_md(mkdocs_data)

# Guardar el contenido en index.md
with open(index_md_path, 'w', encoding='utf-8') as file:
    file.write(index_md_content)

print('Archivo index.md actualizado.')
