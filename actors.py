import random
from typing import Text
from termcolors import bcolors
from textstrings import TextStrings
from objectstats import ObjectStats
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
            i += 1
        return i-1

    def choose_item(self):
        i = 1
        print(TextStrings.str18)
        for item in self.items:
            print(TextStrings.str30 % (str(i), item.name, str(item.quantity), item.description))
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

        if self.type == "player":
             player_health_stats = ObjectStats(actor_name=self.name, actor_name_len=10, actor_name_color=bcolors.OKBLUE, current_value=self.hp, value_max=self.maxhp, bar_size=20, stat_name="HP", newline=False, bar_color=bcolors.OKGREEN)
             player_health_stats.print_stats()
             player_magic_stats = ObjectStats(current_value=self.mp, value_max=self.maxmp, bar_size=10, stat_name="MP", newline=True, bar_color=bcolors.OKBLUE)
             player_magic_stats.print_stats()
            
        elif self.type == "enemy":
             enemy_health_stats = ObjectStats(actor_name=self.name, actor_name_len=10, actor_name_color=bcolors.FAIL, current_value=self.hp, value_max=self.maxhp, bar_size=20, stat_name="HP", newline=False, bar_color=bcolors.FAIL)
             enemy_health_stats.print_stats()
             enemy_magic_stats = ObjectStats(current_value=self.mp, value_max=self.maxmp, bar_size=10, stat_name="MP", newline=True, bar_color=bcolors.WARNING)
             enemy_magic_stats.print_stats()

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
