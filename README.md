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

Perfeito, Caio! Esse é um ponto essencial para o trabalho em equipe ou para quando você precisar baixar o projeto em outra máquina. Como o seu ambiente tem a particularidade do **Device Guard**, incluí o comando de execução seguro.

Aqui está o complemento para o seu **README.md**:

---

## 📥 Clonando e Iniciando o Projeto

Se você acabou de clonar este repositório, siga estes passos para configurar o ambiente e rodar a aplicação:

### 1. Configure a versão do Python (Pyenv)

Certifique-se de ter a versão 3.14.2 instalada. Caso não tenha, instale com `pyenv install 3.14.2`.

```powershell
pyenv local 3.14.2
```

### 2. Prepare o ambiente virtual e instale as dependências

Com o Poetry instalado, execute o comando abaixo. Ele lerá o arquivo `pyproject.toml`, criará o ambiente virtual e instalará todas as bibliotecas necessárias (incluindo as versões exatas do `poetry.lock`):

```powershell
# Garante que o Poetry usará o Python do pyenv
poetry env use $(pyenv which python)

# Instala todas as dependências
poetry install
```

### 3. Executando a API

Para evitar bloqueios de segurança do Windows (Device Guard) e garantir que todas as dependências sejam carregadas corretamente, inicie o servidor com:

```powershell
poetry run python -m uvicorn main:app --reload
```

ou
Para rodar o projeto com a nova estrutura em `src/`:

```powershell
poetry run python -m uvicorn src.main:app --reload
```

---

### 4.💡 Comandos Rápidos de Verificação

Se quiser confirmar se tudo foi instalado corretamente após o clone:

* **Verificar ambiente ativo:** `poetry env info`
* **Verificar pacotes instalados:** `poetry show`
* **Verificar se o Python é o correto:** `poetry run python --version` (Deve retornar 3.14.2)

---

### 5. Dica para o VS Code

Agora que o código está em `src`, o VS Code pode se confundir com os caminhos.

1. Abra as configurações (`Ctrl + ,`).
2. Procure por **"Python Analysis Extra Paths"**.
3. Adicione `./src`.

Isso vai garantir que o IntelliSense continue encontrando seus `controllers` e `models` sem sublinhados vermelhos chatos.

**Dica para o Git:** Lembre-se de nunca subir a pasta `.venv` para o seu repositório. O seu arquivo `.gitignore` deve conter:

```text
.venv/
__pycache__/
*.py[cod]
.python-version
```

### 💡  Dicas de Desenvolvimento

#### 🛠️ Configurando o VS Code

Se estiver usando o VS Code, é essencial apontar para o ambiente virtual correto para que o autocomplete (IntelliSense) funcione:

Aperte ```Ctrl + Shift + P```.

Digite "```Python: Select Interpreter```".

Selecione o interpretador que está no caminho do seu projeto: ```.\.venv\Scripts\python.exe```.

#### 📦 Gerenciando Dependências

Listar pacotes: ```poetry show```

Ver árvore de dependências: ```poetry show --tree```

Adicionar novo pacote: ```bash poetry add <nome-do-pacote>```
