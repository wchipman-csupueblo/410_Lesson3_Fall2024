#!/usr/bin/env python3

def display_title():
    pass

def to_feet(miles):
    pass

def main():
    display_title()
    miles = float(input("How many miles did you walk?   "))
    feet = to_feet(miles)
    print(f"You walked {feet} feet.")


if __name__ == "__main__":
    main()