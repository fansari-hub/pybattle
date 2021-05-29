import random

class Spell:

    #create Black Magic
    fire = ("Fire", 15, 600, "black")
    thunder = ("Thunder", 15, 600, "black")
    blizzard = ("Blizzard", 15, 600, "black")
    meteor = ("Meteor", 25, 1200, "black")
    quake = ("Quake", 18, 800, "black")

    #create White Magic
    cure = ("Minor Cure", 20, 620, "white")
    cura = ("Major Cure", 35, 1500, "white")

    black_magic = [fire, thunder, blizzard, meteor, quake]
    white_magic = [cure, cura]

    player_magic = black_magic + white_magic
    enemy_magic = black_magic + white_magic
    


    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type
    
    def generate_damage(self, i):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low,high)

    @staticmethod
    def get_players_magic_list():
            return Spell.player_magic
    
    @staticmethod
    def get_enemies_magic_list():
            return Spell.enemy_magic

    @staticmethod
    def get_white_magic_list():
            return Spell.white_magic

    @staticmethod
    def get_black_magic_list():
            return Spell.black_magic

