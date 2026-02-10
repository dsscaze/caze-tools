# Publicação Rápida no PyPI

Guia rápido para publicar uma nova versão do `caze-tools` no PyPI.

## Preparação (primeira vez)

```bash
# Instalar ferramentas
py -m pip install --upgrade build twine

# Criar conta em https://pypi.org/account/register/
# Criar token de API em https://pypi.org/manage/account/token/
```

## Publicar Nova Versão

### 1. Atualizar Versão

Edite os arquivos e atualize a versão (ex: de 0.2.0 para 0.2.1):
- `pyproject.toml`: linha `version = "0.2.1"`
- `setup.py`: linha `version="0.2.1"`
- `CHANGELOG.md`: adicione seção com mudanças

### 2. Commit e Tag

```bash
git add .
git commit -m "Atualiza versão para 0.2.1"
git tag v0.2.1
git push origin main --tags
```

### 3. Build e Upload

```bash
# Limpar builds anteriores
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue

# Criar pacote
py -m build

# Verificar pacote
py -m twine check dist/*

# Enviar para PyPI
py -m twine upload dist/*
```

Quando solicitado:
- **Username**: `__token__`
- **Password**: seu token de API (começa com `pypi-`)

### 4. Verificar

```bash
# Testar instalação
pip install --upgrade caze-tools

# Verificar comando
cz --help
```

Pronto! 🎉

---

Para mais detalhes, consulte o [Guia Completo de Publicação](publicacao-pypi.md).
