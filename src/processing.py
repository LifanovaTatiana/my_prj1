from typing import Any, Iterable


def filter_by_state(
    dictionaries: Iterable[list[dict[Any, Any]]], state: Any = "EXECUTED"
) -> list[list[dict[Any, Any]]]:
    """Функция выводит список словарей, у которых ключ 'state' соответствует заданному значению"""

    new_list_dict = []
    for i in dictionaries:
        if i["state"] == state:
            new_list_dict.append(i)
    return new_list_dict


def sort_by_date(dictionaries: Iterable[list[dict[Any, Any]]], reverse: bool = True) -> list[list[dict[Any, Any]]]:
    """Функция возвращает список отсортированный по дате"""

    sorted_list_dict = sorted(dictionaries, key=lambda x: x["date"], reverse=reverse)
    return sorted_list_dict
