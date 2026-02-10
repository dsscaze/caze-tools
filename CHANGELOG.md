# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Versionamento Semântico](https://semver.org/lang/pt-BR/).

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
