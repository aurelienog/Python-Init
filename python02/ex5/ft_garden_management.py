#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for garden-related errors"""
    pass


class PlantError(GardenError):
    """Raised when there is a plant problem"""
    pass


class WaterError(GardenError):
    """Raised when there is a water problem"""
    pass


class Plant:
    def __init__(self, name: str, water: int) -> None:
        self.name = name
        self.water = water
        self.sunlight_hours = 8


class GardenManager:
    def __init__(self, name: str) -> None:
        self.name = name
        self.collection = []
        self.total = 0

    def add_plants(self, plants: list) -> None:
        print("Adding plants to garden...")
        i = 0
        while i < len(plants):
            try:
                plant = plants[i]
                if not plant:
                    raise PlantError("Plant name cannot be empty!")
                else:
                    if i % 2 == 0:
                        water = 4
                    else:
                        water = 14
                    new = Plant(plant, water)
                    self.collection.append(new)
                    print(f"Added {new.name} successfully")
                self.total += 1
            except Exception as e:
                print(f"Error adding plant: {e}")
            i += 1

    def water_plants(self) -> None:
        i = 0
        print("Watering plants...\nOpening watering system")
        try:
            while i < self.total:
                self.collection[i].water += 1
                print(f"Watering {self.collection[i].name} - success")
                i += 1
        finally:
            print("Closing watering system (cleanup)")

    @staticmethod
    def check_plant_health(plant: Plant) -> str:
        if not plant.name:
            raise ValueError("Error: Plant name cannot be empty!")
        if plant.water < 1:
            raise WaterError(f"Error: Water level {plant.water} "
                             "is too low (min 1)")
        elif plant.water > 10:
            raise WaterError(
                f"{plant.name}: Water level {plant.water} is too high (max 10)"
                )
        if plant.sunlight_hours < 2:
            raise GardenError(
                f"Error: Sunlight hours {plant.sunlight_hours}"
                "is too low (min 2)")
        elif plant.sunlight_hours > 12:
            raise GardenError(
                f"Error: Sunlight hours {plant.sunlight_hours}"
                "is too high (min 2)"
                )
        return f"Plant '{plant.name}' is healthy!"


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    manager = GardenManager("manager")
    plants = ["tomato", "lettuce", ""]
    manager.add_plants(plants)
    print("")
    manager.water_plants()
    print("\nChecking plant health...")
    i = 0
    while (i < manager.total):
        try:
            plant = manager.collection[i]
            manager.check_plant_health(plant)
            print(f"{plant.name}: healthy (water: {plant.water},",
                  f"sun: {plant.sunlight_hours})")
        except Exception as e:
            print("Error checking " + f"{e}")
        i += 1
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}\nSystem recovered and continuing...")
    finally:
        print("\nGarden management system test complete!")


def main() -> str:
    test_garden_management()


if __name__ == "__main__":
    main()
