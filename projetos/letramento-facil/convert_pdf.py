import os
import sys
import subprocess
import tempfile

def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
    finally:
        globals()[package] = importlib.import_module(package)

# Garante que o pacote 'markdown' esteja instalado para uma conversão perfeita
install_and_import('markdown')

def find_browser():
    # Caminhos comuns do Edge e Chrome no Windows
    paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    ]
    for path in paths:
        if os.path.exists(path):
            return path
    return None

def convert_md_to_pdf(md_path, pdf_path):
    if not os.path.exists(md_path):
        print(f"Erro: Arquivo MD não encontrado em {md_path}")
        return False

    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Remove o bloco de metadados Frontmatter (--- ... ---) para o PDF ficar limpo
    if md_content.strip().startswith('---'):
        parts = md_content.split('---', 2)
        if len(parts) >= 3:
            md_content = parts[2].strip()

    # Remove a seção "Ver também" (links internos do cérebro irrelevantes para o PDF final)
    if "## Ver também" in md_content:
        md_content = md_content.split("## Ver também")[0].strip()

    # Converter Markdown para HTML
    # Ativa extensões para tabelas e blocos de código
    html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

    # CSS de alta qualidade para um visual executivo/corporativo moderno
    css_styles = """
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333333;
        line-height: 1.6;
        margin: 40px;
        background-color: #ffffff;
    }
    h1, h2, h3, h4 {
        color: #1a365d;
        font-weight: 700;
        margin-top: 24px;
        margin-bottom: 12px;
    }
    h1 {
        font-size: 28px;
        border-bottom: 2px solid #2b6cb0;
        padding-bottom: 8px;
    }
    h2 {
        font-size: 22px;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 6px;
        margin-top: 30px;
    }
    h3 {
        font-size: 18px;
        color: #2b6cb0;
    }
    p {
        margin-bottom: 16px;
        font-size: 14px;
    }
    ul, ol {
        margin-bottom: 16px;
        padding-left: 20px;
        font-size: 14px;
    }
    li {
        margin-bottom: 6px;
    }
    hr {
        border: 0;
        border-top: 1px solid #e2e8f0;
        margin: 30px 0;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 24px;
        font-size: 13px;
    }
    th, td {
        border: 1px solid #cbd5e0;
        padding: 10px 12px;
        text-align: left;
    }
    th {
        background-color: #ebf8ff;
        color: #2b6cb0;
        font-weight: bold;
    }
    tr:nth-child(even) {
        background-color: #f7fafc;
    }
    blockquote {
        margin: 0 0 16px;
        padding: 10px 20px;
        background-color: #f7fafc;
        border-left: 4px solid #2b6cb0;
        color: #4a5568;
        font-style: italic;
    }
    code {
        font-family: Consolas, Monaco, 'Andale Mono', monospace;
        background-color: #edf2f7;
        padding: 2px 4px;
        border-radius: 4px;
        font-size: 13px;
    }
    pre {
        background-color: #edf2f7;
        padding: 12px;
        border-radius: 6px;
        overflow-x: auto;
        margin-bottom: 16px;
    }
    pre code {
        background-color: transparent;
        padding: 0;
    }
    @media print {
        body {
            margin: 20px;
            font-size: 12pt;
        }
        h1, h2, h3 {
            page-break-after: avoid;
        }
        tr {
            page-break-inside: avoid;
        }
    }
    """

    # Montar o HTML completo
    md_dir_path = os.path.dirname(os.path.abspath(md_path)).replace("\\", "/")
    full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <base href="file:///{md_dir_path}/">
    <title>Plano de Letramento</title>
    <style>
        {css_styles}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

    # Salvar em arquivo HTML temporário
    temp_dir = tempfile.gettempdir()
    temp_html_path = os.path.join(temp_dir, "temp_facil_doc.html")
    with open(temp_html_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    browser_path = find_browser()
    if not browser_path:
        print("Erro: Não foi possível localizar o Microsoft Edge ou o Google Chrome para converter o arquivo em PDF.")
        print(f"O HTML foi salvo temporariamente em: {temp_html_path}")
        return False

    print(f"Usando navegador: {browser_path}")
    
    # Executa o navegador em modo headless para gerar o PDF
    cmd = [
        browser_path,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        temp_html_path
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"Sucesso! PDF gerado e salvo em: {pdf_path}")
        # Remover HTML temporário
        if os.path.exists(temp_html_path):
            os.remove(temp_html_path)
        return True
    except Exception as e:
        print(f"Erro durante a conversão do PDF: {e}")
        return False

if __name__ == "__main__":
    # Caminhos relativos ao diretório do próprio script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    md_dir = os.path.join(current_dir, "md")
    pdf_dir = os.path.join(current_dir, "pdf")
    
    # Garante que o diretório de destino dos PDFs exista
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)
        
    # Lista todos os arquivos .md no diretório md/
    files_to_convert = []
    if os.path.exists(md_dir):
        for file in os.listdir(md_dir):
            if file.endswith(".md") and file != "letramento-facil.md":
                files_to_convert.append(file)
            
    print(f"Encontrados {len(files_to_convert)} arquivos para conversao em PDF.")
    
    success_count = 0
    for md_filename in files_to_convert:
        md_file = os.path.join(md_dir, md_filename)
        pdf_filename = md_filename.replace(".md", ".pdf")
        pdf_file = os.path.join(pdf_dir, pdf_filename)
        
        print(f"\nIniciando conversao de: {md_file} -> {pdf_file}")
        if convert_md_to_pdf(md_file, pdf_file):
            success_count += 1
            
    print(f"\nProcesso concluido! {success_count} de {len(files_to_convert)} arquivos convertidos com sucesso.")
