print("Program starting.")
print("Unit conversion program with submenus")

while True:
    # Main menu
    print("\nMain Menu:")
    print("1 - Length")
    print("2 - Weight")
    print("0 - Exit")

    choice = input("Your choice: ")

    if choice == "1":
        # Length submenu
        print("\nLength conversions:")
        print("1 - Meters to kilometers")
        print("2 - Kilometers to meters")

        sub_choice = input("Your choice: ")

        if sub_choice == "1":
            meters = float(input("Insert meters: "))
            kilometers = meters / 1000
            print(f"{round(meters, 1)} m is {round(kilometers, 1)} km")

        elif sub_choice == "2":
            kilometers = float(input("Insert kilometers: "))
            meters = kilometers * 1000
            print(f"{round(kilometers, 1)} km is {round(meters, 1)} m")

        elif sub_choice == "0":
            print("Exiting...")
            print("Program ending.")
            break

        else:
            print("Unknown option.")

    elif choice == "2":
        # Weight submenu
        print("\nWeight conversions:")
        print("1 - Grams to pounds")
        print("2 - Pounds to grams")

        sub_choice = input("Your choice: ")

        if sub_choice == "1":
            grams = float(input("Insert grams: "))
            pounds = grams / 453.59237   # 1 pound = 453.59237 g
            print(f"{round(grams, 1)} g is {round(pounds, 1)} lb")

        elif sub_choice == "2":
            pounds = float(input("Insert pounds: "))
            grams = pounds * 453.59237
            print(f"{round(pounds, 1)} lb is {round(grams, 1)} g")

        elif sub_choice == "0":
            print("Exiting...")
            print("Program ending.")
            break

        else:
            print("Unknown option.")

    elif choice == "0":
        print("Exiting...\n")
        print("Program ending.")
        break
        

    else:
        print("Unknown option.")

