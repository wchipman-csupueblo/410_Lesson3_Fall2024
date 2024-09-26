#!/usr/bin/env python3

import conversions as c

def display_welcome():
    print("Feet and Meters Converter")
    print()

def display_menu():
    print("Conversion Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")

def main():
    #display the welcome message
    display_welcome()
    
    #loop that allows for multiple runs
    again = "y"
    while again.lower() == "y":
        #display the menu
        display_menu()
        choice = input("Select a conversion (a/b): ")
        print()
        #Based on choice call appropriate conversion function
        if choice == "a":
            feet = float(input("Enter feet: "))
            meters = c.to_meters(feet)
            print(round(meters, 2), "meters")
        elif choice == "b":
            meters = float(input("Enter meters: "))
            feet = c.to_feet(meters)
            print(f"{round(feet, 2)} feet")
        else: 
            print("You did not enter a valid selection.")
        print()

        again = input("Would you like to perform another conversion? (y/n): ")
        print()

    # exit the program
    print("Thanks, bye!")


if __name__ == "__main__":
    main()