import os
import click
import fnmatch # Para correspondência de padrões de nome de arquivo (ex: *.py)

# Padrões de arquivos e diretórios a serem ignorados por padrão
DEFAULT_IGNORE = [
    '.git', '.vscode', '.idea', '__pycache__', '*.pyc', '.DS_Store',
    'node_modules', '.venv', 'venv'
]

def collect_files(root_path, recursive, extensions=None, names=None, ignore_patterns=None):
    """Coleta uma lista de arquivos que correspondem aos critérios de filtro."""
    files_to_merge = []
    
    # Normaliza extensões para garantir que comecem com '.'
    normalized_exts = tuple(f".{ext.lstrip('.')}" for ext in extensions) if extensions else ()
    
    # Combina a lista de ignorados padrão com a fornecida
    all_ignore = DEFAULT_IGNORE + list(ignore_patterns or [])

    for dirpath, dirnames, filenames in os.walk(root_path, topdown=True):
        # Filtra os diretórios a serem ignorados
        dirnames[:] = [d for d in dirnames if d not in all_ignore]

        for filename in filenames:
            # Ignora arquivos individuais
            if filename in all_ignore:
                continue

            full_path = os.path.join(dirpath, filename)
            
            has_filters = bool(normalized_exts or names)
            matches = not has_filters  # Se não houver filtros, corresponde a tudo

            if normalized_exts and filename.endswith(normalized_exts):
                matches = True
            
            if names and any(fnmatch.fnmatch(filename, pattern) for pattern in names):
                matches = True

            if matches:
                files_to_merge.append(full_path)

        if not recursive:
            break  # Interrompe após o primeiro nível se não for recursivo

    return files_to_merge

def run(source_dir, output_file, extensions, names, recursive, limit, force, ignore):
    """Função principal que executa a lógica de mesclagem."""
    click.echo(f"🔍 Coletando arquivos de '{source_dir}'...")
    
    files_to_merge = collect_files(source_dir, recursive, extensions, names, ignore)
    
    if not files_to_merge:
        click.secho("Nenhum arquivo encontrado para mesclar com os filtros fornecidos.", fg="yellow")
        return

    file_count = len(files_to_merge)
    click.echo(f" Foram encontrados {file_count} arquivo(s) para mesclar.")

    # Verificação do limite de segurança
    if file_count > limit and not force:
        click.secho(
            f"\nAviso: O número de arquivos ({file_count}) excede o limite de segurança ({limit}).",
            fg="yellow"
        )
        if not click.confirm("Deseja continuar mesmo assim?"):
            click.echo("Operação cancelada pelo usuário.")
            return

    # Processo de mesclagem
    try:
        with open(output_file, 'w', encoding='utf-8') as dest_file:
            for filepath in files_to_merge:
                relative_path = os.path.relpath(filepath, source_dir)
                dest_file.write(f"--- Início de {relative_path} ---\n\n")
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as src_file:
                        dest_file.write(src_file.read())
                except Exception as e:
                    dest_file.write(f"[Erro ao ler o arquivo: {e}]\n")
                dest_file.write(f"\n\n--- Fim de {relative_path} ---\n\n")
        
        click.secho(f"\n✅ Arquivos mesclados com sucesso em: {output_file}", fg="green")
    except IOError as e:
        click.secho(f"Erro ao escrever no arquivo de saída: {e}", fg="red")

@click.command("merge")
@click.argument("source_dir", type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True), default=".")
@click.argument("output_file", type=click.Path(dir_okay=False, writable=True))
@click.option("-e", "--ext", multiple=True, help="Extensão do arquivo para incluir (ex: .py). Pode ser usado várias vezes.")
@click.option("-n", "--name", multiple=True, help="Padrão de nome de arquivo para incluir (ex: 'test_*.py'). Pode ser usado várias vezes.")
@click.option("--ignore", multiple=True, help="Nome de diretório ou arquivo a ignorar.")
@click.option("--no-recursive", is_flag=True, default=False, help="Não busca em subdiretórios.")
@click.option("--limit", type=int, default=100, help="Limite de arquivos antes de pedir confirmação.")
@click.option("-y", "--yes", is_flag=True, default=False, help="Pula a confirmação de segurança (force).")
def merge_command(source_dir, output_file, ext, name, no_recursive, limit, yes, ignore):
    """
    Mescla múltiplos arquivos de um diretório em um único arquivo de saída.
    
    Exemplos:
    
    - Mesclar todos os arquivos .py e .md do diretório atual em 'context.txt':
    
      caze-tools merge . context.txt -e .py -e .md
      
    - Mesclar todos os arquivos de teste do diretório 'src' em 'tests.txt':
    
      caze-tools merge src tests.txt -n "test_*.py"
    """
    run(
        source_dir=source_dir,
        output_file=output_file,
        extensions=ext,
        names=name,
        recursive=not no_recursive,
        limit=limit,
        force=yes,
        ignore=ignore
    )