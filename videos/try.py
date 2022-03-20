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

heroes = ["jason", "juan"]

collection_heroes = 

for heroe in heroes:

