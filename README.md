# Виджет банковских операций клиента
## Описание проекта
Программа создана для фильтрации и сортировки банковских счетов по дате и оплате.

В модуле masks находятся функции get_mask_card_number и get_mask_account, которые возвращают замаскированный номер карты или счета.

В модуле widget находятся две функции mask_account_card, которая маскирует номер карты или счета и get_date, которая возвращает дату в верном формате ДД.ММ.ГГГГ

В модуле generators находится функция filter_by_currency, которая находит операции в заданной валюте, функция transaction_descriptions, выводящая описания операций из списка. А также функция card_number_generator, генерирующая номера банковских карт в заданном 16-значном формате. Все три функции в этом модуле представляют собой итераторы, возвращающие по одному значению за раз с помощью "yield".

В модуле processing находится функция filter_by_state, сортирующая списки со словарями данных по ключу 'state' и sort_by_date, которая принимает список словарей и возвращает отсортированный по параметру "date" в порядке убывания список.

Финальным модулем проекта выступает main, в котором реализована функция main, отвечающая за основную логику проекта и связывающая функциональности написанных ранее функций между собой.
## Project dependencies:
* The program uses the version Python 3.12.4
* flake8 = "7.1.0"
* black = "24.4.2"
* sort = "5.13.2"
* mypy = "1.10.0"
## Функции, которые мы будем использовать:
* Функция скрывающая номер карты и счета
* Функция сортировки по дате
* Функция фильтрации в операциях по счетам
## Тестирование проекта
Проект покрыт юнит-тестами Pytest.
Чтобы запустить тесты с оценкой покрытия выполните команду:
* poetry run pytest --cov 
Чтобы сгенерировать отчет о покрытии в HTML-формате, где src — пакет c модулями, которые тестируем. 
Отчет будет сгенерирован в папке htmlcov и храниться в файле с названием index.html:
* pytest --cov=src --cov-report=html
## Инструкция по установке
1.Чтобы скачать репозиторий:
* git clone git@github.com:LifanovaTatiana/my_prj1.git

2.Установить не обходимые зависимости
* pip install -r requirements.txt

## Команда проекта:
* Татьяна Лифанова — Back-End developer
* Команда SkyPro
## Контакт для связи с командой разработки:
* lifanova.tatiana.v@gmail.com
