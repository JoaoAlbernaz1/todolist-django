# Todo List com Django

Este é um projeto de um sistema de gerenciamento de tarefas (Todo List) desenvolvido com o framework Django. Ele permite aos usuários criar, editar, atualizar e deletar tarefas de forma organizada e intuitiva.

## 🚀 Funcionalidades

- **Criar Tarefas:** Adicione novas tarefas com título, descrição, prioridade e data de vencimento.
- **Editar Tarefas:** Modifique qualquer informação de uma tarefa existente.
- **Deletar Tarefas:** Remova tarefas com uma tela de confirmação segura.
- **Marcar como Concluída:** Altere o status de uma tarefa de pendente para concluída e vice-versa.
- **Interface Moderna:** Interface limpa, organizada e responsiva, desenvolvida com Bootstrap 5.
- **Sistema de Prioridades:** Classifique tarefas como Baixa, Média ou Alta.
- **Status de Tarefas:** Acompanhe o progresso com status de Pendente, Em Progresso, Concluída ou Cancelada.

## 🛠️ Tecnologias Utilizadas

- **Backend:**
  - Python 3
  - Django 4+
  - SQLite3 (banco de dados padrão)

- **Frontend:**
  - HTML5
  - CSS3
  - Bootstrap 5
  - Bootstrap Icons

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para executar o projeto em sua máquina.

### Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

### 1. Clone o Repositório

```bash
git clone https://github.com/JoaoAlbernaz1/todolist-django.git
cd todolist-django
```

### 2. Crie um Ambiente Virtual (Recomendado)

#### **No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

#### **No macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

> **Observação:** No Windows, use o terminal `cmd` ou `PowerShell`. No PowerShell, talvez precise rodar `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` uma vez antes de ativar o ambiente virtual.

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Aplique as Migrações do Banco de Dados

```bash
python manage.py migrate
```

### 5. Crie um Superusuário (Opcional)

```bash
python manage.py createsuperuser
```
Siga as instruções para definir nome de usuário, email e senha.

### 6. Inicie o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

### 7. Acesse a Aplicação

- **Página Principal:** Abra seu navegador e acesse [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Painel Admin:** Acesse [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📝 Estrutura do Projeto

- `todolist/`: Contém as configurações principais do projeto Django (`settings.py`, `urls.py`).
- `tasks/`: A aplicação principal que gerencia as tarefas.
  - `models.py`: Define a estrutura da tabela de tarefas no banco de dados.
  - `views.py`: Contém a lógica de negócio (o que acontece quando uma URL é acessada).
  - `forms.py`: Define os formulários de criação e edição de tarefas.
  - `urls.py`: Mapeia as URLs específicas do app de tarefas para as views.
  - `templates/`: Armazena os arquivos HTML da aplicação.
  - `admin.py`: Customiza como as tarefas são exibidas no painel de admin.
- `db.sqlite3`: O arquivo do banco de dados SQLite.
- `manage.py`: O utilitário de linha de comando do Django. 