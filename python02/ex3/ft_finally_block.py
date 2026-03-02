#!/usr/bin/env python3

def water_plants(plant_list):
    i = 0
    print("Opening watering system")
    try:
        while i < 3:
            plant = plant_list[i]
            if not plant:
                raise Exception("Error: Cannot water None - invalid plant!")
            else:
                print(f"Watering {plant}")
            i += 1
    except Exception as e:
        print(f"{e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    plants = ["tomato", "lettuce", "carrots"]
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    try:
        water_plants(plants)
    finally:
        print("Watering completed successfully!")
    plants = ["tomato", "", "Sunflower"]
    print("\nTesting with error...")
    water_plants(plants)
    print("\nCleanup always happens, even with errors!")


# def main():
#     test_watering_system()


# if __name__ == "__main__":
#     main()
