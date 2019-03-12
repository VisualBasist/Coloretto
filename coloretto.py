import random
import itertools
class Coloretto:
    class Player:
        def __init__(self):
            self.hand=[]
        def take_firstcard(self,stock,selected_first_cards):
            self.hand=random.sample(set(stock)-selected_first_cards,2)
            selected_first_cards.update(self.hand)
            for c in self.hand:
                stock.remove(c)
    def __init__(self):
        self.stock=list(itertools.chain.from_iterable([i]*9 for i in range(7-2)))
        print(self.stock)
        self.players=[Coloretto.Player() for i in range(2)]
        print(self.players)
        selected_first_cards=set()
        for p in self.players:
            p.take_firstcard(self.stock,selected_first_cards)
            print(p.hand)
        print(self.stock)
        random.shuffle(self.stock)
        print(self.stock)

        self.rowcards=[1,2,3]
        print("列カード",self.rowcards)

game=Coloretto()
