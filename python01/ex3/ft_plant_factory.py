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

    @staticmethod
    def create_plants() -> list["Plant"]:
        plants = [
            Plant("Rose", 25, 30),
            Plant("Oak", 200, 365),
            Plant("Cactus", 5, 90),
            Plant("Sunflower", 80, 45),
            Plant("Fern", 15, 120)
        ]
        return plants


def main() -> None:

    plants = Plant.create_plants()
    print("=== Plant Factory Output ===")
    count = 0
    for plant in plants:
        count += 1
        print(f"Created: {plant.name} ({plant.height}cm,", end=" ")
        print(f"{plant.days} days)")
    print(f"\nTotal plants created: {count}")


if __name__ == "__main__":
    main()
