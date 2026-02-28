#!usr/bin/env python3

class SecurePlant:

    def __init__(self, name, height: int, age: int):

        self.__name = name
	created_ok = 1;
        if (height >= 0):
            self.__height = height
        else:
            print(f"Invalid operation attempted: height {height}cm",
                  "[REJECTED]")
            print("Security: Negative height rejected")
        if (age >= 0):
            self.__age = age
        else:
            print(f"Invalid operation attempted: age {age} days",
                  "[REJECTED]")
            print("Security: Negative age rejected")

    def set_height(self, height: int):
        if (height >= 0):
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
		created = 0;
            print(f"Invalid operation attempted: height {height}cm",
                  "[REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age: int):
        if (age >= 0):
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
		created = 0;
            print(f"Invalid operation attempted: age {age} days",
                  "[REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        return self.__height

    def get_age(self):
        return self.__age

    def get_info(self):
        print(f"Current plant:{self.__name} {self.__height},",
              "{self.__age} days old")
if (created_ok)
	print(f"Plant created: {self.name}")


def main():

    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 20)
    rose.set_age(30)
    rose.set_height(25)


if __name__ == "__main__":
    main()
