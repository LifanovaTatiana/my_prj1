from masks import get_mask_card_number, get_mask_account


def mask_account_card(bank_info: str) -> str:
    """
    Функция, маскирующая информацию как о картах, так и о счетах
    """

    if "Счет" in bank_info:
        return "Счет" + " " + get_mask_account(bank_info[5:])
    else:
        return f"{bank_info[:-16]}, get_mask_card_number(bank_info[-16:])"


def get_date(data_string: str) -> str:
    """ Функция, возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """

    return f"{data_string[8:10]}.{data_string[5:7]}.{data_string[:4]}"
