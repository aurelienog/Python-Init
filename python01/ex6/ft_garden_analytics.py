#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def describe(self):
        print(f"{self.name}: {self.height}cm", end="")

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color
    
    def describe(self):
        super().describe()
        print(f" , {self.color} flowers (blooming)", end="")

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, price: int):
        super().__init__(name, height, age, color)
        self.price = price

    def describe(self):
        super().describe()
        print(f" , Prize points: {self.price}")


class Garden:

    def __init__(self, owner: str):
        self.collection = []
        self.count = 0
        self.owner = ""

    def add_plant(self, plant: Plant):
        new_list = [None] * (self.count + 1)
        i = 0
        while (i < self.count):
            new_list[i] = self.collection[i]
            i += 1
        new_list[i] = plant
        self.collection = new_list
        self.count += 1

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        i = 0
        while (i < self.count):
            i+= 1
            plant = self.collection[i]
            print(f"- {plant.describe()}")

class GardenManager:

    def __init__(self, name: str):
        self.name = name
        self.gardens = []
    
    @staticmethod

    @classmethod
    def create_garden_network(cls):
        return f"{cls.count}"

    class GardenStats:
        def __init__(self):
        





def main():


if __name__ == "__main__":
    main()
