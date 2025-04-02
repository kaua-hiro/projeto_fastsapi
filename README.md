# Lista de Tarefas
Este projeto consiste em uma aplicação simples para gerenciamento de tarefas, desenvolvida com uma arquitetura modular para promover a reutilização de código.

Tecnologias Utilizadas
Backend: FastAPI

Banco de Dados: OracleDB

Frontend: HTML5

Como Executar o Projeto
Para rodar o projeto localmente, siga as etapas abaixo:

1. Criar e ativar um ambiente virtual
bash

python -m venv venv  
# No Windows  
venv\Scripts\activate  
# No macOS/Linux  
source venv/bin/activate  
2. Instalar as dependências
bash

pip install -r requirements.txt  
O arquivo requirements.txt contém todas as bibliotecas necessárias para a execução do projeto.

3. Criar o arquivo .env
Na raiz do projeto, crie um arquivo chamado .env e adicione as credenciais do banco de dados:

ini

ORACLE_USER=seu_usuario  
ORACLE_PASSWORD=sua_senha  
ORACLE_DSN=seu_host  
Exemplo de ORACLE_DSN: localhost:1234/xepdb1 ou xe.

4. Executar a aplicação
bash

python main.py  
Após isso, a API estará disponível para uso.

Estrutura do Projeto
bash

.
├── main.py                # Arquivo principal que inicia a aplicação

├── models/                # Definição das tabelas e conexões com o banco de dados

├── routes/                # Endpoints da API (FastAPI)

├── templates/             # Arquivos HTML utilizados no frontend

├── controller/            # Lógica de interação com os modelos de dados

└── .env                   # Configuração do banco de dados (excluído do repositório por segurança)


# Observação
Para utilizar este projeto, é necessário ter uma conta no Oracle Database e configurar corretamente o arquivo .env.
