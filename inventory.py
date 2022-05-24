import random
import db

class BaseAttack():
    def __init__(self, id, name, damage, crit, chain, final=False):
        self.id = id # int, cannot be 1
        self.name = name # str
        self.damage = damage # int
        self.crit = crit # int
        self.chain = chain # int
        self.final = final
        self.second_phase = False
        
    def execute(self, player, objective): 
        return 
        

        

class Player():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.attacks = [1, 1, 1, 1]
        self.hp = 30
        self.dmg_mod = 0
        self.incomming_dmg_mod = 0

    def attack(self, attack, objective):
