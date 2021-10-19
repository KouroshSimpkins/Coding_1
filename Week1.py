"""Week 1 of Coding 1"""

try:
    value = float(input(("Please input a number to test: ")))

    if value%2 == 0:
        print("even")
    else:
        print("odd")


except ValueError:
    print("That's not a number")
