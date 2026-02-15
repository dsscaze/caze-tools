import os
import sys
import click

# Padrões de arquivos e diretórios a serem ignorados por padrão.
# Você pode adicionar mais, como 'node_modules', '.venv', etc.
DEFAULT_IGNORE = [
    '__pycache__',
    '.git',
    '.vscode',
    '.idea',
    '*.pyc',
    '*.pyo',
    '.DS_Store',
]

def generate_tree_lines(root_path, prefix="", ignore_patterns=None):
    """
    Gera recursivamente as linhas da árvore de diretórios.
    Esta função é um gerador (yields lines).
    """
    if ignore_patterns is None:
        ignore_patterns = DEFAULT_IGNORE

    # Lista o conteúdo, ignorando os padrões
    try:
        items = [item for item in os.listdir(root_path) if item not in ignore_patterns]
    except FileNotFoundError:
        return

    # Ordena para ter uma saída consistente (diretórios primeiro, depois arquivos)
    items.sort(key=lambda x: (not os.path.isdir(os.path.join(root_path, x)), x.lower()))

    for i, name in enumerate(items):
        is_last = (i == len(items) - 1)
        connector = "└── " if is_last else "├── "
        
        path = os.path.join(root_path, name)
        
        # Adiciona uma barra para diretórios
        display_name = name + "/" if os.path.isdir(path) else name
        
        yield prefix + connector + display_name

        if os.path.isdir(path):
            # Prepara o prefixo para o próximo nível de recursão
            extension = "    " if is_last else "│   "
            yield from generate_tree_lines(path, prefix=prefix + extension, ignore_patterns=ignore_patterns)

def run(root_path=".", output_file=None, ignore_patterns=None):
    """
    Função principal que executa a lógica de geração da árvore.
    """
    # Combina a lista de ignorados padrão com a fornecida pelo usuário
    all_ignore = DEFAULT_IGNORE + list(ignore_patterns or [])

    # Abre o arquivo de saída ou usa a saída padrão (console)
    output_stream = open(output_file, "w", encoding="utf-8") if output_file else sys.stdout

    try:
        # Imprime a raiz do projeto
        root_name = os.path.basename(os.path.abspath(root_path))
        print(f"{root_name}/", file=output_stream)
        
        # Gera e imprime o restante da árvore
        for line in generate_tree_lines(root_path, ignore_patterns=all_ignore):
            print(line, file=output_stream)
        
        if output_file:
            print(f"\n✅ Estrutura salva com sucesso em: {output_file}")

    finally:
        # Garante que o arquivo seja fechado se não for a saída padrão
        if output_file:
            output_stream.close()

@click.command("ls-struct")
@click.option(
    "-p", "--path", "root_path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True),
    default=".",
    help="Diretório a analisar (padrão: diretório atual)."
)
@click.option(
    "-o", "--output",
    type=click.Path(dir_okay=False, writable=True),
    help="Arquivo de saída para salvar a estrutura (ex: structure.md)."
)
@click.option(
    "--ignore",
    multiple=True,
    help="Nome de diretório ou arquivo a ignorar. Pode ser usado várias vezes."
)
def ls_struct_command(root_path, output, ignore):
    """Gera uma representação em árvore de um diretório."""
    run(root_path, output_file=output, ignore_patterns=ignore)