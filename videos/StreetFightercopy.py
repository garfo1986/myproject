import random



class Heroes:
    def __init__ (self, lifepoints, punch, kick, special_power):
        self.lifepoints = lifepoints
        self.punch = punch
        self.kick = kick
        self.special_power = special_power

    def throw_an_attack (self, contender, kind_attack):
        if kind_attack == "punch":
            attack_points = self.punch
        elif kind_attack == "kick":
            attack_points = self.kick
        elif kind_attack == "special_power":
            attack_points = self.special_power
        else:
            attack_points = 0
            print ("invalid attack")
        contender.lifepoints = contender.lifepoints - attack_points
        return contender.lifepoints

    def throw_a_defense_attack (self, contender, kind_attack):
        if kind_attack == "punch":
            attack_points = self.punch
        elif kind_attack == "kick":
            attack_points = self.kick
        elif kind_attack == "special_power":
            attack_points = self.special_power
        else:
            attack_points = 0
            print ("invalid attack")
        contender.lifepoints = contender.lifepoints - (attack_points//2)
        return contender.lifepoints

    
def get_attack():
    attack = input("what attack would you like to use?: ")
    return attack

#pedro = Heroes(100, 5, 6, 8)

def build_heroe():
    print ("let's define Pedro's skills!: ")
    kick = int(input("kick power: "))
    punch = int(input("punch power: "))
    special_power= int (input("Special power: "))
    pedro = Heroes (100, punch, kick, special_power)
    print ("")
    print ("let's define Jason's skills!: ")
    kick = int(input("kick power: "))
    punch= int(input("punch power: "))
    special_power = int(input("Special power: "))
    jason =Heroes(100, punch, kick, special_power)
    return pedro, jason 



def main():
    pedro, jason =build_heroe()
    turn=0
    defense = ("N")

    while pedro.lifepoints > 0 and jason.lifepoints >0:
        random_number = random.random()
        #if random_number > 0.5:
         #   turn = 1 
        if turn == 0:
        
            print ("jason attacks!")
            attack = get_attack()
            defense = input ("Pedro, would you like to defend?: Y/N: ")
            if defense == ("N"):
                jason.throw_an_attack(pedro, attack)
                print ("Pedro's life points are ", pedro.lifepoints)
                print ("")
                turn = 1   
            elif defense == ("Y"):
                jason.throw_a_defense_attack(pedro, attack)
                print ("pedro's life points are", pedro.lifepoints)
                print ("")
                turn = 0

        elif turn == 1:
            print ("Pedro attacks!")
            attack = get_attack()
            defense = input ("Jason, would you like to defend?: Y/N: ")
            if defense == ("N"):
                pedro.throw_an_attack(jason, attack)
                print ("Jason's life points are: ", jason.lifepoints)
                print ("")
                turn = 0
            elif defense == ("Y"):
                pedro.throw_a_defense_attack(jason, attack)
                print ("Jason's life points are", jason.lifepoints)
                print("")
                turn = 1
            
    if pedro.lifepoints <= 0:
        print ("Jason wins")
    else:
        print("Pedro wins")

main()




