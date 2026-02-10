
# caze-tools 🧰

Uma coleção de ferramentas de linha de comando (CLI) para auxiliar em tarefas comuns de desenvolvimento. Criado por [Daniel Caze (dsscaze)](https://github.com/dsscaze).

## O que é?

`caze-tools` (ou simplesmente `cz`) é uma CLI projetada para automatizar e simplificar rotinas de desenvolvimento, como criar estruturas de projetos, gerar representações de diretórios e mesclar arquivos de código-fonte.

## Instalação

### Via PyPI (Recomendado)

Após a publicação no PyPI, você poderá instalar diretamente:

```bash
pip install caze-tools
```

### A partir do código-fonte

Para desenvolvimento ou versão mais recente:

```bash
git clone https://github.com/dsscaze/caze-tools.git
cd caze-tools
pip install -e .
```

## Comandos Disponíveis

O comando principal é `czt` (um alias para `caze-tools`).

### `czt mkstruct`

Cria uma estrutura de diretórios e arquivos a partir de uma representação em texto (árvore de diretórios).

**Uso:**
```bash
czt mkstruct <arquivo_fonte.md>
```

**Exemplo `estrutura.md`:**
```
meu-projeto/
├── src/
│   ├── __init__.py
│   └── main.py
└── README.md
```

Ao executar `czt mkstruct estrutura.md`, a estrutura acima será criada no diretório atual.

### `czt ls-struct`

Faz o inverso do `mkstruct`: lê uma estrutura de diretórios existente e gera uma representação em árvore.

**Uso:**
```bash
# Imprime a estrutura do diretório atual no console
czt ls-struct

# Salva a estrutura em um arquivo
czt ls-struct -o project_tree.md

# Gera a estrutura de outra pasta
czt ls-struct ../outro-projeto
```

### `czt merge`

Mescla múltiplos arquivos de um diretório em um único arquivo de saída. Extremamente útil para criar contextos para LLMs ou para arquivar código.

**Uso:**
```bash
czt merge <diretorio_origem> <arquivo_saida> [opções]
```

**Exemplos:**

- Mesclar todos os arquivos `.py` e `.js` em `context.txt`:
  ```bash
  czt merge . context.txt --ext py --ext js
  ```

- Mesclar todos os arquivos de teste do diretório `src`:
  ```bash
  czt merge src tests_merged.txt --name "test_*.py"
  ```

### `czt addprefix`

Adiciona um prefixo a todos os arquivos de uma pasta (recursivamente).

**Uso:**
```bash
czt addprefix <pasta> <prefixo> [--dry-run]
```

**Exemplos:**

- Adicionar prefixo "old_" a todos os arquivos:
  ```bash
  czt addprefix ./minha-pasta old_
  ```

- Simular sem fazer alterações reais:
  ```bash
  czt addprefix ./minha-pasta new_ --dry-run
  ```

### `czt rename`

Renomeia arquivos substituindo um prefixo por outro (recursivamente).

**Uso:**
```bash
czt rename <pasta> <prefixo_antigo> <novo_prefixo> [--dry-run]
```

**Exemplos:**

- Trocar prefixo "old_" por "new_":
  ```bash
  czt rename ./minha-pasta old_ new_
  ```

- Simular a operação antes de executar:
  ```bash
  czt rename ./minha-pasta test_ prod_ --dry-run
  ```

### `czt toroot`

Move todos os arquivos de subpastas para a pasta raiz, mantendo nomes únicos.

**Uso:**
```bash
czt toroot <pasta> [--dry-run]
```

**Exemplos:**

- Mover todos os arquivos para a raiz:
  ```bash
  czt toroot ./minha-pasta
  ```

- Simular a operação:
  ```bash
  czt toroot ./minha-pasta --dry-run
  ```

### `czt trimimg`

Remove transparências desnecessárias de imagens PNG, reduzindo o tamanho do arquivo.

**Uso:**
```bash
czt trimimg <pasta> [--padding N] [--threshold N] [--dry-run]
```

**Opções:**
- `--padding`: Pixels de margem a manter (padrão: 0)
- `--threshold`: Nível de transparência mínimo (0-255, padrão: 10)

**Exemplos:**

- Processar todas as PNGs com padding de 5px:
  ```bash
  czt trimimg ./imagens --padding 5
  ```

- Simular processamento:
  ```bash
  czt trimimg ./imagens --dry-run
  ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* para relatar bugs ou sugerir novas funcionalidades.

## Publicação

Se você é mantenedor e deseja publicar uma nova versão no PyPI, consulte o [Guia de Publicação](docs/publicacao-pypi.md).

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
