secret_word = "yeison"
guessed_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guessed_word != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guessed_word = input("what is my name?: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:  
    print ("you don't know my name!!! :(")
else:
    print ("you have won")