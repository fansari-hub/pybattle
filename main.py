import battle

while True:
    
    input("Press enter to start a new battle!")
    battle1 = battle.battle_event()
    battle1.begin_battle()
    del(battle1)