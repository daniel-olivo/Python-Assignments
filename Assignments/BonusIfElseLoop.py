#Version 1: with if else
'''
def greeting():
    name = input("Please enter you name: ")
    print("Nice to meet you ", name)
    #print(name, end="")
    color = input(name, ", what is your favorite color: ")
    #print(color, end="")
    print(color, "? That's a nice color.")
    #print(name, end="")
    food = input(name, ", what is your favorite food: ")
    #print(food, end="")
    print(name, " sounds yummy.")
    #print(name, end="")
    goToGo = input(name, ", do you have to go? (yes/no) ")
    if(goToGo == "yes"):
        print("Goodbye ", name)
    else:
        greeting()

greeting()
'''
#Version 2: with if else
print("This is where version 2 starts")
goToStart = "no"
while goToStart == "no":
    name = input("Please enter you name: ")
    print("Nice to meet you ", name)
    color = input("{},what is your favorite color: ".format(name))
    print("{}?, That's a nice color.".format(color))
    food = input("{}, what is your favorite food: ".format(name))
    print("{} sounds yummy.".format(food))
    goToStart = input("{}, do you have to go? (yes/no) ".format(name))

print("Goodbye ")
