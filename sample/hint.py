from typing import List

def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def process_items(items: List[str]):
    for item in items:
        print(item)

print(get_full_name("john", "doe")) # John Doe
print(get_name_with_age(get_full_name("john", "doe"), 23)) # John Doe is this old: 23
process_items(["apple", "banana"])