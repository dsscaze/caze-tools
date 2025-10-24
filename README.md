
# caze-tools 🧰

Uma coleção de ferramentas de linha de comando (CLI) para auxiliar em tarefas comuns de desenvolvimento. Criado por [Daniel Caze (dsscaze)](https://github.com/dsscaze).

## O que é?

`caze-tools` (ou simplesmente `cz`) é uma CLI projetada para automatizar e simplificar rotinas de desenvolvimento, como criar estruturas de projetos, gerar representações de diretórios e mesclar arquivos de código-fonte.

## Instalação

Você pode instalar o `caze-tools` diretamente do PyPI (quando publicado) ou do repositório Git.

```bash
# Para instalar a versão estável (ainda não disponível)
# pip install caze-tools

# Para instalar para desenvolvimento a partir do código-fonte
git clone https://github.com/dsscaze/caze-tools.git
cd caze-tools
pip install -e .
```

## Comandos Disponíveis

O comando principal é `cz` (um alias para `caze-tools`).

### `cz mkstruct`

Cria uma estrutura de diretórios e arquivos a partir de uma representação em texto (árvore de diretórios).

**Uso:**
```bash
cz mkstruct <arquivo_fonte.md>
```

**Exemplo `estrutura.md`:**
```
meu-projeto/
├── src/
│   ├── __init__.py
│   └── main.py
└── README.md
```

Ao executar `cz mkstruct estrutura.md`, a estrutura acima será criada no diretório atual.

### `cz ls-struct`

Faz o inverso do `mkstruct`: lê uma estrutura de diretórios existente e gera uma representação em árvore.

**Uso:**
```bash
# Imprime a estrutura do diretório atual no console
cz ls-struct

# Salva a estrutura em um arquivo
cz ls-struct -o project_tree.md

# Gera a estrutura de outra pasta
cz ls-struct ../outro-projeto
```

### `cz merge`

Mescla múltiplos arquivos de um diretório em um único arquivo de saída. Extremamente útil para criar contextos para LLMs ou para arquivar código.

**Uso:**
```bash
cz merge <diretorio_origem> <arquivo_saida> [opções]
```

**Exemplos:**

- Mesclar todos os arquivos `.py` e `.js` em `context.txt`:
  ```bash
  cz merge . context.txt --ext py --ext js
  ```

- Mesclar todos os arquivos de teste do diretório `src`:
  ```bash
  cz merge src tests_merged.txt --name "test_*.py"
  ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* para relatar bugs ou sugerir novas funcionalidades.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
