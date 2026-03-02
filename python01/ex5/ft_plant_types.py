#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age, plant_type):
        self.name = name
        self.height = height
        self.age = age
        self.plant_type = plant_type

    def describe(self):
        return print(f"{self.name} ({self.plant_type}): "
                     f"{self.height}cm, {self.age} days", end="")


class Flower(Plant):
    def __init__(self, name, height, age, color):

        super().__init__(name, height, age, "Flower")
        self.color = color

    def describe(self):
        super().describe()
        print(f", {self.color} color")

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):

        super().__init__(name, height, age, "Tree")
        self.trunk_diameter = trunk_diameter

    def describe(self):
        super().describe()
        print(f", {self.trunk_diameter}cm diameter")

    def produce_shade(self):
        print(f"{self.name} provides 78 square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str):
        super().__init__(name, height, age, "Vegetable")
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe(self):
        super().describe()
        print(f", {self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}")


def main():

    plants = [
        Flower("Rose", 25, 30, "red"),
        Tree("Oak", 500, 1825, 50),
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Flower("Sunny", 10, 15, "yellow"),
        Tree("Tea", 250, 500, 30),
        Vegetable("Eggy", 12, 10, "winter", "iron")
    ]
    i = 0
    print("=== Garden Plant Types ===\n")
    while i < 3:
        plants[i].describe()
        if (plants[i].plant_type == "Flower"):
            plants[i].bloom()
            print("")
        elif (plants[i].plant_type == "Tree"):
            plants[i].produce_shade()
            print("")
        i += 1


if __name__ == "__main__":
    main()
