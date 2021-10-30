# Настройка виртуального окружения:

Добавить в проект файл .env командой
```console
cp .env.template .env
```
Настроить переменные среды в .env файле
- SECRET_KEY
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB

# Поднятие контейнера:
Для запуска сервера необходимо выполнить команду: 
```console
make run_server
```

# После запуска контейнеров:
Создать нового юзера:
```console
make create_superuser
```

Сервер будет доступен по адресу [0.0.0.0:8000](http://0.0.0.0:8000/admin/).