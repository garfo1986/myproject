# we use raise to include an error, this error must be a known one or must be created as a class, you can also add a string which will pop out along with the error:


def age(old):


    if old < 0:
    # the string doesn't have to be exactly what the error indicates, we can include anything in there.
        raise NameError ("that's not a valid input")


    elif old < 20:
        print ("you're very young")
    elif old < 40:
        print ("you're young")
    elif old < 60:
        print ("you're mature")
    elif old < 100:
        print ("be careful")
    elif old >= 100:
        print ("you're a legend")

old = int(input("what is your age?: "))
age(old)