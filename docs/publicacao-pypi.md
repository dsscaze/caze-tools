# Guia de Publicação no PyPI

Este documento explica como publicar o `caze-tools` no PyPI para que ele fique disponível via `pip install`.

## Pré-requisitos

1. **Conta no PyPI**: Crie uma conta em [https://pypi.org/account/register/](https://pypi.org/account/register/)
2. **Conta no TestPyPI** (opcional, mas recomendado): [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/)
3. **Ferramentas de build instaladas**:
   ```bash
   py -m pip install --upgrade build twine
   ```

## Passo a Passo

### 1. Preparar o Projeto

Certifique-se de que os arquivos de configuração estão corretos:

#### Verificar `pyproject.toml`
- ✅ Nome do pacote está correto
- ✅ Versão está atualizada
- ✅ Descrição está completa
- ✅ Email do autor está preenchido
- ✅ URL do repositório está correta
- ✅ Classificadores estão apropriados
- ✅ Dependências listadas

#### Verificar `setup.py` (se usado)
- ✅ Versão corresponde ao `pyproject.toml`
- ✅ Entry points estão corretos

#### Verificar `README.md`
- ✅ Documentação completa e atualizada
- ✅ Exemplos de uso incluídos
- ✅ Instruções de instalação corretas

### 2. Atualizar a Versão

Antes de cada publicação, atualize a versão em:
- `pyproject.toml`: linha `version = "X.Y.Z"`
- `setup.py`: linha `version="X.Y.Z"`

Siga o [Versionamento Semântico](https://semver.org/lang/pt-BR/):
- **MAJOR** (X): Mudanças incompatíveis na API
- **MINOR** (Y): Novas funcionalidades compatíveis
- **PATCH** (Z): Correções de bugs

Exemplo:
- `0.1.0` → Primeira versão de desenvolvimento
- `0.2.0` → Adiciona novos comandos
- `0.2.1` → Corrige bugs
- `1.0.0` → Primeira versão estável

### 3. Limpar Builds Anteriores

```bash
# No PowerShell
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue
```

### 4. Criar o Pacote de Distribuição

```bash
py -m build
```

Isso criará dois arquivos na pasta `dist/`:
- Um arquivo `.tar.gz` (source distribution)
- Um arquivo `.whl` (wheel distribution)

### 5. Testar no TestPyPI (Recomendado)

Antes de publicar no PyPI oficial, teste no TestPyPI:

```bash
py -m twine upload --repository testpypi dist/*
```

Você será solicitado a:
- Username: seu usuário do TestPyPI
- Password: sua senha ou token de API

Depois, teste a instalação:

```bash
pip install --index-url https://test.pypi.org/simple/ caze-tools
```

### 6. Publicar no PyPI Oficial

Quando estiver tudo funcionando:

```bash
py -m twine upload dist/*
```

Você será solicitado a:
- Username: `__token__`
- Password: seu token de API do PyPI (recomendado) ou sua senha

### 7. Verificar a Publicação

Acesse [https://pypi.org/project/caze-tools/](https://pypi.org/project/caze-tools/) e verifique se:
- ✅ Descrição está correta
- ✅ README renderizado corretamente
- ✅ Links funcionando
- ✅ Versão correta

### 8. Testar a Instalação

Em um ambiente limpo:

```bash
pip install caze-tools
cz --help
```

## Configuração de Token de API (Recomendado)

Para maior segurança, use tokens de API ao invés de senha:

1. Acesse [https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/)
2. Clique em "Add API token"
3. Nomeie o token (ex: "caze-tools-upload")
4. Selecione o escopo (pode ser global ou específico do projeto)
5. Copie o token gerado (começa com `pypi-`)

Configure o token no arquivo `~/.pypirc`:

```ini
[pypi]
username = __token__
password = pypi-seu-token-aqui

[testpypi]
username = __token__
password = pypi-seu-token-de-teste-aqui
```

**IMPORTANTE**: Nunca commite este arquivo no Git!

Adicione ao `.gitignore`:
```
.pypirc
```

## Automatização com GitHub Actions (Opcional)

Para automatizar a publicação via CI/CD, você pode criar um workflow no GitHub:

```yaml
# .github/workflows/publish.yml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install build twine
    - name: Build package
      run: python -m build
    - name: Publish to PyPI
      env:
        TWINE_USERNAME: __token__
        TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
      run: twine upload dist/*
```

Adicione o token como secret no GitHub:
1. Vá em `Settings` → `Secrets and variables` → `Actions`
2. Clique em `New repository secret`
3. Nome: `PYPI_API_TOKEN`
4. Valor: seu token do PyPI

## Checklist Antes de Publicar

- [ ] Todos os testes passando
- [ ] README atualizado
- [ ] CHANGELOG atualizado (se houver)
- [ ] Versão incrementada
- [ ] Build limpa (`dist/` removido)
- [ ] Dependências corretas
- [ ] Testado localmente
- [ ] Testado no TestPyPI
- [ ] Git tag criada (ex: `git tag v0.2.0`)
- [ ] Tag enviada ao GitHub (`git push origin v0.2.0`)

## Comandos Úteis

```bash
# Verificar o pacote antes de enviar
py -m twine check dist/*

# Ver informações do pacote wheel
py -m wheel metadata dist/caze_tools-*.whl

# Instalar localmente para testar
py -m pip install dist/caze_tools-*.whl

# Desinstalar
py -m pip uninstall caze-tools
```

## Solução de Problemas

### Erro: "File already exists"
O PyPI não permite sobrescrever versões. Você deve:
1. Incrementar a versão
2. Fazer novo build
3. Fazer upload novamente

### Erro de autenticação
- Verifique se seu username é `__token__` (ao usar token de API)
- Verifique se o token está correto e não expirou
- Tente usar `--verbose` para mais detalhes: `py -m twine upload --verbose dist/*`

### README não renderiza corretamente
- Certifique-se de que `readme = "README.md"` está no `pyproject.toml`
- Verifique se o README está válido em Markdown
- Use o PyPI Warehouse Preview para testar

## Referências

- [Packaging Python Projects (oficial)](https://packaging.python.org/tutorials/packaging-projects/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [PyPI Help](https://pypi.org/help/)
- [Semantic Versioning](https://semver.org/lang/pt-BR/)
