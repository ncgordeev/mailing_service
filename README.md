<h3 align="center">Сервис email рассылки сообщений на Django</h3>

<details>
  <summary>Оглавление</summary>
  <ol>
    <li>О проекте</li>
    <li>Технологии</li>
    <li>Настройка проекта</li>
    <li>Использование</li>
    <li>Контакты</li>
  </ol>
</details>



## О проекте

Сервис email рассылок. После регистрации вы сможете добавить клиентов, сообщение и создать рассылку,
выбрав дату начала и окончания рассылки и с какой периодичностью производить рассылку.
При наступлении даты отправки происходит автоматическая отправка сообщения вашим клиентам.

## Технологии
- Django
- PostgreSQL
- Redis
- Crontab


## Настройка проекта

Для работы с проектом произведите базовые настройки.

### 1. Клонирование проекта

Клонируйте репозиторий используя следующую команду.
  ```sh
  git clone git@github.com:ncgordeev/mailing_service.git
  ```


### 2. Настройка виртуального окружения и установка зависимостей

- Инструкция для работы через виртуальное окружение - poetry: 
```text
poetry init - Создает виртуальное окружение
poetry shell - Активирует виртуальное окружение
poetry install - Устанавливает зависимости
```

### 3. Редактирование .env.sample:

- В корне проекта переименуйте файл .env.sample в .env и отредактируйте параметры:
    ```text
    # Postgresql
    PG_NAME=="db_name" - название вашей БД
    PG_USER="postgres" - имя пользователя БД
    PG_PASSWORD=="secret" - пароль пользователя БД
    PG_HOST=="host" - можно указать "localhost" или "127.0.0.1"
    PG_PORT=port - указываете порт для подключения по умолчанию 5432
    
    # Django
    SECRET_KEY=secret_key - секретный ключ django проекта
  
    # Mailing  
    EMAIL_HOST_USER='your_email@yandex.ru' - ваш email yandex
    EMAIL_HOST_PASSWORD='your_yandex_smtp_password' - ваш пароль smtp (подробнее о настройке ниже)
    
    # Superuser
    ADMIN_EMAIL='admin@test.com' - email регистрации администратора сайта
    ADMIN_PASSWORD='secret' - пароль регистрации администратора сайта
    
    # Redis
    REDIS_HOST=redis://host:port - данные местоположения redis
    CACHE_ENABLED=True - использование кэша
    ```
- О настройке почты smtp: 
[Настройка почтового сервиса SMTP ](https://proghunter.ru/articles/setting-up-the-smtp-mail-service-for-yandex-in-django)

### 4. Настройка БД и кэширования:

- Создать миграции:
  ```text
  python manage.py makemigrations
  ```

- Примените миграции:
  ```text
  python manage.py migrate
  ```

- Если вы хотите чистый сайт без данных и пользователей тогда применять фикстуру ниже не надо, 
для создания суперюзера введите команду: 
  ```text
  python manage.py csu
  ```
 
- Если вы хотите использовать данные из фикстур этого проекта создавать суперюзера не надо введите команду:
  ```text
  python manage.py loaddata fixtures/*.json
  ```

- Установите Redis:

  - Linux команда:
   ```text
   sudo apt install redis; 
  или 
  sudo yum install redis;
   ```

  - macOS команда:
   ```text
   brew install redis;
   ```

  Windows инструкция:
  - [Перейти на Redis docs](https://redis.io/docs/install/install-redis/install-redis-on-windows/)


## Использование

- Для запуска проекта наберите в терминале команду:
  ```text
  python manage.py runserver
  ```
  перейдите по адресу: [http://127.0.0.1:8000](http://127.0.0.1:8000)


- Для запуска автоматической отправки рассылок (происходит проверка раз в минуту), необходимо использовать команду запустив рядом с проектом в новом окне:
  ```text
  python manage.py crontab add
  ```
  Просмотреть периодические задачи:
  ```text
  python manage.py crontab show
  ```
  Удалить периодические задачи:
  ```text
  python manage.py crontab remove
  ```

- Для ручного запуска рассылок можно использовать команду:
  ```text
  python manage.py run_mailing
  ```
