# Preparando o Ambiente

Como preparar o ambiente para o Workshop

## se você ainda não tem Python 3.6 instale

Verifique se possui o python 3.6 executanto:

```bash
python3.6 -V
```

Se não estiver instalado então neste link pode fazer o download: https://www.python.org/downloads/


## crie um diretorio para o nosso projeto

```bash
cd YOUR_PROJECTS_FOLDER
mkdir flask_workshop
```

ou se preferir faça clone do repositório:

```bash
git clone https://github.com/cursodepythonoficial/flask_workshop.git

```

> no windows dependendo da versão o comando para criar diretórios é o `md` ex: `md flask_workshop`, mas se preferir pode fazer via windows explorer.

## Agora crie um ambiente virtual para o projeto

```bash
cd flask_workshop
python3.6 -m venv env
```

## Ative o ambiente virtual

```bash
source env/bin/activate
```

## Instale os pacotes que usaremos no workshop

```bash
pip3 install flask flask-admin tinydb tinymongo pymongo flask-admin ipython ipdb flask-debugtoolbar flask-wtf flask-classy flask-shell-ipython pytest-flask gunicorn
```

ou execute

```bash
pip install -r requirements.txt
```

## Verifique que a instalação está ok

```bash
flask --help
```



## Editor

Você pode usar o editor de códigos ou IDE que preferir, no workshop eu usarei o VSCode, se quiser pode instalar em: https://code.visualstudio.com/ e a extensão que adiciona suporte a Python é: https://marketplace.visualstudio.com/items?itemName=donjayamanne.python
