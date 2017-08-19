# Flask Workshop - pt1

python pt1/app.py
export FLASK_APP=pt1/app.py
flask run
flask shell


## deploy

```bash
docker build -t myflask .
```

## run

```bash
docker run --name myflask -d -p 80:80 myflask
```

## access

```bash
docker exec -t -i myflask  /bin/bash
```


## Existing Docker image
```bash
docker pull cursodepython/flask_workshop
```

```bash
docker run --name myflask -d -p 80:80 cursodepython/flask_workshop
docker exec -t -i myflask  /bin/bash
```

https://hub.docker.com/r/cursodepython/flask_workshop/


## referencias

https://github.com/rehabstudio/docker-gunicorn-nginx
https://paulohrpinheiro.xyz/texts/python/2016-11-30-flask-esqueletico.html
