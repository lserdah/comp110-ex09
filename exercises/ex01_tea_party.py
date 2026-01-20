"""A program that asks for the number of guests and calculates the amount of tea,
treats, and total cost needed for a tea party."""

__author__: str = "730577014"


def main_planner (guests:int) -> None:
    """Prints out the total number of tea bags, treats, and total cost for the tea party."""
    print("A Cozy Tea Party for " +str(guests) +" People!")

    tea: int= tea_bags(people=guests)
    print ("Tea Bags: " + str(tea))

    treat:int= treats(people=guests)
    print ("Treats: " + str(treat))

    total_cost: float= cost(tea_count=tea, treat_count=treat)
    print ("Cost: $" + str(total_cost))

def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed for the given number of people."""
    return people * 2

def treats(people: int) -> int:
    """Calculates the number of treats needed for the given number of people."""
    teas: int = tea_bags(people=people)
    return int(teas * 1.5)

def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of tea bags and treats."""
    tea_cost: float = tea_count * 0.5
    treat_cost: float = treat_count * 0.75
    return tea_cost + treat_cost

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

