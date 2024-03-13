
# Тестовое Задание


### О проекте

Простейшая форма опроса для клиентов на Django для Nomia



### Запуск (Локально или через Docker)

* #### Docker
    ```
    docker-compose up -d --build
    ```

* #### Локально

    #### Обязательно подставьте свои данные в DATABASES settings.py

    Cоздать и активировать виртуальное окружение:

    ```
    python3 -m venv venv
    ```

    * Если у вас Linux/macOS

        ```
        source venv/bin/activate
        ```

    * Если у вас windows

        ```
        source venv/scripts/activate
        ```


Установить зависимости из файла requirements.txt:


  ```
  python3 -m pip install --upgrade pip
  pip install -r requirements.txt
  ```
Создание и применение миграций

  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

Запуск
  ```
  python3 manage.py runserver
  ```

#### Приложение доступно на...
    
    http://127.0.0.1:8000/
 


### Технологии
Проект написан на Python/Django/PostgreSQL/Docker а все используемые технологии удобно расположены в файле requirements.txt

### Автор
Дмитрий Самсонов
