import random
import itertools
class Coloretto:
    class Player:
        def __init__(self):
            self.hand=[]
    def __init__(self):
        self.stock=list(itertools.chain.from_iterable([i]*9 for i in range(7-2)))
        random.shuffle(self.stock)
        print(self.stock)
        self.players=[Coloretto.Player() for i in range(2)]
        print(self.players)
        self.rowcards=[1,2,3]
        print(self.rowcards)

game=Coloretto()
