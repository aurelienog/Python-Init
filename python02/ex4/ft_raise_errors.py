#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} is too low (min 1")
    elif water_level > 10:
        raise ValueError(f"Error: Water level {water_level}",
                         "is too high (max 10")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}",
                         "is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours}",
                         "is too high (min 2)")
    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")
    print("\nTesting good values...")
    print(check_plant_health("tomato", 5, 8))
    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 5, 8)
    except Exception as e:
        print(e)
    print("\nTesting bad water level..")
    try:
        check_plant_health("tomato", 15, 8)
    except Exception as e:
        print(e)
    try:
        print("\nTesting bad sunlight hours...")
    except Exception as e:
        print(e)
    try:
        check_plant_health("tomato", 5, 0)
    except Exception as e:
        print(e)
    print("\nAll error raising tests completed!")


# def main() -> None:
#     test_plant_checks()


# if __name__ == "__main__":
#     main()
