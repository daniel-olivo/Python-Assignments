#Version 1: with if else
def greeting():
    name = input("Please enter you name: ")
    print("Nice to meet you ", name)
    print(name, end="")
    color = input(", what is your favorite color: ")
    print(color, end="")
    print("? That's a nice color.")
    print(name, end="")
    food = input(", what is your favorite food: ")
    print(food, end="")
    print(" sounds yummy.")
    print(name, end="")
    goToGo = input(", do you have to go? (yes/no) ")
    if(goToGo == "yes"):
        print("Goodbye ", name)
    else:
        greeting()

greeting()

#Version 2: with if else
print("This is where version 2 starts")
goToStart = "no"
while goToStart == "no":
    name = input("Please enter you name: ")
    print("Nice to meet you ", name)
    color = input(name, ", what is your favorite color: ")
    print(color, "? That's a nice color.")
    food = input(name, ", what is your favorite food: ")
    print(food," sounds yummy.")
    goToStart = input(name,", do you have to go? (yes/no) ")

print("Goodbye ")