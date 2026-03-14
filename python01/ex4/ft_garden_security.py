#!/usr/bin/env python3

class SecurePlant:

    def __init__(self: "SecurePlant", name: str) -> None:
        self._name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {name}")

    def set_height(self: "SecurePlant", height: int) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm",
                  "[REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self: "SecurePlant", age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days",
                  "[REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self: "SecurePlant") -> int:
        return self._height

    def get_age(self: "SecurePlant") -> int:
        return self._age

    def get_info(self: "SecurePlant") -> None:
        print(f"Current plant: {self._name} ({self._height}cm, {self._age}",
              "days)")


def main() -> None:

    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    print("")
    rose.get_info()


if __name__ == "__main__":
    main()
