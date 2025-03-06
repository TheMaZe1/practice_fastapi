# FastAPI practice

Это REST API сервис для получения информации о торгах Spimex биржы.

## Установка и запус

### 1. Клонирование репозитория
```sh
https://github.com/TheMaZe1/practice_fastapi.git
```

### 2. Настройка окружения

Создайте файл .env на основе .env.example(так как все разворачивается через docker-compose просто оставить те данные которые написаны в .env.example)

### 3. Запуск через Docker

Запустите контейнеры командой
```sh
docker-compose up -d --build
```

Готово. API доступно по адресу:
http://localhost:8000/

## Документация к API

Документация к API находится по адресу http://localhost:8000/docs

P.S. Для проверки работоспособности API в проекте используется dump БД.

