# Lista de Tarefas

Este projeto é uma aplicação simples de lista de tarefas, desenvolvida com uma estrutura modularizada para facilitar a reutilização do código.

## Tecnologias Utilizadas

- Backend: FastAPI
- Banco de Dados: OracleDB
- Frontend: HTML5

## Como Executar o Projeto

Para rodar este projeto localmente, siga os passos abaixo:

### Criar um ambiente virtual
```
python -m venv venv
```

### Ativar o ambiente virtual
```
venv\Scripts\activate
```

### Instalar as dependências
```
pip install -r requirements.txt
```

requirements.txt é a lista de dependências necessárias para o projeto.

### Criar o arquivo .env
Na raiz do projeto, crie um arquivo chamado .env e adicione as seguintes informações:

```
ORACLE_USER=seu_nome
ORACLE_PASSWORD=sua_senha
ORACLE_DSN=seu_localhost
```

Exemplo de ORACLE_DSN: localhost:1234/xepdb1 ou xe.

### Executar o projeto
```
python main.py
```

Isso inicializará a API e a aplicação estará pronta para uso.

## Estrutura do Projeto

```
.
├── main.py                # Arquivo principal que inicia a aplicação
├── models/                # Definições das tabelas e conexões com o banco de dados
├── routes/                # Definição das rotas do FastAPI
├── templates/             # Arquivos HTML para o frontend
├── controller/            # Funções responsáveis por interagir com o modelo de dados
└── .env                   # Arquivo com credenciais do banco de dados (não incluso no repositório por segurança)
```

## Importante

Qualquer usuário que deseje rodar este projeto precisa ter uma conta no Oracle Database e configurar corretamente o .env.
