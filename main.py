# from src.widget import mask_account_card, get_date
# from src.masks import get_mask_card_number, get_mask_account
from src.processing import filter_by_state, sort_by_date

# Задание 1
# card_number = int(input("Введите номер карты: "))
# accound_number = int(input("Введите номер счета: "))
#
# print(get_mask_card_number(card_number))
# print(get_mask_account(accound_number))

# Задание 2
# card_number = str(input("Введите номер карты/счёта: "))
# accound_number = str(input("Введите дату: "))
#
# print(mask_account_card(card_number))
# print(get_date(accound_number))

# Задание 3
print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
