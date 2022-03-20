class Heroes:
    life_points = 100
    kick = 15
    punch = 15
    special_power = 20
    name = ""

    def throw_a_punch ():
        pedro.life_points = pedro.life_points - pedro.punch 
        return (pedro.life_points)

    def throw_a_kick ():
        name.life_points = name.life_points - name.kick
        return (name.life_points)

    def throw_a_special (self, name):
        name.life_points = name.life_points - name.special_power 
        return (name.life_points)


pedro = Heroes()
pedro.kick = 19

jason = Heroes()
jason.punch = 50

def get_attack ():
    contender = input ("who are you attacking?: ")
    attack = input ("what skill would you like to use?: ")
    return contender, attack

while pedro.life_points >0 and jason.life_points >0:
    contender, attack =   get_attack()
    if contender == "pedro" and attack == "punch":
        pedro.life_points = jason.throw_a_punch(contender)

if pedro.life_points <= 0:
    print ("jason wins")







