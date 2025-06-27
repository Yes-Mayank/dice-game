import random

count =0
while True and count <= 2:
    choice =input("wanna roll? (yes/no) " ).lower()
    if choice == "yes":
        die1= random.randint(1, 6)
        die2= random.randint(1, 6)
        count +=1
        print(f"{die1} , {die2}")


    elif choice == "no":
        print("thanks for your time")
        break
    else:
        print("invalid input")

if count == 3:
    print("game over")


