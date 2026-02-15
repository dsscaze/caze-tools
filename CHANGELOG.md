# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [0.3.0] - 2026-02-15

### Alterado
- **BREAKING CHANGE**: `czt merge` agora recebe apenas o arquivo de saída como argumento obrigatório
  - Diretório de origem agora é opcional via `-s, --source` (padrão: diretório atual)
  - Sintaxe antiga: `czt merge <dir> <output>`
  - Sintaxe nova: `czt merge <output> [--source <dir>]`
- **BREAKING CHANGE**: `czt ls-struct` agora usa opção para especificar o diretório
  - Diretório agora é opcional via `-p, --path` (padrão: diretório atual)
  - Sintaxe antiga: `czt ls-struct [dir]`
  - Sintaxe nova: `czt ls-struct [--path <dir>]`

### Corrigido
- Corrigido problema onde argumentos com default eram interpretados incorretamente pelo Click
- Comandos agora funcionam corretamente quando executados sem especificar o diretório

## [0.2.2] - 2026-02-09

### Corrigido
- Adicionado arquivos `__init__.py` faltantes nas pastas `caze_tools` e `caze_tools/commands`
- Pacote agora instala corretamente e pode ser importado

## [0.2.1] - 2026-02-09

### Corrigido
- Alias do comando principal revertido de `cz` para `czt`
- Documentação atualizada com o alias correto

## [0.2.0] - 2026-02-09

### Adicionado
- Comando `addprefix`: Adiciona prefixo a todos os arquivos de uma pasta
- Comando `rename`: Renomeia arquivos substituindo um prefixo por outro
- Comando `toroot`: Move arquivos de subpastas para a raiz
- Comando `trimimg`: Remove transparências desnecessárias de imagens PNG
- Documentação completa no README com todos os comandos
- Guia de publicação no PyPI em `/docs/publicacao-pypi.md`
- Arquivo CHANGELOG.md para controle de versões

### Alterado
- Alias do comando principal de `czt` para `cz` no setup.py
- Sincronização de versão entre pyproject.toml e setup.py

### Corrigido
- Proteção de arquivo `.pypirc` adicionada ao .gitignore

## [0.1.0] - Data anterior

### Adicionado
- Comando `mkstruct`: Cria estrutura de diretórios a partir de texto
- Comando `ls-struct`: Lista estrutura de diretórios em formato árvore
- Comando `merge`: Mescla múltiplos arquivos em um único arquivo
- Estrutura inicial do projeto
- Configuração de pacote Python com setuptools
- README inicial
- Licença MIT
