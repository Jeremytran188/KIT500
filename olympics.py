"""
3.2PP Fill in the Blanks: Paris Olympics
"""

__author__ = "Ngoc Kien Tran"


def main():
    # 1. Display title
    print("Paris 2024 Medal Tally")
    print()

    # 2–4. Inputs
    first_place: str = input("Enter the name of the country in first place: ")
    capital_city: str = input("Enter the capital city of that country: ")
    second_place: str = input("Enter the name of the country in second place: ")

    # 5–6. Gold medals
    gold_medals_1: int = int(input("How many gold medals has the first-placed country won? "))
    gold_medals_2: int = int(input("How many gold medals has the second-placed country won? "))

    # 7. Calculate margin
    margin: int = gold_medals_1 - gold_medals_2

    print()  # spacing

    # 8. Output messages
    print(f"{first_place} currently tops the 2024 Paris Olympics' medal tally with {gold_medals_1} gold.")
    print(f"Citizens of {capital_city} are overjoyed at beating arch-rivals {second_place}.")
    print(f"Their lead of {margin} gold looks secure with only competitive programming left.")


if __name__ == "__main__":
    main()