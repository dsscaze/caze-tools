import os
import click


def run(pasta_raiz, prefixo_antigo, novo_prefixo, dry_run):
    """Função principal que executa a lógica de troca de prefixo nos arquivos."""
    click.echo(f"📁 Processando pasta: {pasta_raiz}")
    click.echo(f"🔄 Substituindo '{prefixo_antigo}' por '{novo_prefixo}'")
    
    if dry_run:
        click.secho("🔍 Modo simulação (sem fazer alterações reais)", fg="yellow")
    
    contador_renomeados = 0
    contador_pulados = 0

    for raiz, subpastas, arquivos in os.walk(pasta_raiz):
        for nome_arquivo in arquivos:
            # Verifica se começa com o prefixo desejado
            if not nome_arquivo.startswith(prefixo_antigo):
                contador_pulados += 1
                continue

            caminho_antigo = os.path.join(raiz, nome_arquivo)
            novo_nome = nome_arquivo.replace(prefixo_antigo, novo_prefixo, 1)
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
    click.echo(f"  • Arquivos não renomeados (não começam com o prefixo): {contador_pulados}")
    click.secho("✨ Processo concluído.", fg="green")


@click.command("rename")
@click.argument("pasta_raiz", type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True))
@click.argument("prefixo_antigo", type=str)
@click.argument("novo_prefixo", type=str)
@click.option("--dry-run", is_flag=True, default=False, help="Simula as alterações sem fazer mudanças reais.")
def rename(pasta_raiz, prefixo_antigo, novo_prefixo, dry_run):
    """
    Substitui um prefixo por outro em todos os arquivos de uma pasta (recursivamente).
    
    Exemplo: caze-tools rename ./minha_pasta "old_" "new_"
    """
    run(pasta_raiz, prefixo_antigo, novo_prefixo, dry_run)
