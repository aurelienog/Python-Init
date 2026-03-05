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
    try:
        position = convert([position[0], position[1], position[2]])
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: ValueError, Args: ("{e}",)')
    else:
        print_distance(position)


def main() -> None:
    if len(sys.argv) != 4:
        print("No coordinate provided. Usage: python3 ft_coordinate_system.py"
              " <coordinate1> <coordinate2> <coordinate3>")
        return
    print("=== Game Coordinate System ===\n")
    print("Position created: ", end="")
    check_coordinates([sys.argv[1], sys.argv[2], sys.argv[3]])
    print('\nParsing coordinates: "3,4,0"')
    print("Parsed position: ", end="")
    check_coordinates(["3", "4", "0"])
    print('\nParsing invalid coordinates: "abc,def,ghi"')
    check_coordinates(["abc", "def", "ghi"])
    print("\nUnpacking demonstration:")
    coordinates = (3, 4, 0)
    print(f"Player at x={coordinates[0]}, y={coordinates[1]},"
          f" z={coordinates[2]}")
    x, y, z = coordinates
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
