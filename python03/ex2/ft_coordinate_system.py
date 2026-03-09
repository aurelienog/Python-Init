#!/usr/bin/env python3

import sys
from math import sqrt


def convert(arguments: list) -> tuple:
    converted = [0] * 3
    i = 0
    while (i < 3):
        try:
            converted[i] = int(arguments[i])
        except ValueError:
            raise ValueError("invalid literal for int() with base 10: "
                             f"'{arguments[i]}'")
        i += 1
    return tuple(converted)


def print_distance(position: tuple) -> None:
    print(position)
    distance = sqrt((0-position[0])**2 + (0-position[1])**2 +
                    (0-position[2])**2)
    if (distance * 100) % 10 != 0:
        print(f"Distance between (0, 0, 0) and {position}: {distance:.2f}")
    else:
        print(f"Distance between (0, 0, 0) and {position}: {distance:.1f}")


def check_coordinates(position: list) -> None:
    is_first = 1
    try:
        position = convert([position[0], position[1], position[2]])
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{position[0]}', end=",")
        print(f'{position[1]}', end=",")
        print(f'{position[2]}"')
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}",)')
    else:
        if is_first:
            print("Position created: ", end="")
        is_first = 0
        print_distance(position)


def main() -> None:
    if len(sys.argv) != 4:
        print("No coordinate provided. Usage: python3 ft_coordinate_system.py"
              " <coordinate1> <coordinate2> <coordinate3>")
        return
    print("=== Game Coordinate System ===\n")
    check_coordinates([sys.argv[1], sys.argv[2], sys.argv[3]])
    print('\nParsing coordinates: "3,4,0"')
    print("Parsed position: ", end="")
    check_coordinates(["3", "4", "0"])
    check_coordinates(["abc", "def", "ghi"])
    print("\nUnpacking demonstration:")
    coordinates = (3, 4, 0)
    print(f"Player at x={coordinates[0]}, y={coordinates[1]},"
          f" z={coordinates[2]}")
    x, y, z = coordinates
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
