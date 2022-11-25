# API YaMDB

Сервис  "YaMDB" - портал о фильмах, книгах и музыке, где пользователи могут оценивать и комментировать произведения.
Создано в рамках курса Яндекс.Практикум.

# Описание проекта

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

## Как запустить проект:

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/SkyFlyer2/infra_sp2.git
```

Cоздайте файл ```.env```:
```bash 
cd infra

touch .env
```

Заполните ```.env``` файл переменными окружения по примеру:
```bash 
echo DB_ENGINE=django.db.backends.postgresql >> .env

echo DB_NAME=postgres l >> .env

echo POSTGRES_PASSWORD=postgres >> .env

echo POSTGRES_USER=postgres  >> .env

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

Проект доступен по адресу `http://localhost/`

Документация по API `http://localhost:8000/redoc/`


**Примеры API-запросов**

* Запросы для всех пользователей

curl -H 'Accept: application/json' `http://127.0.0.1:8000/api/v1/titles/` - получить список всех произведений

curl -H 'Accept: application/json' `http://127.0.0.1:8000/api/v1/categories/` - получить список категорий

curl -H 'Accept: application/json' `http://127.0.0.1:8000/api/v1/genres/` - получить список жанров

curl -H 'Accept: application/json' `http://127.0.0.1:8000/api/v1/comments/` - получить список всех комментариев к записи


**Аутентификация:**

* Создать учетную запись:

curl --header "Content-Type: application/json" --request POST --data '{"username":"username","email":"email@email.com"}' `http://localhost:8000/api/v1/auth/signup/`

* После создания записи вы получите код подтверждения, по которому можно получить токен для авторизации:

curl --header "Content-Type: application/json" --request POST --data '{"username":"username","email":"email@email.com", "confirmation_code":"your_code"}' `http://localhost:8000/api/v1/auth/token/`
