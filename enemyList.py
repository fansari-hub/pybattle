from actors import Person
import random


class EnemiesList:
    enemy1 = ("Troll", random.randrange(2000, 3000), random.randrange(100, 150), 525, 25)
    enemy2 = ("Imp", random.randrange(1500, 2500), random.randrange(100, 150), 560, 100)
    enemy3 = ("Slime", random.randrange(1500, 2000), random.randrange(100, 150), 500, 200)

    enemies = [enemy1, enemy2, enemy3]

    @staticmethod
    def get_enemies():
            return EnemiesList.enemies
