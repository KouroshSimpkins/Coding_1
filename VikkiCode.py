
try:
    number = float(input("Input a number: "))
    if number % 2 == 0:
        print("{0} is even number".format(number))
    else:
        print("{0} is odd number".format(number))
except ValueError:
    print("You must input a number")

first = input()

count = 0

for i in range(0, 10,):
    if i % 2 == 0:
        count += 1

print(count)