# Тестовое задание для "UTF"

С использованием Python 3.11, Django 4.2, DRF 3.15, Django Debug Toolbar 4.3

### Локальный запуск

Проект можно запустить и протестировать всё указанное выше самостоятельно.

Инструкция по запуску:

1. Склонируйте репозиторий:
   ```
   git@github.com:tanja-ovc/utf-test-task.git
   ```
   или
   ```
   https://github.com/tanja-ovc/utf-test-task.git
   ```
   
2. Убедитесь, что находитесь в директории проекта ```utf-test-task/```

3. Создайте и активируйте виртуальное окружение:
   ```
   python3 -m venv venv
   ```
   ```
   . venv/bin/activate
   ```
   
4. Обновите менеджер пакетов ```pip```:
   ```
   pip install --upgrade pip
   ```
   
5. Установите необходимые для работы проекта пакеты:
   ```
   pip install -r requirements.txt
   ```
   
6. Перейдите в директорию, содержащую ```manage.py```:
   ```
   cd utf_food/
   ```
   
7. Примените миграции к БД:
   ```
   python3 manage.py migrate
   ```
   
8. При желании загрузите тестовые данные в БД:
   ```
   python3 manage.py loaddata test_data.json
   ```

9. Сделайте запрос по адресу http://127.0.0.1:8000/api/v1/foods/. Вместе с выдачей по запросу справа вы увидите панель Django Debug Toolbar, которую вы можете использовать для анализа запроса.