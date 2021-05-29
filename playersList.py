from actors import Person
import random


class PlayersList:
    player1 = ("Valos", random.randrange(3000,3500), 100, 300, 34)
    player2 = ("Nick", random.randrange(4000,4500), 100, 311, 34)
    player3 = ("Rob", random.randrange(2500,3000), 100, 288, 34)

    players = [player1, player2, player3]

    @staticmethod
    def get_players():
            return PlayersList.players
