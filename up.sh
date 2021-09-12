#!/bin/bash
echo "Запуск postgres"
docker-compose up --build -d ma_postgres
sleep 5
echo "Начало загрузки данных в postgres"
venv/bin/python ./sqlite_to_postgres/load_data.py
echo "Старт Админки"
docker-compose up --build -d ma_web
docker-compose up --build ma_nginx  # можно сделать просто --build без параметров, указал явно.