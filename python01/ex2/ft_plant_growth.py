#!/usr/bin/env python3

class Plant:
    def __init__(self: "Plant", name: str, height: int, days: int) -> None:
        self.name = name
        self.height = height
        self.days = days

    def grow(self: "Plant") -> None:
        self.height += 1

    def age(self: "Plant") -> None:
        self.days += 1

    def get_info(self: "Plant") -> None:
        print(f"{self.name}: {self.height}, {self.days} days old")


def main() -> None:
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Sunflower", 80, 45)
    print("=== Day 1 ===")
    p1.get_info()
    print("=== Day 7 ===")
    i = 0
    while i < 6:
        p1.grow()
        p1.age()
        p2.grow()
        p2.age()
        i += 1
    p1.get_info()
    print("Growth this week: +6cm")


if __name__ == "__main__":
    main()
