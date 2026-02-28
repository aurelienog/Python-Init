#!usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, days: int):
        self.name = name
        self.height = height
        self.days = days

    def grow(self):
        self.height += 1

    def age(self):
        self.days += 1

    def get_info(self):
        print(f"{self.name}: {self.height}, {self.days} days old")


def main():

    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    i = 0
    print("=== Plant Factory Output ===")
    while (i < 5):
        print(f"Created: {plants[i].name} ({plants[i].height}cm,", end=" ")
        print(f"{plants[i].days} days)")
        i += 1
    print(f"\nTotal plants created: {i}")


if __name__ == "__main__":
    main()
