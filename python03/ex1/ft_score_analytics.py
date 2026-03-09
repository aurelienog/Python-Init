#!/usr/bin/env python3

import sys


def convert_atoi(arguments: list) -> list:
    valid_numbers = 0
    i = 1
    while (i < len(arguments)):
        try:
            int(arguments[i])
            valid_numbers += 1
        except ValueError:
            print(f"Error: '{arguments[i]}' is not a number")
        i += 1
    if (valid_numbers == 0):
        return []
    numbers = [0] * valid_numbers
    i = 1
    j = 0
    while (i < len(arguments)):
        try:
            numbers[j] = int(arguments[i])
            j += 1
        except ValueError:
            pass
        i += 1
    return numbers


def print_scores(numbers: list) -> None:
    i = 0
    first = 1
    print("Scores processed: [", end="")
    while (i < len(numbers)):
        if (not first):
            print(f", {numbers[i]}", end="")
        else:
            first = 0
            print(f"{numbers[i]}", end="")
        i += 1
    print("]")


def print_stats(numbers: list) -> None:
    suma = sum(numbers)
    length = len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    print_scores(numbers)
    print(f"Total players: {length}")
    print(f"Total score: {suma}")
    print(f"Average score: {suma / length}")
    print(f"High score: {maximum}")
    print(f"Low score: {minimum}")
    print(f"Score range: {maximum - minimum}")


def main() -> None:
    length = len(sys.argv)
    print("=== Player Score Analytics ===")
    if length < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        numbers = convert_atoi(sys.argv)
        if numbers:
            print_stats(numbers)


if __name__ == "__main__":
    main()
