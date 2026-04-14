# FastAPI Project (Python 3.14.2) 🚀

## Luizalabs_Backend_python

Bootcamp da dio com o objetivo introdutorio do Python no backend

Fundamentos de API REST no Python.

Este guia foca no fluxo **Pyenv + Poetry + FastAPI** contornando os bloqueios de execução de scripts.

---

Este projeto utiliza **FastAPI** com gerenciamento de dependências via **Poetry** e controle de versões Python através do **Pyenv**.

## 📋 Pré-requisitos

1. **Pyenv-win**: Instalado e configurado no Path do Windows.
2. **Poetry**: Instalado (recomenda-se via instalador oficial ou `pipx`).
3. **Python 3.14.2**: Instalado via pyenv.

---

## 🛠️ Configuração do Ambiente

### 1. Definir a versão do Python

Dentro da pasta do projeto (`...\Luizalabs_Backend_python\dio_blog`), defina a versão local para garantir que o Pyenv use a correta:

```powershell
pyenv local 3.14.2
```

### 2. Configurar o Poetry

Para evitar que o Poetry tente usar o Python do sistema, force-o a olhar para a versão ativa do Pyenv e (opcionalmente) criar o ambiente virtual dentro do projeto:

```powershell
poetry config virtualenvs.in-project true
poetry env use $(pyenv which python)
```

### 3. Instalar Dependências

Inicie o projeto e adicione o FastAPI e o Uvicorn:

```powershell
# Inicia o arquivo de configuração (se ainda não existir)
poetry init -n

# Adiciona as dependências principais
poetry add fastapi "uvicorn[standard]"
```

---

## 💻 Estrutura do Projeto

Certifique-se de que o arquivo `main.py` está na raiz do diretório para facilitar a execução:

**`main.py`**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "python_version": "3.14.2",
        "message": "FastAPI rodando com Poetry e Pyenv"
    }
```

---

## 🚀 Como Executar o Servidor

Devido às políticas de segurança do **Device Guard**, o executável direto do uvicorn (`uvicorn.exe`) pode ser bloqueado. A forma correta e segura de rodar o servidor é chamando-o como um módulo do Python:

```powershell
poetry run python -m uvicorn main:app --reload
```

* **`poetry run`**: Garante que o Python do ambiente virtual seja usado.
* **`python -m uvicorn`**: Executa o Uvicorn como módulo (contorna o bloqueio de `.exe` não assinados).
* **`main:app`**: Indica o arquivo `main.py` e a instância `app` do FastAPI.
* **`--reload`**: Reinicia o servidor automaticamente a cada alteração no código.

---

## 🔍 Solução de Problemas Comuns

| Erro | Solução |
| :--- | :--- |
| `Device Guard bloqueou...` | Use sempre `python -m uvicorn` em vez de apenas `uvicorn`. |
| `Could not import module "main"` | Verifique se você está na pasta raiz e se o arquivo se chama `main.py`. |
| `Virtualenvs.prefer-active-python` não existe | Use `poetry env use $(pyenv which python)` para vincular a versão manualmente. |
| Erro de Scripts no PowerShell | Execute: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` (como Admin). |

---

## 📡 Endpoints Úteis

* **API**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
* **Documentação (Swagger)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **Documentação Alternativa (Redoc)**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
