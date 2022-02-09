import random

def face1():
    print("===========")
    print("|         |")
    print("|    O    |")
    print("|         |")
    print("===========")

def face2():
    print("===========")
    print("|    O    |")
    print("|         |")
    print("|    O    |")
    print("===========")

def face3():
    print("===========")
    print("|        O|")
    print("|    O    |")
    print("|O        |")
    print("===========")

def face4():
    print("===========")
    print("|O       O|")
    print("|         |")
    print("|O       O|")
    print("===========")

def face5():
    print("===========")
    print("|O       O|")
    print("|    O    |")
    print("|O       O|")
    print("===========")

def face6():
    print("===========")
    print("|O   O   O|")
    print("|         |")
    print("|O   O   O|")
    print("===========")

dice_faces = [face1, face2, face3, face4, face5, face6]
role = True
while role == True:
    x = random.randint(0,5)
    dice_faces[x]()
    input("press enter to play")