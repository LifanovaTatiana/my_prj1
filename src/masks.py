def get_mask_card_number(number_card: int) -> str:
    """
    Функция маскировки номера банковской карты
    """
    str_number_card = str(number_card)
    return f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"

def get_mask_account(number_account: int) -> str:
    """
    Функция маскировки номера банковского счета
    """
    str_number_account = str(number_account)
    return f"**{str_number_account[-4:]}"


