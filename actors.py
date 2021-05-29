import random
from typing import Text
from termcolors import bcolors
from textstrings import TextStrings
import pyinputplus


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items, type):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = [TextStrings.str26, TextStrings.str27, TextStrings.str28]
        self.name = name
        self.type = type
        self.dead = False

    def generate_damage(self):
        if self.dead == False:
            return random.randrange(self.atkl, self.atkh)
        else:
        #    print(bcolors.FAIL + self.name +  " OBJECT IS DEAD AND CANNOT GENERATE DAMAGE!")
            return 0


    def take_damage(self,dmg):
        if self.dead == False:
            self.hp -= dmg
            if self.hp < 0:
                self.hp = 0
                self.die()
        return self.hp
        

    def die(self):
        print (TextStrings.str12 % self.name)
        self.dead = True


    def heal_spell(self, health_spell):
        if self.dead == False:
            heal = health_spell.generate_damage(health_spell)
            self.hp += heal
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            print(TextStrings.str13 % (self.name, health_spell.name, str(heal)))
        #else:
        #    print(bcolors.FAIL + self.name +  " OBJECT IS DEAD AND CANNOT HEAL!")

    def heal_item(self, health_item):
        if self.dead == False:
            heal = health_item.prop
            self.hp += heal
            if self.hp > self.maxhp:
                self.hp = self.maxhp
            print(TextStrings.str14 % (self.name, health_item.name, str(heal)))
        #else:
        #    print(bcolors.FAIL + self.name +  " OBJECT IS DEAD AND CANNOT USE ITEM!")

    def elixir_item(self, elixir_item):
        if self.dead == False:
            self.hp = self.maxhp
            self.mp = self.maxmp
            print(TextStrings.str15 % (self.name, elixir_item.name))
        #else:
        #    print(bcolors.FAIL + self.name +  " OBJECT IS DEAD AND CANNOT USE ELIXIR!")

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(TextStrings.str16, "[", end='')
        for item in self.actions:
            print(str(i) , "==" , item + "  " , end='')
            i += 1
        print("]\n", bcolors.ENDC)
        self.get_stats()

    def choose_magic(self):
        i = 1
        print(TextStrings.str17)
        for spell in self.magic:
            print(TextStrings.str29 % (str(i), spell.name, str(spell.cost)))
            #print(str(i) + ".", spell.name, "(cost: ", str(spell.cost) + ")" )
            i += 1
        return i-1

    def choose_item(self):
        i = 1
        print(TextStrings.str18)
        for item in self.items:
            print(TextStrings.str30 % (str(i), item.name, str(item.quantity), item.description))
            #print(bcolors.OKGREEN + str(i) + bcolors.ENDC + ".", bcolors.WARNING, item.name, bcolors.ENDC,  ":", item.description, "(x" + str(item.quantity) + ")")
            i += 1
        return i-1       

    def choose_target(self, enemies):
        i=1

        print(TextStrings.str19)
        for enemy in enemies:
            if enemy.get_hp() > 0:
                print (str(i) + "." , end='')
                enemy.get_stats()
                i +=1
        if i > 1:
            choice = int(pyinputplus.inputNum (prompt=TextStrings.str20, min=1, max=i-1)) -1
        else: 
            choice = 0
        return choice
            

    def get_stats(self):

        hp_bar = ""
        hp_bar_ticks = (self.hp / self.maxhp) * 100 / 4

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxmp) * 100 / 10

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1     
        
        if self.type == "player":
            print(TextStrings.str21 % ((self.name).ljust(10),str(self.hp).ljust(4),str(self.maxhp).ljust(4),hp_bar.ljust(25),str(self.mp).ljust(3),str(self.maxmp).ljust(3),mp_bar.ljust(10)))
            
        elif self.type == "enemy":
            print(TextStrings.str22 % ((self.name).ljust(10),str(self.hp).ljust(4),str(self.maxhp).ljust(4),hp_bar.ljust(25),str(self.mp).ljust(3),str(self.maxmp).ljust(3),mp_bar.ljust(10)))

    @staticmethod
    def persons_alive(persons):
        persons_alive = 0

        for person in persons:
            if person.get_hp() > 0:
                persons_alive += 1
        return persons_alive


    def attack(self, attack_target):
        target = attack_target
        dmg = self.generate_damage()
        print(TextStrings.str23 % (self.name, target.name, str(dmg)))
        target_health = target.take_damage(dmg)
        return dmg

    def attack_magic(self, attack_target, spell):
        target = attack_target
        dmg = spell.generate_damage(spell)
        print(TextStrings.str24 % (self.name, spell.name, str(dmg), target.name))
        target_health = target.take_damage(dmg)
        return dmg

    def attack_item(self, attack_target, item):
        target = attack_target
        dmg = item.prop
        print(TextStrings.str25 % (self.name, item.name, str(dmg), target.name))
        target_health = target.take_damage(dmg)
        return dmg
