import random
import itertools
class Coloretto:
    class Player:
        pass
    def __init__(self):
        self.stock=list(itertools.chain.from_iterable([i]*9 for i in range(5)))
        random.shuffle(self.stock)
        print(self.stock)
        self.players=[Coloretto.Player() for i in range(2)]
        print(self.players)

game=Coloretto()
