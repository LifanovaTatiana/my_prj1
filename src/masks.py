def get_mask_card_number(number_card: str) -> str:
    """
    Функция маскировки номера банковской карты
    """
    if len(number_card) != 16 or not number_card.isdigit():
        raise ValueError("Неверный номер карты")
    str_number_card = str(number_card)
    return f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"


def get_mask_account(number_account: str) -> str:
    """
    Функция маскировки номера банковского счета
    """
    if len(number_account) != 20 or not number_account.isdigit():
        raise ValueError("Неверный номер счёта")
    str_number_account = str(number_account)
    return f"**{str_number_account[-4:]}"
