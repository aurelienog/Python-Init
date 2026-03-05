#!/usr/bin/env python3

import sys


def main() -> None:
    length = len(sys.argv)
    print("=== Command Quest ===")
    if length < 2:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {length}")
    elif length == 2:
        print(f"Program name: {sys.argv[0]}")
        print("Arguments received: 1")
        print(f"Argument 1: {sys.argv[1]}")
        print(f"Total arguments: {length}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {length - 1}")
        i = 1
        while i < length:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {length}")


if __name__ == "__main__":
    main()
