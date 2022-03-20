
year= int(input(""))
leap = False
def leap_year():
    if year % 4 == 0 and year % 400 ==0:
        leap = True
        print(leap)
    else:
        print (False)


leap_year()