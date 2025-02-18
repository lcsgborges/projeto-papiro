# Projeto Papiro Notas

## Objetivos:
<p>Desenvolver uma aplicação web para gerenciar notas de forma fácil e intuitiva.</p>

## Ferramentas e Linguagens:

<div style=background-color: white;>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-plain.svg" align="center" heigth="50" width="60">

  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain-wordmark.svg" align="center" heigth="50" width="60">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original.svg" align="center" heigth="50" width="60">
</div>

## Como contribuir:
1. Clone o repositório:
```
git clone https://github.com/lcsgborges/projeto-papiro.git
cd nome-do-repositorio
```

2. Crie um ambiente virtual:
```
python3 -m venv venv
source venv/bin/activate # linux/mac
venv\Scripts\activate    # windows    
```
3. Instale as dependências:
```pip install -r requirements.txt```

4. Faça as migraçoes do banco de dados:
```python manage.py migrate```

5. Inicie o servidor (na pasta em que se encontra o arquivo manage.py):
```python manage.py runserver```
