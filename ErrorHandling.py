ValidInput=False
while(ValidInput==False):
    try:
        a=int(input("Enter a number between 1 - 10: ")) # any text will fail
        squared = a*a
        print(a, "Squared is ", squared)
        ValidInput=True
    except:
        print("Please enter a numerical value between 1 - 10!")