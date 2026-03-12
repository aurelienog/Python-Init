#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return None

    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return None

    return temp


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    print("Testing temperature: 25")
    temp = check_temperature("25")
    if temp is not None:
        print(f"Temperature {temp}°C is perfect for plants!")

    print("\nTesting temperature: abc")
    temp = check_temperature("abc")
    if temp is not None:
        print(f"Temperature {temp}°C is perfect for plants!")

    print("\nTesting temperature: 100")
    temp = check_temperature("100")
    if temp is not None:
        print(f"Temperature {temp}°C is perfect for plants!")

    print("\nTesting temperature: -50")
    temp = check_temperature("-50")
    if temp is not None:
        print(f"Temperature {temp}°C is perfect for plants!")
    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    test_temperature_input()


if __name__ == "__main__":
    main()
