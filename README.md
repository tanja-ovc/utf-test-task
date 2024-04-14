# Тестовое задание для "UTF"

Решение задания находится в файле [utf_food/food/api/v1/views.py](https://github.com/tanja-ovc/utf-test-task/blob/main/utf_food/food/api/v1/views.py)

Сам проект полноценно создан для того, чтобы было удобно тестировать решение. Исходный код задания просто структурирован и размещён в соответствующие директории и файлы, ничего не изменено.

### Технологии

Python 3.11, Django 4.2, DRF 3.15, Django Debug Toolbar 4.3

### Визуализация решения

- Суммарно:

<img width="1040" alt="Screenshot 2024-04-13 at 23 23 32" src="https://github.com/tanja-ovc/utf-test-task/assets/85249138/bc6bdf95-0352-4af4-8464-8d8e9b51f85e">

- Подробно:

<img width="1042" alt="Screenshot 2024-04-13 at 23 24 01" src="https://github.com/tanja-ovc/utf-test-task/assets/85249138/eaaa8e2d-f892-4dc9-a96b-39a71f28a027">
<img width="1031" alt="Screenshot 2024-04-13 at 23 24 20" src="https://github.com/tanja-ovc/utf-test-task/assets/85249138/aecfd42a-48e9-49f4-a5c2-61106cb862a7">
<img width="1027" alt="Screenshot 2024-04-13 at 23 24 38" src="https://github.com/tanja-ovc/utf-test-task/assets/85249138/4234228f-e695-4640-8ba4-c3a928881610">

- Тестируемые данные (здесь наглядно, полноценно тут: [test_data.json](https://github.com/tanja-ovc/utf-test-task/blob/main/utf_food/test_data.json))

<img width="697" alt="Screenshot 2024-04-13 at 23 20 52" src="https://github.com/tanja-ovc/utf-test-task/assets/85249138/2858f9ee-9ba8-45b1-b164-d9ed47a3228f">

<img width="700" alt="Screenshot 2024-04-13 at 23 20 26" src="https://github.com/tanja-ovc/utf-test-task/assets/85249138/471382b0-ae1a-47d7-97ba-3a0725211294">

- Как выглядит выдача по GET-запросу по http://127.0.0.1:8000/api/v1/foods/:

```json
[
    {
        "id": 1,
        "name_ru": "Напитки",
        "name_en": "Beverages",
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": 333,
                "code": 3046,
                "name_ru": "Кола",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "120.00",
                "additional": [
                    555,
                    444
                ]
            },
            {
                "internal_code": 222,
                "code": 3046,
                "name_ru": "Спрайт",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "120.00",
                "additional": [
                    555,
                    444
                ]
            }
        ]
    },
    {
        "id": 2,
        "name_ru": "Выпечка",
        "name_en": "Pastry",
        "name_ch": null,
        "order_id": 11,
        "foods": [
            {
                "internal_code": null,
                "code": 670,
                "name_ru": "Берлинер",
                "description_ru": null,
                "description_en": null,
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "230.00",
                "additional": []
            }
        ]
    },
    {
        "id": 5,
        "name_ru": "Фаст фуд",
        "name_en": null,
        "name_ch": null,
        "order_id": 15,
        "foods": [
            {
                "internal_code": 555,
                "code": 345,
                "name_ru": "Бургер",
                "description_ru": null,
                "description_en": "Burger",
                "description_ch": null,
                "is_vegan": false,
                "is_special": false,
                "cost": "300.00",
                "additional": [
                    333,
                    222,
                    111
                ]
            }
        ]
    }
]
```


### Локальный запуск

Проект можно запустить и протестировать всё указанное выше самостоятельно.

Инструкция по запуску:

1. Склонируйте репозиторий:
   ```
   git clone git@github.com:tanja-ovc/utf-test-task.git
   ```
   или
   ```
   git clone https://github.com/tanja-ovc/utf-test-task.git
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

9. Запустите локальный сервер:
   ```
   python3 manage.py runserver
   ```

10. Сделайте запрос по адресу http://127.0.0.1:8000/api/v1/foods/. Вместе с выдачей по запросу справа вы увидите панель Django Debug Toolbar, которую вы можете использовать для анализа запроса.

    <img width="899" alt="Screenshot 2024-04-14 at 00 10 19" src="https://github.com/tanja-ovc/utf-test-task/assets/85249138/e77eb3c5-88c8-417a-8c44-fd93d055604e">
