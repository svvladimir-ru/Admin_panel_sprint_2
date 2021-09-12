Для запуска сервиса выполнить следующие шаги:

### Добавить для запуска файлы .env в sqlite_to_postgres и movies_admin/config/settings
### Авто запуск
1. Клонируем репозиторий
2. Создаем виртуальное окружение python -m venv venv
3. В консоле запускаем ./up.sh (Файл должен быть исполняемым chmod +x ./up.sh)
4. Пользуемся и радуемся)

### Ручной запуск
1. Клонируем репозиторий
2. Создаем виртуальное окружение python -m venv venv
 
Далее выполняем компанды:
- source venv/bin/activate
- pip install -r requirements.txt
- docker-compose up --build -d ma_postgres
- python ./sqlite_to_postgres/load_data.py
- docker-compose up --build -d ma_web
- docker-compose up --build ma_nginx
