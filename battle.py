from termcolors import bcolors
from actors import Person
from magic import Spell
from inventory import Item
from enemyList import EnemiesList
from playersList import PlayersList
from textstrings import TextStrings
import random
import os
import pyinputplus

class battle_event():

    def cleanup_battlefield(self, enemies,players):
        battle_over = False

        for player in players:
            if player.get_hp() <= 0:
                del players[players.index(player)]
        
        for enemy in enemies:
            if enemy.get_hp() <= 0:
                del enemies[enemies.index(enemy)]

        if (Person.persons_alive(players) <=0) or (Person.persons_alive(enemies) <=0):
            battle_over = True
        return battle_over


    def begin_battle(self):
        #instantate objects
        player_magic = []
        enemy_magic = []
        player_items = []
        players = []
        enemies = []

        for pm in Spell.get_players_magic_list():
            player_magic.append(Spell(*pm))

        for em in Spell.get_enemies_magic_list():
            enemy_magic.append(Spell(*em))

        for pi in Item.get_player_items():
            player_items.append(Item(*pi))

        for player in PlayersList.get_players():
            players.append(Person(*player, player_magic, player_items, "player"))

        for enemy in EnemiesList.get_enemies():
            enemies.append(Person(*enemy, enemy_magic, [], "enemy"))


        #begin game loop
        running = True
        turn = 0
        spawn_count = 0


        while running:
            turn +=1
            os.system('cls' if os.name == 'nt' else 'clear')
            print (TextStrings.str1 % str(turn))
            
            #end of game check 
            if Person.persons_alive(enemies) <= 0:
                print(TextStrings.str2)
                running = False
                continue

            elif Person.persons_alive(players) <= 0:
                print(TextStrings.str3)
                running = False
                continue
            
            print(TextStrings.str0)

            for player in players:
                player.get_stats()
            print("")
            for enemy in enemies:
                enemy.get_stats()   
            
            print(TextStrings.str0)
            #player move
            for player in players:
                player.choose_action()
                choice = pyinputplus.inputChoice(choices=["1","2","3","-1"], prompt=TextStrings.str4 + bcolors.OKBLUE + player.name + bcolors.ENDC + ":" )
                index = int(choice) - 1

                #player attack
                if index == 0:
                    enemy = player.choose_target(enemies)
                    dmg = player.attack(enemies[enemy])
                    if self.cleanup_battlefield(enemies,players) == True:
                        break
                
                #player cast spell 
                elif index == 1:
                    magic_max = player.choose_magic()
                    magic_choice = int(pyinputplus.inputNum(prompt=TextStrings.str5 ,min=0, max=magic_max)) -1


                    if magic_choice == -1:
                        continue
                
                    spell = player.magic[magic_choice]
                    current_mp = player.get_mp()

                    if spell.cost > current_mp:
                        print(bcolors.FAIL + TextStrings.str6 + bcolors.ENDC)
                        continue
                    
                    player.reduce_mp(spell.cost)
                    if spell.type == "white":       
                        player.heal_spell(spell)
                    elif spell.type == "black":
                        enemy = player.choose_target(enemies)
                        dmg = player.attack_magic(enemies[enemy], spell)
                        if self.cleanup_battlefield(enemies,players) == True:
                            break
                

                #player choose items
                elif index == 2:
                    item_max = player.choose_item()
                    item_choice = int(pyinputplus.inputNum(prompt=TextStrings.str7, min=0, max=item_max)) -1
                    
                    if item_choice == -1:
                        continue

                    item = player.items[item_choice]

                    if player.items[item_choice].quantity == 0:
                        print (TextStrings.str8)
                        continue
                    
                    player.items[item_choice].quantity -= 1
                    
                    if item.type == "potion":
                        player.heal_item(item)

                    elif item.type == "elixir":
                        if item.name == "Mega Elixir":
                            for i in players:
                                i.elixir_item(item)
                        else:
                            player.elixir_item(item)
                    
                    elif item.type == "attack":
                        enemy = player.choose_target(enemies)
                        dmg = player.attack_item(enemies[enemy], item)
                        if self.cleanup_battlefield(enemies,players) == True:
                            break


            #enemy move
            for enemy in enemies:
                enemy_choice = random.randrange(0,2)
                #enemy_choice = 1

                if self.cleanup_battlefield(enemies,players) == True:
                            break
            
                if enemy_choice == 0:
                    target = random.randrange(0,len(players))
                    enemy_dmg = enemy.attack(players[target])
                    

                elif enemy_choice == 1:
                    if (enemy.get_hp() / enemy.get_max_hp() * 100) < 30:
                        for i in enemy.magic:
                            if i.name == "Minor Cure":
                                spell = i
                    elif (enemy.get_hp() / enemy.get_max_hp() * 100) < 15:
                        for i in enemy.magic:
                            if i.name == "Major Cure":
                                spell = i
                    else:
                        magic_choice = random.randrange(0, len(Spell.get_black_magic_list()))
                        spell = enemy.magic[magic_choice]
                    
                    current_mp = enemy.get_mp()

                    if spell.cost < current_mp:
                        enemy.reduce_mp(spell.cost)
                        
                        if spell.type == "white":
                            enemy.heal_spell(spell)
                    
                        elif spell.type == "black":
                            target = random.randrange(0,len(players))
                            dmg = enemy.attack_magic(players[target], spell)

                    else: #if the enemy is out of MP, attack instead!
                        target = random.randrange(0,len(players))
                        enemy_dmg = enemy.attack(players[target])

                if enemy_choice == 2:
                    print("not implemented!")

                text = input(TextStrings.str9)

            spawn_chance = random.randrange(0,10)
            if spawn_chance == 5:
                spawn_count += 1
                enemies.append(Person (name ="Ninja" + str(spawn_count), hp=random.randrange(750, 1000), mp=random.randrange(50, 75), atk=700, df=200, magic=enemy_magic, items=[], type="enemy"))
                print(TextStrings.str10)
                text = input(TextStrings.str11)
