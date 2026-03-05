#!/usr/bin/env python3

import sys


def make_inventory(list: list) -> None:
    inventory = dict(list)
    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {sum(inventory.values())}")
    print(f"Unique item types: {len(inventory.keys())}")


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
    if i == size:
        raise ValueError
    i += 1
    j = i
    while j < size - 1 and str[j] != ' ':
        j += 1
    if str[j] == size:
        raise ValueError
    try:
        value = ft_atoi(ft_substr(str, i, size))
    except ValueError:
        raise ValueError
    return (key, value)


def convert_input(argv: list, size: int) -> list:
    i = 0
    pairs = []
    while i < size:
        try:
            extract = separate(argv[i], len(argv[i]))
        except ValueError:
            raise ValueError
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
            make_inventory(pairs)
        except ValueError:
            print("nop")


if __name__ == "__main__":
    main()
