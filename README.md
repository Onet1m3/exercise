# [Python/Django] Exercise

Запуск Django приложения версии `3.0`:

  * Склонируйте репозиторий в нужную вам директорию 
  * Откройте проект используя PyCharm или другие IDE
  * Стандартные настройки в `settings.py`
  * Установка зависимостей `pipenv install`
  * Активируйте системное окружение `pipenv shell`
  * Создание суперпользователя  `python manage.py make_user` логин и пароль будут admin admin
  * Накатите фикстуры `python manage.py loaddata users.json`

Теперь перйдите на [`localhost:8000`](http://localhost:8000) в вашем браузере, чтобы убедится, что всё работает.

## Запуск Celery для виндовс
  * запуск сelery-beat(планировщик) `celery -A skillbox beat`
  * запуск celery tasks `celery -A skillbox worker -l INFO --pool=solo`
## Запуск Celery для linux
  * celery --app=exercise worker -B -l INFO
        
## Шаблоны HTML

  * Все HTML, нужные для сайта, хранятся в директории `/templates/`


## Сайт располагается на IP 165.22.193.8