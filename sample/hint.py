from typing import List, Dict, Optional

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


def say_hi(name: Optional[str] = None): # デフォルトはNone
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

say_hi()
say_hi("John")