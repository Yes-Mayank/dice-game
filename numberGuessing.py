import random

randomNum = random.randint(0 , 100)

while True:
    try:
        user_input = int(input("guess the number in b/w 0-100: "))


        if user_input > randomNum+10:
            print("too big")
        
        elif user_input > randomNum < randomNum+10:
            print("big")

        elif user_input < randomNum-10:
            print("too small ")   

        elif user_input < randomNum >randomNum-10:
            print("small")  

        else:
            print("yeah, you did it")    
            break   
    except ValueError:
        print(" pls, enter valid number")


