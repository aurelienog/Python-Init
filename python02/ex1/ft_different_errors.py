#!/usr/bin/env python3

def garden_operations() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\nTesting ZeroDivisionError...")
    try:
        5 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        open("test.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("\nTesting KeyError...")
    try:
        plants = {"rose": "red", "tulip": "yellow"}
        plants["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    print("\nTesting multiple errors together...")
    try:
        int("abc") / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


def test_error_types() -> None:
    garden_operations()


# def main() -> None:
#     test_error_types()


# if __name__ == "__main__":
#     main()
