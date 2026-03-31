import re
import click


def extrair_valor(linha, chave):
    match = re.search(rf"{re.escape(chave)}\s*:\s*(.+)", linha)
    if match:
        return match.group(1).strip()
    return None


def run(arquivo, chave, contar, distintos, saida):
    valores = []

    with open(arquivo, "r", encoding="utf-8", errors="ignore") as f:
        for linha in f:
            if chave in linha:
                valor = extrair_valor(linha, chave)
                if valor is not None:
                    valores.append(valor)

    if contar:
        click.echo(f"Total de ocorrências de '{chave}': {len(valores)}")
        return

    if distintos:
        unicos = sorted(set(valores))
        click.echo(f"Valores distintos de '{chave}' ({len(unicos)}):")
        for v in unicos:
            click.echo(f"  {v}")
        return

    if not saida:
        base = arquivo.rsplit(".", 1)
        saida = base[0] + f"_{chave}.txt" if len(base) > 1 else arquivo + f"_{chave}.txt"

    with open(saida, "w", encoding="utf-8") as f:
        for v in valores:
            f.write(v + "\n")

    click.echo(f"{len(valores)} linhas extraídas → {saida}")


@click.command("extractlog")
@click.argument("arquivo", type=click.Path(exists=True, file_okay=True, dir_okay=False, readable=True))
@click.argument("chave")
@click.option("--contar", is_flag=True, default=False, help="Conta o total de ocorrências.")
@click.option("--distintos", is_flag=True, default=False, help="Lista e conta os valores distintos.")
@click.option("--saida", default=None, help="Caminho do arquivo de saída (padrão: <arquivo>_<chave>.txt).")
def extractlog(arquivo, chave, contar, distintos, saida):
    """
    Extrai valores de linhas de log que contenham uma chave no formato 'chave: valor'.

    Por padrão, salva os valores extraídos em um novo arquivo.
    Use --contar para contar ocorrências ou --distintos para listar valores únicos.

    Exemplo: caze-tools extractlog [arquivo] [chaveProcurada]
    """
    run(arquivo, chave, contar, distintos, saida)
