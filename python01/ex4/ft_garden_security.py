#!/usr/bin/env python3

class SecurePlant:

    def __init__(self: "SecurePlant", name: str) -> None:
        self.__name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {name}")

    def set_height(self: "SecurePlant", height: int) -> None:
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm",
                  "[REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self: "SecurePlant", age: int) -> None:
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days",
                  "[REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self: "SecurePlant") -> int:
        return self.__height

    def get_age(self: "SecurePlant") -> int:
        return self.__age

    def get_info(self: "SecurePlant") -> None:
        print(f"Current plant: {self.__name} ({self.__height}cm, {self.__age}",
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
