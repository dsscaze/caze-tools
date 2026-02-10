import os
import click


def run(pasta_raiz, prefixo, dry_run):
    """Função principal que executa a lógica de adição de prefixo aos arquivos."""
    click.echo(f"📁 Processando pasta: {pasta_raiz}")
    click.echo(f"📌 Prefixo a adicionar: '{prefixo}'")
    
    if dry_run:
        click.secho("🔍 Modo simulação (sem fazer alterações reais)", fg="yellow")
    
    contador_renomeados = 0
    contador_pulados = 0

    for raiz, subpastas, arquivos in os.walk(pasta_raiz):
        for nome_arquivo in arquivos:
            # Evita adicionar o prefixo duas vezes
            if nome_arquivo.startswith(prefixo):
                contador_pulados += 1
                continue

            caminho_antigo = os.path.join(raiz, nome_arquivo)
            novo_nome = prefixo + nome_arquivo
            caminho_novo = os.path.join(raiz, novo_nome)

            if dry_run:
                click.echo(f"  [SIM] Renomearia: {nome_arquivo} → {novo_nome}")
            else:
                try:
                    os.rename(caminho_antigo, caminho_novo)
                    click.echo(f"  ✅ Renomeado: {nome_arquivo} → {novo_nome}")
                    contador_renomeados += 1
                except OSError as e:
                    click.secho(f"  ❌ Erro ao renomear {nome_arquivo}: {e}", fg="red")

    click.echo()
    click.echo(f"📊 Resumo:")
    click.echo(f"  • Arquivos renomeados: {contador_renomeados}")
    click.echo(f"  • Arquivos pulados (já possuem prefixo): {contador_pulados}")
    click.secho("✨ Processo concluído.", fg="green")


@click.command("addprefix")
@click.argument("pasta_raiz", type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True))
@click.argument("prefixo", type=str)
@click.option("--dry-run", is_flag=True, default=False, help="Simula as alterações sem fazer mudanças reais.")
def addprefix(pasta_raiz, prefixo, dry_run):
    """
    Adiciona um prefixo a todos os arquivos de uma pasta (recursivamente).
    
    Exemplo: caze-tools addprefix ./minha_pasta "novo_"
    """
    run(pasta_raiz, prefixo, dry_run)
