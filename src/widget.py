import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(bank_info: str) -> str:
    """
    Функция, маскирующая информацию как о картах, так и о счетах
    """

    if "Счет" in bank_info:
        return "Счет" + " " + get_mask_account(bank_info[5:])
    else:
        return f"{bank_info[:-16]}{get_mask_card_number(bank_info[-16:])}"


def get_date(data_string: str) -> str:
    """Функция, возвращает строку с датой в формате "ДД.ММ.ГГГГ" """
    pattern = r"^\d{4}\-\d{2}\-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}$"
    if not bool(re.match(pattern, data_string)):
        raise ValueError("Неверный формат даты")
    date = data_string.split("T")[0]
    date_parts = date.split("-")
    [year, month, day] = date_parts
    if int(month) > 12 or int(day) > 31:
        raise ValueError("Неверная дата")
    return f"{day}.{month}.{year}"
