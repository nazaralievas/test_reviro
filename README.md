Это тестовое задание от Reviro: простая система управления инвентаризацией продукции с реализацией CRUD продуктов и предприятий,
написанная на фреймовре django-rest с использованием Docker.

Инструкция по запуску:

1. Клонируйте репозиторий на локальную машину:
 git clone https://github.com/nazaralievas/test_reviro.git

2. Перейдите в директорию проекта:
 cd test_reviro

3. Запустите Docker Desktop

4. в терминале выполните команду:
 docker-compose build

5. запустите миграции:
docker-compose run --rm web-app sh -c "python manage.py migrate"

6. создайте суперюзера:
 docker-compose run --rm web-app sh -c "python manage.py createsuperuser"

7. запустите приложение с помощью команды:
 docker-compose up

8. при успешном запуске, по адресу http://localhost:8000/ вы увидите основные API-эндпоинты, однако более детальную информацию можете получить по адресу
 http://localhost:8000/swagger/
