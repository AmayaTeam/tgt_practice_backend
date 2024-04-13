# TGT Весенняя технологическая практика

## Чтобы запустить проект
1. Запуск проекта
   * Собрать и запустить проект
     ```commandline
     docker-compose up -d --build
     ```
   * Запустить проект
     ```commandline
     docker-compose up -d
     ```
   * Остановить проект
     ```commandline
     docker-compose stop
     ```

## Перед коммитом
*  Отформатируй код с помощью команды:
    ```commandline
    black .
    ```
*  Используй линтер для дополнительной проверки:
    ```commandline
    flake8 .
    ```

Дополнительно:
* запуск консоли изнутри контейнера:
  ```commandline
  docker-compose exec web poetry run python manage.py shell 
  ```