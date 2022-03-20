import random
try:
    def guess_the_number(x):
    
    
        print("============")
        print(  "Hello!")
        print("============")
        print(f"in this game, you will have to guess a computer generated random number from 1 to {x}")

        number = random.randint(1, x)
        guessn = 0

        while guessn != number:
            guessn= int(input("what is your guess?: "))

            if guessn < number:
                print("try again, this number is lower than my number")
            elif guessn > number:
                print("try again, this number is higher than my number")
        print (f"congratulations! you have guessed the {number} number!")        


    guess_the_number(20)
except:
    print("that's not a valid number")