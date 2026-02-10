import os
import shutil
import click


def run(pasta_raiz, dry_run):
    """Função principal que executa a lógica de trazer arquivos para a raiz."""
    click.echo(f"📁 Processando pasta: {pasta_raiz}")
    
    if dry_run:
        click.secho("🔍 Modo simulação (sem fazer alterações reais)", fg="yellow")
    
    contador_movidos = 0
    contador_pulados = 0

    for raiz, dirs, arquivos in os.walk(pasta_raiz):
        for arquivo in arquivos:
            caminho_origem = os.path.join(raiz, arquivo)

            # Ignora arquivos que já estão na raiz
            if raiz == pasta_raiz:
                contador_pulados += 1
                continue

            caminho_destino = os.path.join(pasta_raiz, arquivo)

            # Se já existir arquivo com mesmo nome, cria sufixo incremental
            if os.path.exists(caminho_destino):
                nome, ext = os.path.splitext(arquivo)
                contador = 1

                while True:
                    novo_nome = f"{nome}_{contador}{ext}"
                    novo_destino = os.path.join(pasta_raiz, novo_nome)

                    if not os.path.exists(novo_destino):
                        caminho_destino = novo_destino
                        break

                    contador += 1

            if dry_run:
                click.echo(f"  [SIM] Moveria: {arquivo} → {caminho_destino}")
            else:
                try:
                    shutil.move(caminho_origem, caminho_destino)
                    click.echo(f"  ✅ Movido: {arquivo} → {caminho_destino}")
                    contador_movidos += 1
                except OSError as e:
                    click.secho(f"  ❌ Erro ao mover {arquivo}: {e}", fg="red")

    click.echo()
    click.echo(f"📊 Resumo:")
    click.echo(f"  • Arquivos movidos: {contador_movidos}")
    click.echo(f"  • Arquivos pulados (já na raiz): {contador_pulados}")
    click.secho("✨ Processo concluído.", fg="green")


@click.command("toroot")
@click.argument("pasta_raiz", type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True))
@click.option("--dry-run", is_flag=True, default=False, help="Simula as alterações sem fazer mudanças reais.")
def toroot(pasta_raiz, dry_run):
    """
    Move todos os arquivos de subpastas para a raiz, criando nomes com sufixo 
    incremental em caso de conflito.
    
    Exemplo: caze-tools toroot ./minha_pasta
    """
    run(pasta_raiz, dry_run)
