import random
from tqdm import tqdm
import time

class Heroes:
    def __init__(self, life_points, kick, punch, special_power):
        self.life_points = life_points
        self.kick = kick
        self.punch = punch
        self.special_power = special_power

    def throw_an_attack(self, contender, kind_attack):
        if kind_attack == 'punch':
            attack_points = self.punch
        elif kind_attack == 'kick':
            attack_points = self.kick
        elif kind_attack == 'special':
            attack_points = self.special_power
        else:
            attack_points = 0
            print("it doesnt a valid attack")
        contender.life_points = contender.life_points - attack_points
        return (contender.life_points)


def get_attack ():
    attack = input ("what skill would you like to use?: ")
    return attack

def build_heroes():
    print("Define characteristics for Pedro")
    kick = int(input("Kick power: "))
    punch = int(input("Punch power: "))
    special = int(input("Special power: "))
    pedro = Heroes(100, kick , punch, special)
    print("")
    print("Define characteristics for Jason")
    kick = int(input("Kick power: "))
    punch = int(input("Punch power: "))
    special = int(input("Special power: "))
    jason = Heroes(100, kick , punch, special)
    return pedro, jason
    

def get_progress_bar(life_points, contender_name):
    for i in tqdm (range (life_points),desc=contender_name,total = 100,  ncols=75):
        time.sleep(0.01)
    

def main():
    pedro, jason = build_heroes()
    turno = 0

    while pedro.life_points >0 and jason.life_points >0:
        random_number = random.random()
        if random_number > 0.5 : turno = 1   
        if turno == 0:
            print("") 
            time.sleep(0.01)
            print("Jason attacks") 
            attack =   get_attack()
            jason.throw_an_attack(pedro, attack)
            get_progress_bar(jason.life_points, "Jason's life points")
            get_progress_bar(pedro.life_points, "Pedro's life points")
        elif turno == 1:
            print("")
            time.sleep(0.01)
            print("Pedro attacks")        
            attack =   get_attack()
            pedro.throw_an_attack(jason, attack)
            get_progress_bar(jason.life_points, "Jason's life points")
            get_progress_bar(pedro.life_points, "Pedro's life points")

    if pedro.life_points <= 0:
        print ("Jason wins")
    else:
        print ("Pedro wins")