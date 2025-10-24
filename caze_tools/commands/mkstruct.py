import os
import re
import sys
import click

def parse_tree_lines(lines):
    """
    Analisa as linhas de uma representação de árvore de diretórios e reconstrói
    os caminhos completos para cada arquivo e pasta.
    """
    items = []
    path_stack = []  # Pilha para manter o controle dos diretórios pais

    for line in lines:
        # Ignora linhas vazias ou que são apenas conectores verticais
        if not line.strip() or line.strip() == '│':
            continue

        # Calcula o nível de indentação
        # Regex para encontrar o início do conteúdo real (ignora os caracteres da árvore)
        match = re.search(r'[^│\s├└─]', line)
        if not match:
            continue
        indent = match.start()
        
        # O nível é baseado na indentação. Assumimos 4 caracteres por nível (ex: "│   " ou "    ")
        # mas uma abordagem mais robusta é simplesmente usar a indentação.
        # Aqui, vamos usar um divisor comum como 4 para definir níveis discretos.
        level = indent // 4

        # Extrai o nome do arquivo/diretório da linha
        # Remove os caracteres da árvore e espaços em branco
        name_part = re.sub(r'^[│\s├└─]+', '', line).strip()
        # Remove comentários inline (ex: "← comentário")
        name_part = name_part.split('←')[0].strip()

        if not name_part:
            continue

        # Ajusta a pilha de caminhos para corresponder ao nível atual
        # Se o nível atual for menor, "subimos" na árvore de diretórios
        while len(path_stack) > level:
            path_stack.pop()

        # Constrói o caminho completo
        full_path = os.path.join(*path_stack, name_part)
        items.append(full_path)

        # Se o item atual for um diretório, adiciona-o à pilha para os próximos itens
        if name_part.endswith('/'):
            # Adiciona à pilha sem a barra final
            path_stack.append(name_part.strip('/'))

    return items

def ensure_path(path):
    if path.endswith("/"):
        os.makedirs(path, exist_ok=True)
        return f"[DIR] {path}"
    else:
        dirn = os.path.dirname(path)
        if dirn:
            os.makedirs(dirn, exist_ok=True)
        # create empty file if not exists
        open(path, "a", encoding="utf-8").close()
        return f"[FILE] {path}"

def run(source_file):
    if not os.path.exists(source_file):
        print(f"Arquivo não encontrado: {source_file}", file=sys.stderr)
        return 1

    with open(source_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    items = parse_tree_lines(lines)
    created = []
    for it in items:
        if not it:
            continue
        created.append(ensure_path(it))

    print("✅ Estrutura criada com sucesso!")
    for c in created:
        print(" ", c)
    return 0

@click.command("mkstruct")
@click.argument("source", type=click.Path(exists=True, dir_okay=False))
def mkstruct_command(source):
    """Cria estrutura de diretórios a partir de um arquivo .md"""
    run(source)
