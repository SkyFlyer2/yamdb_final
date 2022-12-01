# API YaMDB
![yamdb_workflow](https://github.com/SkyFlyer2/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

Сервис  "YaMDB" - портал о фильмах, книгах и музыке, где пользователи могут оценивать и комментировать произведения.
Создано в рамках курса Яндекс.Практикум.

# Описание проекта

yamdb_final - заключительный проект курса "Python-разработчик" на Яндекс.Практикум. Реализована методика разработки CI/CD (Continuos Integration/Continuos Delivery).

## Ссылка на сайт
Сервис запущен по [адресу](http://158.160.4.20/redoc/)


## Технологии
* Python 3.8
* Django 2.2
* Django REST Framework 2.2.16
* SimpleJWT
* python-dotenv
* git
* PostreSQL
* Nginx
* gunicorn
* Docker
* DockerHub

## Порядок действий для развертывания и запуска сервиса:

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/SkyFlyer2/yamdb_final.git
```

Выполните вход на удаленный сервер
Установка docker:

```
sudo apt install docker.io
```

или

```
curl -fsSL https://get.docker.com -o get-docker.sh
DRY_RUN=1 sudo sh ./get-docker.sh
```

Установка docker-compose:
sudo apt-get install docker-compose-plugin

В файле infra/nginx.conf пропишите IP-адрес сервера:

```
server_name xxx.xxx.xxx.xxx;
```

Из каталога infra скопируйте на удаленный сервер файлы  docker-compose.yml и default.conf.

scp docker-compose.yml <username>@<host>:/home/<username>/docker-compose.yml
scp -r default.conf <username>@<host>:/home/<username>/nginx/default.conf


Cоздайте файл ```.env```:

```bash 
touch .env
```

Заполните ```.env``` файл переменными окружения по примеру:
```bash 
echo SECRET_KEY=<уникальный токен> >> .env
echo DB_ENGINE=django.db.backends.postgresql >> .env
echo DB_NAME=<название базы данных postgre sql> l >> .env
echo POSTGRES_USER=<имя пользователя>  >> .env
echo POSTGRES_PASSWORD=<ваш пароль> >> .env
echo DB_HOST=db  >> .env
echo DB_PORT=5432  >> .env
```

Теперь можно установить и запустить приложение в контейнерах (контейнер web загружается из DockerHub):
```bash 
sudo docker-compose up -d
```

Запуск миграций, создание суперюзера, сбор статики и заполнение БД:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input 

docker-compose exec web python manage.py loaddata fixtures.json
```
___________________________________

Проект доступен по адресу `http://<IP адрес сервера>/`

Документация по API `http://<IP адрес сервера>/redoc/`


**Примеры API-запросов**

* Запросы для всех пользователей

curl -H 'Accept: application/json' `http://<IP адрес сервера>/api/v1/titles/` - получить список всех произведений

curl -H 'Accept: application/json' `http://<IP адрес сервера>/api/v1/categories/` - получить список категорий

curl -H 'Accept: application/json' `http://<IP адрес сервера>/api/v1/genres/` - получить список жанров

curl -H 'Accept: application/json' `http://<IP адрес сервера>/api/v1/comments/` - получить список всех комментариев к записи


**Аутентификация:**

* Создать учетную запись:

curl --header "Content-Type: application/json" --request POST --data '{"username":"username","email":"email@email"}' `http://<IP адрес сервера>/api/v1/auth/signup/`

* После создания записи вы получите код подтверждения, по которому можно получить токен для авторизации:

curl --header "Content-Type: application/json" --request POST --data '{"username":"username","email":"email@email", "confirmation_code":"your_code"}' `http://<IP адрес сервера>/api/v1/auth/token/`
