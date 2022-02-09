x = input("which number => ")
num = int(x)
while num > 1:
    if num % 2 == 1:
        num = (num * 3) + 1
        print(num)
    elif num % 2 != 1:
        num = num / 2
        print(num)