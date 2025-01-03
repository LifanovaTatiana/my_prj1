from typing import Dict, List


def filter_by_state(dictionaries: List[Dict[str, str | int]], state: str = "EXECUTED") -> List[Dict[str, str | int]]:
    """Функция выводит список словарей, у которых ключ 'state' соответствует заданному значению"""

    filtered_list = []
    for i in dictionaries:
        if i["state"] == state:
            filtered_list.append(i)
    return filtered_list


def sort_by_date(dictionaries: List[Dict[str, str | int]], reverse: bool = True) -> List[Dict[str, str | int]]:
    """Функция возвращает список отсортированный по дате"""

    sorted_list = sorted(dictionaries, key=lambda x: x["date"], reverse=reverse)
    return sorted_list
