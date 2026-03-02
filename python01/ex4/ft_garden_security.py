#!/usr/bin/env python3

class SecurePlant:

    def __init__(self, name: str, height: int, age: int):

        created = 1
        self.__name = name
        if height >= 0:
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm",
                  "[REJECTED]")
            print("Security: Negative height rejected")
            created = 0
        if age >= 0:
            self.__age = age
        else:
            print(f"Invalid operation attempted: age {age} days",
                  "[REJECTED]")
            print("Security: Negative age rejected")
            created = 0
        if created:
            print(f"Plant created: {self.__name}")

    def set_height(self, height: int):
        if height >= 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm",
                  "[REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int):
        if age >= 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days",
                  "[REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        print(f"Current plant: {self.__name} ({self.__height}cm, {self.__age}",
              "days)")


def main():

    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 20)
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    print("")
    rose.get_info()


if __name__ == "__main__":
    main()
