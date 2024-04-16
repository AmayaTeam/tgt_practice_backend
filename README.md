# TGT Весенняя технологическая практика (Backend)

## Чтобы запустить проект
1. Запуск проекта
   * Собрать и запустить проект (в фоне)
     ```commandline
     docker-compose up -d --build
     ```
   * Запустить проект (в фоне)
     ```commandline
     docker-compose up -d
     ```
   * Запустить проект в командной строке
     ```commandline
     docker-compose up
     ```
   * Остановить проект
     ```commandline
     docker-compose stop
     ```
2. Тестовые данные
   * Загрузить тестовые данные
     ```commandline
     docker-compose exec web poetry run python manage.py add_base_data
     ```
   * Удалить тестовые данные
     ```commandline
     docker-compose exec web poetry run python manage.py add_base_data
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
* Запуск консоли изнутри контейнера:
  ```commandline
  docker-compose exec web poetry run python manage.py shell 
  ```
* Если порт postgresql уже используется:
  * найти процесс которым занят
    ```commandline
    sudo lsof -i :5432
    ```
  * остановить его
    ```commandline
    sudo kill <PID>
    ```
  * если не помогает, перезапусти сервис postgres
    ```commandline
    sudo service postgresql restart 
    ```
* Добавить зависимость в проект:
  ```commandline
  poetry add <python_package>
  ```