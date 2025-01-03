def filter_by_currency(info_list, currency):
    """
    Функция, находящая операции в заданной валюте
    """
    if not info_list:
        raise ValueError("Список транзакций пуст")

    for transaction in info_list:
        if "operationAmount" in transaction:
            result_by_currency = (x for x in info_list if x["operationAmount"]["currency"]["code"] == currency)
            first_item = next(result_by_currency, None)

            if first_item is None:
                raise ValueError("Операции в заданной валюте не найдены")

            yield first_item
            yield from result_by_currency

        elif "currency_code" in transaction:
            result_by_currency = (x for x in info_list if x["currency_code"] == currency)
            first_item = next(result_by_currency, None)

            if first_item is None:
                raise ValueError("Операции в заданной валюте не найдены")

            yield first_item
            yield from result_by_currency

        else:
            raise KeyError("Информация о валюте отсутствует")

