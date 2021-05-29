class Item:

    #items
    potion = ("Potion", "potion", "Heals 100 HP", 100, 15)
    hipotion = ("Hi Potion", "potion", "Heals 250 HP", 250, 5)
    superpotion = ("Super Potion", "potion", "Heals 1000 HP", 1000, 5)
    elixir = ("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999, 5)
    hielixir = ("Mega Elixir", "elixir", "Fully restores party HP/MP", 9999, 2)
    grenade = ("Grenade", "attack", "Deals 500 damage", 500, 5)

    
    player_items = [potion, hipotion, superpotion, elixir, hielixir, grenade]
    enemy_items = []

    

    def __init__(self, name, type, description, prop, quantity):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
        self.quantity = quantity

    
    @staticmethod
    def get_player_items():
            return Item.player_items
    
    @staticmethod
    def get_enemy_items():
            return Item.enemy_items
