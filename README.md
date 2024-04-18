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
     docker-compose exec web poetry run python manage.py delete_data
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
## Примеры GraphQL запросов
* Endpoint GraphQL http://localhost:8000/graphql/ (можно через визуальный интерфейс, либо через Postman или любую другую подобную программу)

### Примеры запросов

```
# Query ToolModuleGroup
query {
  toolModuleGroups {
    name
    toolmoduletypeSet {
      name
      toolmoduleSet {
        sn
        toolinstalledsensorSet {
          rToolsensortypeId {
            name
          }
        }
      }
    }
  }
}
# Create ToolInstalledSensor
mutation {
  createToolInstalledSensor(input: {
    rToolmoduleId: "4d519190-356f-4c40-b4b0-455e72a9cecb",
    rToolsensortypeId: "80d5c792-6435-447d-85d7-f9ca07a7b993",
    recordPoint: 666
  }) {
    toolInstalledSensor {
      id
      rToolmoduleId {
        id
      }
      rToolsensortypeId {
        id
      }
      recordPoint
    }
  }
}
# Update
mutation {
  updateToolInstalledSensor(input: {
    id: "88c96469-6fcd-419e-9d82-90c829365e58",
    recordPoint: 123.45
  }) {
    toolInstalledSensor {
      id
      rToolmoduleId {
        id
      }
      rToolsensortypeId {
        id
      }
      recordPoint
    }
  }
}
# Delete
mutation {
  deleteToolInstalledSensor(input: {id: "88c96469-6fcd-419e-9d82-90c829365e58"}) {
    success
  }
}
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