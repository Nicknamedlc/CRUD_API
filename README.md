# **Task Manager API**  

**Trabalho da Disciplina de Engenharia de Software: Arquitetura e Padrões**  
**Curso:** Ciência da Computação  
**Professor:** Cassia Nino
**Aluno:** João e Victorio (VictorioBF)  

---

## **📌 Visão Geral**  
Este projeto consiste em uma **API RESTful** para um sistema de gestão de tarefas colaborativas, desenvolvida em **Python com FastAPI**, seguindo os princípios de **Arquitetura de Software e Padrões de Projeto**. A aplicação permite que usuários criem, editem, atribuam e concluam tarefas, seguindo uma arquitetura **MVC (Model-View-Controller)** com camadas bem definidas para garantir **modularidade, desacoplamento e testabilidade**.  

---

## **📋 Funcionalidades**  
✔ **CRUD de Tarefas** (Criar, Ler, Atualizar, Deletar)  
✔ **Atribuição de Tarefas** a usuários  
✔ **Autenticação JWT** (JSON Web Tokens)  
✔ **Logs Estruturados** (com Uvicorn e loguru)  
✔ **Documentação Automatizada** (Swagger/OpenAPI)  
✔ **Testes Automatizados** (Unitários e de Integração, com pytest e ruff)  
✔ **Formatação de código automático** (formatação por padrões)  



---

## **🛠️ Arquitetura (MVC)**  
A API foi desenvolvida seguindo o padrão **MVC (Model-View-Controller)**, com as seguintes camadas:  

| Camada          | Descrição                                                                 | Exemplo de Componentes                          |  
|----------------|-------------------------------------------------------------------------|-----------------------------------------------|  
| **Model**      | Gerencia os dados e a lógica de negócio.                                | `Task`, `User`              |  
| **View**       | Responsável pela apresentação dos dados (JSON na API REST).             | FastAPI `Response`, Schemas          |  
| **Controller** | Intermediário entre Model e View, lidando com requisições HTTP.        | FastAPI `Router`, `TaskController`            |

---

## **📊 Diagramas da Arquitetura** *(Espaço para inserir os diagramas gerados)*  

### **1. Diagrama de Componentes**  
**User**
```mermaid
classDiagram
    class UserModel {
        +id: int
        +username: str
        +email: str
        +hashed_password: str
        +created_at: datetime
        +updated_at: datetime
    }

    class UserSchema {
        +username: str
        +email: EmailStr
        +password: str
    }

    class UserRoute {
        +create_user()
        +get_user()
        +update_user()
        +delete_user()
    }

    UserRoute --> UserSchema : Valida dados
    UserRoute --> UserModel : Salva/Consulta
    UserModel --> Database : Persistência
```
**Task**
```mermaid
classDiagram
    class TaskModel {
        +id: int
        +title: str
        +description: str
        +state: TaskState
        +user_id: int
    }

    class TaskSchema {
        +title: str
        +description: str
        +state: TaskState
    }

    class TaskRoute {
        +create_task()
        +list_tasks()
        +patch_task()
        +delete_task()
    }

    TaskRoute --> TaskSchema : Valida dados
    TaskRoute --> TaskModel : Salva/Consulta
    TaskModel --> Database : Persistência
    
    
    
```

### **2. Diagrama de Sequência (Fluxo de Criação de Usuário)**
```mermaid
sequenceDiagram
    participant Cliente
    participant API
    participant Serviço
    participant Repositório
    participant BancoDados

    Cliente->>API: POST /tasks (JSON)
    API->>Serviço: create_task(task_data)
    Serviço->>Repositório: save(task)
    Repositório->>BancoDados: INSERT
    BancoDados-->>Repositório: ID criado
    Repositório-->>Serviço: Task object
    Serviço->>Serviço: Validações/Regras
    Serviço-->>API: Task criada
    API-->>Cliente: 201 Created (JSON)
```

### **3. Diagrama de Banco de dados**
```mermaid
erDiagram
    USER {
        int id PK
        string username
        string email
        string password
        datetime created_at
        datetime updated_at
        int id_task FK
    }
    TASK {
        int id PK
        string title
        string description
        string state
        int user_id FK
    }

    USER ||--o{ TASK : "assignee"
 ```

## **⚙️ Configuração e Execução**  

### **Pré-requisitos**  
- Python 3.13+  
- SQLite  
- Poetry (gerenciamento de dependências)  

### **Instalação**  
```bash
# Clone o repositório
git clone https://github.com/Nicknamedlc/CRUD_API.git

# Instale as dependências
pip install poetry

poetry install CRUD_API

# Execute as migrações (Alembic)
alembic upgrade head

# Inicie a API
uvicorn app.main:app --reload --reload-delay 10
```

### **Acesse a Documentação**  
- **Swagger UI:** `http://localhost:8000/docs` (ao executar o projeto)

---

## **🧪 Testes**  
```bash
# Execute testes unitários
pytest tests/unit

# Execute testes de integração
pytest tests/integration

# com o uso do poetry
Poetry run task test 
```

---

## **📝 Padrões e Boas Práticas**  
✅ **Repository Pattern** (Separação clara entre lógica de negócio e acesso a dados)  
✅ **Injeção de Dependência** (Para melhor testabilidade)  
✅ **Logs Estruturados** (Facilitando monitoramento)  
✅ **Documentação Automatizada** (OpenAPI/Swagger)  

---

## **🔗 Vídeo Exemplo**
`https://drive.google.com/file/d/1p_sAB3nEtpJZXdOkljzRCBpYwHkR-JIB/view`

---

## **🔧 Como Testar os Endpoints**

1. Acesse a documentação interativa:
   ```
   http://localhost:8000/docs
   ```

2. Autentique-se primeiro via endpoint `/auth/login`

3. Use os exemplos de requisição fornecidos no Swagger UI

---

## **📌 Conclusão**  
Este projeto foi desenvolvido como parte da disciplina de **Engenharia de Software: Arquitetura e Padrões**, focando em **Arquitetura MVC e Padrões de Projeto**. A estrutura modular e a clara separação de responsabilidades facilitam a manutenção e a escalabilidade da aplicação.

---