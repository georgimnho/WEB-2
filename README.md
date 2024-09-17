# Projeto de Gerenciamento de Tarefas

## Visão Geral

Este projeto tem como objetivo fornecer uma plataforma robusta para criação, gerenciamento e acompanhamento de tarefas. As APIs desenvolvidas permitem organizar e priorizar tarefas de forma eficiente, tornando o controle das atividades mais ágil e acessível. O projeto é construído utilizando o *Django REST Framework*, com três principais APIs: **Tarefas**, **Categorias** e **Prioridades**.

## Funcionalidades Principais

### 1. API de Tarefas
Responsável por gerenciar as tarefas que os usuários precisam realizar, oferecendo funcionalidades completas de CRUD (criação, leitura, atualização e exclusão).

- **Endpoints:**
  - `GET/POST /api/tasks/`: Cria uma nova tarefa ou lista todas as tarefas existentes.
  - `GET/PUT/DELETE /api/tasks/{id}/`: Visualiza, edita ou deleta uma tarefa específica.
  - `GET /api/tasks/user/{user_id}/`: Lista todas as tarefas de um usuário específico.

### 2. API de Categorias
Permite a organização das tarefas em diferentes categorias, como "Trabalho", "Estudos" ou "Pessoal".

- **Endpoints:**
  - `GET/POST /api/categories/`: Lista ou cria novas categorias de tarefas.
  - `GET/PUT/DELETE /api/categories/{id}/`: Visualiza, edita ou deleta uma categoria específica.
  - `GET /api/categories/{id}/tasks/`: Lista todas as tarefas relacionadas a uma categoria específica.

### 3. API de Prioridades
Define e gerencia os níveis de prioridade das tarefas, classificando-as como "Baixa", "Média" ou "Alta".

- **Endpoints:**
  - `GET/POST /api/priorities/`: Lista ou cria novos níveis de prioridade.
  - `GET/PUT/DELETE /api/priorities/{id}/`: Visualiza, edita ou deleta um nível de prioridade.
  - `GET /api/priorities/{id}/tasks/`: Lista todas as tarefas com um determinado nível de prioridade.

## Estrutura do Projeto

Este projeto segue a arquitetura *Model-View-Set* típica do Django REST Framework, garantindo separação de responsabilidades e facilidade de manutenção.

### 1. API de Tarefas
- **ViewSet:** `TaskViewSet` gerencia o CRUD de tarefas.
- **Relacionamento:** Cada tarefa é vinculada a uma categoria e a um nível de prioridade, permitindo organização e hierarquização.
  
### 2. API de Categorias
- **ViewSet:** `CategoryViewSet` gerencia as operações relacionadas às categorias de tarefas.
- **Filtro:** Possibilidade de listar tarefas filtradas por uma categoria específica.

### 3. API de Prioridades
- **ViewSet:** `PriorityViewSet` gerencia as operações relacionadas aos níveis de prioridade.
- **Filtro:** As tarefas podem ser filtradas pelo nível de prioridade.

## Tecnologias Utilizadas
- **Linguagem:** Python
- **Framework:** Django e Django REST Framework
- **Banco de Dados:** PostgreSQL 
- **Autenticação:** Autenticação JWT
  
## Instalação e Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu_usuario/projeto-gerenciamento-tarefas.git

2. Crie e ative o ambiente virtual:
   **No Windows:** .\venv\Scripts\activate
   **No Linux:**  source meu_ambiente_virtual/bin/activate

3. Instale as dependências:
    `pip install -r requirements.txt`

4. Execute as migrações do banco de dados:
    `python manage.py migrate`

5. Inicie o servidor de desenvolvimento:
    `python manage.py runserver`

    


