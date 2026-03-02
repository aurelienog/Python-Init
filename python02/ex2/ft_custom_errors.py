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


def create_plant_error() -> None:
    plant_height = 5
    if plant_height < 10:
        raise PlantError("The tomato plant is wilting!")


def create_water_error() -> None:
    water = 0
    if water < 10:
        raise WaterError("Not enough water in the tank!")


def catching_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError..")
    try:
        create_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        create_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        create_plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        create_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print("\nAll custom error types work correctly!")


# def main() -> None:
#     catching_errors()


# if __name__ == "__main__":
#     main()
