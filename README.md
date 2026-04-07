# Tarefas

Aplicação Django para gerenciamento de tarefas (To-Do List).

## Descrição

Sistema simples de gerenciamento de tarefas com as funcionalidades de:
- Criar novas tarefas
- Editar tarefas existentes
- Marcar tarefas como completas
- Definir prazos para tarefas
- Visualizar todas as tarefas

## Requisitos

- Python 3.8+
- Django 4.0+
- pip

## Instalação

1. Clone ou baixe o repositório:
```bash
git clone <seu-repositorio-url>
cd tarefas
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute as migrações:
```bash
python manage.py migrate
```

6. Crie um superusuário (opcional):
```bash
python manage.py createsuperuser
```

## Uso

1. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

2. Acesse a aplicação em `http://localhost:8000`

3. Para acessar o painel administrativo: `http://localhost:8000/admin`

## Estrutura do Projeto

```
tarefas/
├── core/                    # Configurações principais do Django
│   ├── settings.py         # Configurações do projeto
│   ├── urls.py             # URLs principais
│   ├── views.py            # Views globais
│   └── static/             # Arquivos estáticos (CSS, JS, imagens)
│
├── tarefas/                # App principal de tarefas
│   ├── models.py           # Modelos de dados
│   ├── views.py            # Views das tarefas
│   ├── forms.py            # Formulários
│   ├── urls.py             # URLs da app
│   ├── admin.py            # Configuração do admin
│   └── templates/          # Templates HTML
│       ├── home.html
│       ├── adicionar.html
│       └── editar.html
│
├── manage.py               # Script de gerenciamento do Django
├── db.sqlite3              # Banco de dados SQLite
└── requirements.txt        # Dependências do projeto
```

## Funcionalidades

- **Adicionar Tarefas**: Crie novas tarefas com descrição e prazo
- **Editar Tarefas**: Modifique tarefas existentes
- **Marcar como Concluída**: Altere o status de conclusão
- **Listar Tarefas**: Visualize todas as tarefas

## Contribuindo

Sinta-se livre para fazer fork, abrir issues ou enviar pull requests.

## Licença

Este projeto é de código aberto e está disponível sob a licença MIT.
