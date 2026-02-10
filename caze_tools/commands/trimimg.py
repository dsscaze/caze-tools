import os
from PIL import Image
import click


def run(pasta_raiz, padding, threshold, dry_run):
    """Função principal que executa a lógica de trim em imagens."""
    click.echo(f"📁 Processando pasta: {pasta_raiz}")
    click.echo(f"✂️  Configurações: padding={padding}px, threshold={threshold}")
    
    if dry_run:
        click.secho("🔍 Modo simulação (sem fazer alterações reais)", fg="yellow")
    
    contador_sucesso = 0
    contador_erro = 0
    contador_pulado = 0

    for raiz, dirs, arquivos in os.walk(pasta_raiz):
        for arquivo in arquivos:
            if not arquivo.lower().endswith(".png"):
                continue

            caminho_completo = os.path.join(raiz, arquivo)

            try:
                img = Image.open(caminho_completo).convert("RGBA")
                pixels = img.load()
                width, height = img.size

                x_min, y_min = width, height
                x_max, y_max = 0, 0

                # Encontra os limites da área não-transparente
                for y in range(height):
                    for x in range(width):
                        _, _, _, a = pixels[x, y]
                        if a >= threshold:
                            x_min = min(x_min, x)
                            y_min = min(y_min, y)
                            x_max = max(x_max, x)
                            y_max = max(y_max, y)

                # Verifica se a imagem é totalmente transparente
                if x_max <= x_min or y_max <= y_min:
                    click.secho(f"  ⏭️  Pulado: {arquivo} (totalmente transparente)", fg="yellow")
                    contador_pulado += 1
                    continue

                # Aplica padding
                x_min = max(0, x_min - padding)
                y_min = max(0, y_min - padding)
                x_max = min(width, x_max + padding)
                y_max = min(height, y_max + padding)

                if dry_run:
                    click.echo(f"  [SIM] Faria trim em: {arquivo}")
                else:
                    cropped = img.crop((x_min, y_min, x_max + 1, y_max + 1))
                    cropped.save(caminho_completo)
                    click.echo(f"  ✅ Trimmed: {arquivo}")
                    contador_sucesso += 1

            except Exception as e:
                click.secho(f"  ❌ Erro ao processar {arquivo}: {e}", fg="red")
                contador_erro += 1

    click.echo()
    click.echo(f"📊 Resumo:")
    click.echo(f"  • Imagens processadas: {contador_sucesso}")
    click.echo(f"  • Imagens puladas: {contador_pulado}")
    click.echo(f"  • Erros: {contador_erro}")
    click.secho("✨ Processo concluído.", fg="green")


@click.command("trimimg")
@click.argument("pasta_raiz", type=click.Path(exists=True, file_okay=False, dir_okay=True, readable=True))
@click.option("--padding", type=int, default=2, help="Pixels de margem ao redor da área trimmed.")
@click.option("--threshold", type=int, default=1, help="Limite de alpha para considerar pixel não-transparente (0-255).")
@click.option("--dry-run", is_flag=True, default=False, help="Simula as alterações sem fazer mudanças reais.")
def trimimg(pasta_raiz, padding, threshold, dry_run):
    """
    Remove pixels transparentes de imagens PNG (trim image).
    Processa recursivamente todos os PNGs da pasta.
    
    Exemplo: caze-tools trimimg ./minha_pasta
    """
    run(pasta_raiz, padding, threshold, dry_run)
