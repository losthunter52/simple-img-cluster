## SIMPLE-IMG-CLUSTER

Projeto simples para realizar a clusterização de imagens utilizando sklearn e django

## Para Rodar o Projeto:

certifique-se que está na raiz do repositorio "[...]/simple-img-cluster/"

1 - crie e rode uma venv
```bash
  python -m venv venv
  venv/scripts/activate
```

2 - instale o pip e os requirements
```bash
  python -m pip install --upgrade pip
  pip install -r requirements.txt
```

3 - inicialize o banco de dados e os arquivos estaticos
```bash
  cd app
  python manage.py makemigrations
  python manage.py migrate
  python manage.py collectstatic
```

4 - Crie uma secret key para o arquivo settings.py
```bash
  SECRET_KEY = "coloque a secret key aqui"
```

5 - Rode o projeto
```bash
  python manage.py runserver
```

6 - Teste o projeto: http://127.0.0.1:8000/