#!/usr/bin/env python3

import sys


def print_demo(inventory: dict) -> None:
    print("\n=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    is_first = 1
    for key in inventory.keys():
        if not is_first:
            print(", ", end="")
        print(f"{key}", end="")
        is_first = 0
    print("\nDictionary values: ", end="")
    is_first = 1
    for value in inventory.values():
        if not is_first:
            print(", ", end="")
        print(f"{value}", end="")
        is_first = 0
    has_sword = inventory.get("sword")
    if not has_sword:
        print("\nSample lookup - 'sword' in inventory: False")
    else:
        print("\nSample lookup - 'sword' in inventory: True")


def count(inventory: dict) -> int:
    suma = 0
    for value in inventory.values():
        suma += value
    return suma


def print_suggestions(categories: dict) -> None:
    print("\n=== Management Suggestions ===")
    print("Restock needed:", end="")
    isfirst = 1
    for key, value in categories["Scarce"].items():
        if value < 2:
            if not isfirst:
                print(f", {key}", end="")
            else:
                print(f" {key}", end="")
                isfirst = 0
    print("")


def create_categories(inventory: dict) -> None:
    categories = {
        "Abundant": {},
        "Moderate": {},
        "Scarce": {}
    }
    for key, value in inventory.items():
        if value < 4:
            categories["Scarce"][key] = value
        elif value >= 4 and value < 7:
            categories["Moderate"][key] = value
        else:
            categories["Abundant"][key] = value
    print("\n=== Item Categories ===")
    for key, value in categories.items():
        if value:
            print(f" {key}: {value}")
    print_suggestions(categories)


def report_stats(inventory: dict) -> None:
    print("\n=== Inventory Statistics ===")
    max_value = 0
    item = None
    for key, value in inventory.items():
        if value > max_value:
            item = key
            max_value = value
    if max_value == 1:
        print(f"Most abundant: {item} ({max_value} unit)")
    else:
        print(f"Most abundant: {item} ({max_value} units)")
    min_value = 0
    item = None
    for key, value in inventory.items():
        if value < max_value:
            item = key
            min_value = value
    if min_value == 1:
        print(f"Least abundant: {item} ({min_value} unit)")
    else:
        print(f"Least abundant: {item} ({min_value} units)")


def report_current(inventory: dict, qty: int) -> None:
    print("\n=== Current Inventory ===")
    for key, value in inventory.items():
        percent = (value / qty) * 100
        if value == 1:
            print(f"{key}: {value} unit ({percent:.1f}%)")
        else:
            print(f"{key}: {value} units ({percent:.1f}%)")


def make_inventory(list: list) -> dict:
    inventory = dict(list)
    print("=== Inventory System Analysis ===")
    suma = count(inventory)
    print(f"Total items in inventory: {suma}")
    keys = len(inventory.keys())
    print(f"Unique item types: {keys}")
    report_current(inventory, suma)
    report_stats(inventory)
    return inventory


def ft_substr(str: str, start: int, size: int) -> str:
    new = str[start:size]
    return new


def ft_atoi(str: str) -> int:
    i = 0
    number = 0
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while i < len(str):
        j = 0
        while j < 10 and str[i] != digits[j]:
            j += 1
        if j == 10:
            raise ValueError
        number = number * 10 + j
        i += 1
    return number


def separate(str: str, size: int) -> tuple:
    i = 0
    while i < size and str[i] != ':':
        i += 1
    key = ft_substr(str, 0, i)
    if i == size or i + 1 == size:
        raise ValueError("Quantity is missing")
    i += 1
    j = i
    while j < size - 1 and str[j] != ' ':
        j += 1
    try:
        value = ft_atoi(ft_substr(str, i, size))
    except ValueError:
        raise ValueError(f"'{ft_substr(str, i, size)}' is not a valid number")
    return (key, value)


def convert_input(argv: list, size: int) -> list:
    i = 0
    pairs = []
    while i < size:
        try:
            extract = separate(argv[i], len(argv[i]))
        except ValueError as e:
            raise ValueError(f"invalid inventory entry: '{argv[i]}'\n{e}")
        pairs += [extract]
        i += 1
    return pairs


def main() -> None:
    length = len(sys.argv)
    if length < 2:
        return
    else:
        args = sys.argv[1:]
        try:
            pairs = convert_input(args, length - 1)
            inventory = make_inventory(pairs)
            create_categories(inventory)
            print_demo(inventory)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
