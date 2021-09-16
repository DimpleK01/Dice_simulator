import random
print("-----DICE SIMULATOR-----")
roll = 'r'
while (roll=='r'):
    roll = input("press r to roll the dice  ")
    face = random.randint(1,6)
    if face== 1:
        print(" ______")
        print("|      |")
        print("|  0   |")
        print("|      |")
        print(" ______ ")

    elif face==2:
        print(" ______")
        print("|  0   |")
        print("|      |")
        print("|  0   |")
        print(" ______ ")

    elif face==3:
        print(" ______")
        print("|  0   |")
        print("|  0   |")
        print("|  0   |")
        print(" ______ ")

    elif face==4:
        print(" ______")
        print("| 0  0 |")
        print("|      |")
        print("| 0  0 |")
        print(" ______ ")

    elif face==5:
        print(" ______")
        print("| 0  0 |")
        print("|  0   |")
        print("| 0  0 |")
        print(" ______ ")

    elif face==6:
        print(" ______")
        print("| 0  0 |")
        print("| 0  0 |")
        print("| 0  0 |")
        print(" ______ ")