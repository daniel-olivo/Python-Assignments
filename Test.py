def thermometer(a):
    if a > 60 and a < 90:
        print("It is warm outside!!!")
    elif a >= 90:
        print("It is hot outside!!!")
    elif a < 60:
        print("It is cold outside!!!")
def main():
    thermometer(91)

main()



