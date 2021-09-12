Для запуска сервиса выполнить следующие шаги:

### Добавить для запуска файлы .env в sqlite_to_postgres и movies_admin/config/settings
Пример env:
В папке sqlite_to_postgres - POSTGRES_HOST=localhost
```
SECRET_KEY=django-insecure-k_e0gw#vs2j+&*ey8ptu@*sxrc!rm*4njr2pc4-s=rg8ix+$0p
HOSTNAME=127.0.0.1
ENGINE=django.db.backends.postgresql
POSTGRES_DB=movies
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=ma_postgres
POSTGRES_PORT=5432
POSTGRES_OPTIONS=content
```


### Авто запуск
1. Клонируем репозиторий
2. Создаем виртуальное окружение python -m venv venv
3. Выполняем команду ```pip install -r requirements.txt```
4. В консоле запускаем ./up.sh (Файл должен быть исполняемым chmod +x ./up.sh)
5. Пользуемся и радуемся)

### Ручной запуск
1. Клонируем репозиторий
2. Создаем виртуальное окружение python -m venv venv
 
Далее выполняем компанды:
```
- source venv/bin/activate
- pip install -r requirements.txt
- docker-compose up --build -d ma_postgres
- python ./sqlite_to_postgres/load_data.py
- docker-compose up --build -d ma_web
- docker-compose up --build ma_nginx
```
