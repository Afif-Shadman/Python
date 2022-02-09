import random 

difficulty = input("choose your difficulty easy(E) medium(M) hard(H) =>").lower()


if difficulty == "e":
    x = 50
elif difficulty == "m":
    x = 100
elif difficulty == "h":
    x = 1000

number = random.randint(1 , x)
 
guess = int(input("guess any number between 0 and " + str(x) + " =>"))

gameover = False

while gameover == False:
    if guess > x:
        guess = int(input("try something lower =>"))
    elif guess < x:
        guess = int(input("try something between higher =>"))
    elif guess == x:
        print("you got it correct")
        gameover = True