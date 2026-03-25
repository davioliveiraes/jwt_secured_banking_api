# JWT Secured Banking API

API REST de gerenciamento bancário desenvolvida em Python com Flask, aplicando conceitos de autenticação JWT, criptografia de senhas com bcrypt e proteção de rotas.

## Finalidade

Este projeto tem como objetivo construir uma API bancária segura que permite o registro de usuários, autenticação via token JWT e operações de saldo protegidas. A aplicação demonstra na prática como implementar:

- Autenticação e autorização com JSON Web Tokens (JWT)
- Criptografia de senhas utilizando bcrypt com salt
- Middleware de proteção de rotas para endpoints sensíveis
- Validação de permissões por usuário (um usuário só pode alterar seu próprio saldo)
- Tratamento centralizado de erros HTTP

### Endpoints

| Método | Rota | Autenticação | Descrição |
|--------|------|:------------:|-----------|
| POST | `/bank/registry` | Não | Registro de novo usuário |
| POST | `/bank/login` | Não | Login e geração do token JWT |
| PATCH | `/bank/balance/<user_id>` | Sim | Atualização de saldo do usuário |

## Tecnologias Utilizadas

- **Python 3.13** — Linguagem principal
- **Flask 3.1** — Framework web para criação de rotas e servidor HTTP
- **PyJWT 2.10** — Geração e validação de tokens JWT (algoritmo HS256)
- **bcrypt 5.0** — Hash de senhas com salt automático
- **SQLite3** — Banco de dados relacional embutido
- **python-dotenv 1.2** — Carregamento de variáveis de ambiente via `.env`
- **pytest 9.0** — Framework de testes unitários

## Como Executar

### Pré-requisitos

- Python 3.10+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/davioliveiraes/jwt_secured_banking_api.git
cd jwt_secured_banking_api

# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
KEY=sua_chave_secreta
ALGORITHM=HS256
JWT_HOURS=10
```

### Inicialização do banco de dados

```bash
sqlite3 storage.db < init/schema.sql
```

### Executando a aplicação

```bash
python run.py
```

O servidor será iniciado em `http://localhost:3000`.

### Executando os testes

```bash
pytest
```

## Conceitos Aprendidos

### Autenticação com JWT

Implementação completa do fluxo de autenticação baseado em tokens: o usuário realiza login com credenciais válidas e recebe um token JWT assinado com chave secreta (HS256) e tempo de expiração configurável. Esse token deve ser enviado no header `Authorization` nas requisições protegidas.

### Criptografia de Senhas com bcrypt

As senhas nunca são armazenadas em texto puro. Utilizando bcrypt, cada senha é transformada em um hash com salt aleatório antes de ser persistida no banco, tornando inviável a recuperação da senha original mesmo em caso de vazamento do banco de dados.

### Middleware de Proteção de Rotas

Criação de um middleware que intercepta requisições em rotas protegidas, extrai o token JWT do header `Authorization`, valida sua autenticidade e verifica se o `user_id` do token corresponde ao usuário da requisição, garantindo que cada usuário só acesse seus próprios recursos.

### Arquitetura Limpa e Padrão Composer

O projeto segue princípios de Clean Architecture com separação em camadas (Routes → Views → Controllers → Repositories → Drivers) e utiliza o padrão Composer para injeção de dependências, facilitando a testabilidade e manutenção do código.

### Tratamento Centralizado de Erros

Erros HTTP customizados (`400 Bad Request`, `401 Unauthorized`, `404 Not Found`) são tratados de forma centralizada com respostas padronizadas em JSON, proporcionando uma API consistente e previsível.

### Testes Unitários

Cobertura de testes em todas as camadas da aplicação utilizando pytest, com uso de mocks para isolar dependências e validar comportamentos individuais de cada componente.

## Referências

- [Flask — Documentação Oficial](https://flask.palletsprojects.com/)
- [PyJWT — Documentação Oficial](https://pyjwt.readthedocs.io/)
- [bcrypt — PyPI](https://pypi.org/project/bcrypt/)
- [JWT.io — Introdução ao JSON Web Token](https://jwt.io/introduction)
- [OWASP — Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [OWASP — Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Clean Architecture — Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
