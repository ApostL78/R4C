[![Django CI](https://github.com/ApostL78/R4C/actions/workflows/django.yml/badge.svg)](https://github.com/ApostL78/R4C/actions/workflows/django.yml)
[![codecov](https://codecov.io/gh/ApostL78/R4C/graph/badge.svg?token=PRDT1TC0A4)](https://codecov.io/gh/ApostL78/R4C)

# How To Run
To start this app you need to:
1. Clone this repo and move to project
```sh
git clone https://github.com/ApostL78/R4C.git && cd R4C
```
2. Create and activate `venv`
```sh
python3 -m venv venv && source ./venv/bin/activate
```
3. Create environment variables
```sh
cp .env.example .env
```
and then put your values

4. Run with docker-compose
```sh
docker-compose up --build -d
```
After the application starts, navigate to `http://localhost:8000` in your web browser.

5. For best usage go inside web app container
```sh
docker-compose exec -it web bash
``` 
then run command and create super user to manage data in admin page
```sh
python3 manage.py createsuperuser
```
Login in admin panel, create instances and check endpoints




# R4C - Robots for consumers

## Небольшая предыстория.
Давным-давно, в далёкой-далёкой галактике, была компания производящая различных 
роботов. 

Каждый робот(**Robot**) имел определенную модель выраженную двух-символьной 
последовательностью(например R2). Одновременно с этим, модель имела различные 
версии(например D2). Напоминает популярный телефон различных моделей(11,12,13...) и его версии
(X,XS,Pro...). Вне компании роботов чаще всего называли по серийному номеру, объединяя модель и версию(например R2-D2).

Также у компании были покупатели(**Customer**) которые периодически заказывали того или иного робота. 

Когда роботов не было в наличии - заказы покупателей(**Order**) попадали в список ожидания.

---
## Что делает данный код?
Это заготовка для сервиса, который ведет учет произведенных роботов,а также 
выполняет некие операции связанные с этим процессом.

Сервис нацелен на удовлетворение потребностей трёх категорий пользователей:
- Технические специалисты компании. Они будут присылать информацию
- Менеджмент компании. Они будут запрашивать информацию
- Клиенты. Им будут отправляться информация
___

## Как с этим работать?
- Создать для этого проекта репозиторий на GitHub
- Открыть данный проект в редакторе/среде разработки которую вы используете
- Ознакомиться с задачами в файле tasks.md
- Написать понятный и поддерживаемый код для каждой задачи 
- Сделать по 1 отдельному PR с решением для каждой задачи
- Прислать ссылку на своё решение
