# 🎴 Sticker Album API

API REST desenvolvida em **Python** com **FastAPI** para gerenciamento de um álbum de figurinhas, incluindo autenticação JWT, controle de usuários, gerenciamento completo das figurinhas e ambiente totalmente **dockerizado**.

---

# ✨ Funcionalidades

## 🔐 Autenticação

- Cadastro de usuários
- Login utilizando JWT
- Login compatível com OAuth2
- Refresh Token
- Rotas protegidas por autenticação

## 🎴 Gerenciamento de Figurinhas

- Adicionar figurinhas ao álbum
- Atualização automática da quantidade de figurinhas repetidas
- Remover figurinhas
- Consultar figurinhas específicas
- Listagem completa do álbum
- Listagem de figurinhas repetidas
- Cálculo automático do progresso do álbum

## 🗄 Banco de Dados

- PostgreSQL
- SQLAlchemy ORM
- Migrações com Alembic

## 🐳 Docker

- Aplicação totalmente dockerizada
- Banco de dados PostgreSQL em container
- Orquestração com Docker Compose
- Ambiente padronizado para desenvolvimento e execução

---

# 🛠 Tecnologias Utilizadas

- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- JWT (python-jose)
- Passlib + Bcrypt
- Uvicorn
- Python Dotenv
- Docker
- Docker Compose

---

# 📂 Estrutura do Projeto

```text
.
├── alembic/
├── app/
│   ├── routers/
│   │   ├── auth_routes.py
│   │   └── figurinha_routes.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# 🚀 Instalação

## 1. Clone o repositório

```bash
git clone https://github.com/Guipassarim0/album-figurinhas-api.git

cd album-figurinhas-api
```

---

# ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto utilizando o `.env.example` como base.

### Linux / macOS

```bash
cp .env.example .env
```

### Windows (PowerShell)

```powershell
Copy-Item .env.example .env
```

Edite o arquivo `.env` com as configurações desejadas.

Exemplo:

```env
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=db
DB_PORT=5432
DB_NAME=album_db

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> **Importante**
>
> - Ao utilizar **Docker Compose**, mantenha `DB_HOST=db`.
> - Ao executar a aplicação localmente, altere `DB_HOST=localhost`.

---

# 🐳 Executando com Docker (Recomendado)

## Construir as imagens

```bash
docker compose build
```

## Iniciar os containers

```bash
docker compose up -d
```

## Executar as migrações

```bash
docker compose exec api alembic upgrade head
```

A aplicação ficará disponível em:

```
http://localhost:8000
```

Swagger:

```
http://localhost:8000/docs
```

ReDoc:

```
http://localhost:8000/redoc
```

---

# 💻 Executando Localmente (sem Docker)

## Criar ambiente virtual

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

## Instalar dependências

```bash
pip install -r requirements.txt
```

## Configurar o arquivo `.env`

Altere apenas o host do banco:

```env
DB_HOST=localhost
```

## Executar as migrações

```bash
alembic upgrade head
```

## Iniciar a API

```bash
uvicorn app.main:app --reload
```

---

# 🔐 Endpoints de Autenticação

## Criar Conta

**POST** `/auth/criar_conta`

### Exemplo

```json
{
  "nome": "Guilherme",
  "email": "guilherme@email.com",
  "senha": "123456"
}
```

---

## Login

**POST** `/auth/login`

### Exemplo

```json
{
  "email": "guilherme@email.com",
  "senha": "123456"
}
```

### Resposta

```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "Bearer"
}
```

---

## Login OAuth2

**POST** `/auth/login_form`

---

## Refresh Token

**GET** `/auth/refresh`

---

# 🎴 Endpoints de Figurinhas

Todas as rotas abaixo exigem autenticação JWT.

---

## Listar Figurinhas

**GET** `/figurinhas/listar`

### Resposta

```json
[
  {
    "sigla": "BRA",
    "numero": 10,
    "quantidade": 2,
    "observacao": "Neymar"
  }
]
```

---

## Adicionar Figurinha

**POST** `/figurinhas/criar_figurinha`

```json
{
  "sigla": "BRA",
  "numero": 10,
  "quantidade": 1,
  "observacao": "Neymar"
}
```

---

## Remover Figurinha

**POST** `/figurinhas/remover_figurinha`

```json
{
  "sigla": "BRA",
  "numero": 10,
  "quantidade": 1
}
```

---

## Consultar Figurinha

**GET** `/figurinhas/{sigla}/{numero}`

Exemplo:

```
/figurinhas/BRA/10
```

---

## Figurinhas Repetidas

**GET** `/figurinhas/repetidas`

---

## Progresso do Álbum

**GET** `/figurinhas/progresso`

### Resposta

```json
{
  "figurinhas": 450,
  "total_album": 980,
  "progresso_percentual": 45.92
}
```

---

# 🔒 Autenticação

As rotas protegidas utilizam autenticação JWT.

Inclua o token no cabeçalho da requisição:

```http
Authorization: Bearer SEU_TOKEN
```

---

# 📈 Melhorias Futuras

- Testes automatizados
- Paginação de resultados
- Cache com Redis
- Deploy em nuvem
- CI/CD com GitHub Actions
- Monitoramento e observabilidade

---

# 👨‍💻 Autor

**Guilherme Passarim**

Projeto desenvolvido para fins de estudo e prática de desenvolvimento Backend utilizando **FastAPI**, **SQLAlchemy**, **PostgreSQL**, **Alembic**, **JWT** e **Docker**.