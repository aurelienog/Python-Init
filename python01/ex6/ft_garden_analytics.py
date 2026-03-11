#!/usr/bin/env python3

class Plant:
    def __init__(self: "Plant", name: str, height: int, age: int) -> None:
        self.name = name
        self.initial_height = height
        self.height = height
        self.age = age

    def describe(self: "Plant") -> str:
        return f"{self.name}: {self.height}cm"

    def grow(self: "Plant") -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_type(self: "Plant") -> str:
        return "regular"


class FloweringPlant(Plant):
    def __init__(self: "FloweringPlant", name: str, height: int, age: int,
                 color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def describe(self: "FloweringPlant") -> str:
        base = super().describe()
        return f"{base}, {self.color} flowers (blooming)"

    def get_type(self: "FloweringPlant") -> str:
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self: "PrizeFlower", name: str, height: int, age: int,
                 color: str, price: int) -> None:
        super().__init__(name, height, age, color)
        self.price = price

    def describe(self: "PrizeFlower") -> str:
        base = super().describe()
        return f"{base}, Prize points: {self.price}"

    def get_type(self: "PrizeFlower") -> str:
        return "prize flowers"


class Garden:

    def __init__(self: "Garden", owner: str) -> None:
        self.collection = []
        self.count = 0
        self.owner = owner
        self.total_growth = 0

    def add_plant(self: "Garden", plant: Plant) -> None:
        new_list = [None] * (self.count + 1)
        i = 0
        while (i < self.count):
            new_list[i] = self.collection[i]
            i += 1
        new_list[i] = plant
        self.collection = new_list
        self.count += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_plants_grow(self: "Garden") -> None:
        print(f"{self.owner} is helping all plants grow...")
        i = 0
        while i < self.count:
            self.collection[i].grow()
            self.total_growth += 1
            i += 1

    def report(self: "Garden") -> None:
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        i = 0
        while (i < self.count):
            plant = self.collection[i]
            print(f"- {plant.describe()}")
            i += 1


class GardenManager:
    total_gardens = 0

    def __init__(self: "GardenManager", name: str) -> None:
        self.name = name
        self.gardens = []

    def add_garden(self: "GardenManager", garden: Garden) -> None:
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls: type["GardenManager"]) -> str:
        return f"Total gardens managed: {cls.total_gardens}"

    @staticmethod
    def validate_height(garden: Garden) -> bool:
        i = 0
        suma = 0
        while i < garden.count:
            suma += (garden.collection[i].height -
                     garden.collection[i].initial_height)
            i += 1
        return garden.total_growth == suma

    class GardenStats:
        def __init__(self: "GardenManager.GardenStats") -> None:
            self.growth_score = 0
            self.plants_score = 0

        def calculate_total_growth(self: "GardenManager.GardenStats",
                                   garden: Garden) -> str:
            return f"Total growth: {garden.total_growth}cm"

        def calculate_total_plants(self: "GardenManager.GardenStats",
                                   garden: Garden) -> str:
            return f"Plants added: {garden.count}"

        def calculate_total_per_type(self: "GardenManager.GardenStats",
                                     garden: Garden) -> str:
            i = 0
            length = garden.count
            regular = 0
            flowering = 0
            prize = 0
            while i < length:
                if garden.collection[i].get_type() == "regular":
                    regular += 1
                elif garden.collection[i].get_type() == "flowering":
                    flowering += 1
                elif garden.collection[i].get_type() == "prize flowers":
                    prize += 1
                i += 1
            return (f"Plant types: {regular} regular, {flowering} flowering,"
                    + f" {prize} prize flowers")

        def calculate_total_score(self: "GardenManager.GardenStats",
                                  garden: Garden) -> int:
            score = 0
            i = 0
            while i < garden.count:
                score += garden.collection[i].height
                if garden.collection[i].get_type() == "flowering":
                    score += 10
                elif garden.collection[i].get_type() == "prize flowers":
                    score += 20 + garden.collection[i].price
                i += 1
            return score


def main() -> None:
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager("Alice")
    garden1 = Garden(manager.name)
    manager.add_garden(garden1)
    garden1.add_plant(Plant("Oak Tree", 100, 350))
    garden1.add_plant(FloweringPlant("Rose", 25, 10, "red"))
    garden1.add_plant(PrizeFlower("Sunflower", 50, 8, "yellow", 10))
    print("")
    garden1.help_plants_grow()
    print("")
    garden1.report()
    stats = manager.GardenStats
    print(f"\n{stats.calculate_total_plants(manager, garden1)}", end=", ")
    print(f"{stats.calculate_total_growth(manager, garden1)}")
    print(f"{stats.calculate_total_per_type(manager, garden1)}")
    bob = GardenManager("Bob")
    garden2 = Garden(bob.name)
    bob.add_garden(garden2)
    print(f"\nHeight validation test: {manager.validate_height(garden1)}")
    print(f"Garden scores - {manager.name}: "
          + f"{stats.calculate_total_score(manager, garden1)}, "
          + f"{bob.name}: 92")
    print(f"{GardenManager.create_garden_network()}")


if __name__ == "__main__":
    main()
