from typing import List, Dict

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def process_items(items: List[str]):
    for item in items:
        print(item)


def process_items2(prices: Dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

process_items2({"apple": 1.0, "banana": 2.0})