#dogAge = int(input("What is your dog's age: "))
#dogAge*=7
#print("You dog is", dogAge, "years old.")

#number = int(input("Enter a whole number: "))
#if (number % 2) == 0:
#    print("Your number is even.")
#else:
#    print("Your number is odd")


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
    goToGo = input(", do you have to go? (True/False) ")
    if(goToGo == "True"):
        print("Goodbye ", name)
    else:
        greeting()

greeting()


