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
Запустить тесты можно командой: pytest

 Структура проекта
/app                        
    test_app.py        # Тесты для API
```

![Screenshot from 2024-06-11 14-18-39](https://github.com/ElenaGlu/Affiliate_network/assets/123466535/38782a3a-c451-4eb4-a412-327b3ac84fbf)
![Screenshot from 2024-06-11 14-18-59](https://github.com/ElenaGlu/Affiliate_network/assets/123466535/331b270b-9fb2-46d1-9503-39e4e1c590ae)
![Screenshot from 2024-06-11 14-19-14](https://github.com/ElenaGlu/Affiliate_network/assets/123466535/13753559-3a6f-4d51-b9bc-c49354bdb3ff)
![Screenshot from 2024-06-11 14-19-55](https://github.com/ElenaGlu/Affiliate_network/assets/123466535/b37b2065-8b37-462a-9833-1abc31006823)
![Screenshot from 2024-06-11 14-20-36](https://github.com/ElenaGlu/Affiliate_network/assets/123466535/583efedb-b52e-40d8-a0b3-8e1234154c92)


