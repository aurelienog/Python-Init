def ft_water_reminder():
    last = input("Days since last watering: ")
    if (int(last) > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
