## _Веб-приложение для работы с трекером Keitaro_
Веб-сервис для управления партнерскими сетями и офферами через Keitaro Tracker.

Сервис позволяет:
-  Создавать партнерские сети (Affiliate Networks) и офферы (Offers)
-  Сохранять их в базе данных
-  Отправлять данные в Keitaro по отдельным запросам
-  Получать список офферов и сетей из Keitaro

 Эндпоинты:

- `POST /aff_network/` — добавить партнерскую сеть в БД  
- `POST /offer/` — добавить оффер в БД
- `GET /get_aff_network/` — получить информацию о партнерской сети из Keitaro  
- `GET /get_offer/` — получить информацию об оффере из Keitaro  

### Технологии:

Python3, FastAPI, PostgreSQL, Tortoise ORM, Aerich, Poetry, Docker Compose, Jinja2, Pytest

### Тестирование:

Использован Pytest для написания интеграционных тестов.

```
/app                        
    test_app.py
```
![MyCollages (2)](https://github.com/user-attachments/assets/61199dfa-7ce5-40e8-9ba8-7109fac93da0)
