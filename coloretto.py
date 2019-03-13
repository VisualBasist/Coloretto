import random
import itertools
class Coloretto:
    class Player:
        def __init__(self,isbot=False):
            self.hand=[]
            self.isbot=isbot
        def take_firstcard(self,stock,selected_first_cards):
            self.hand=random.sample(set(stock)-selected_first_cards,2)
            selected_first_cards.update(self.hand)
            for c in self.hand:
                stock.remove(c)
        def take_stockcard(self,stock):
            #stockを引数で渡さなくていいようにするのがいい気がする
            stock.pop()
        def take_rowcard_fin(self):
            pass
        def action(self,stock):
            if input("t(take) or f(fin) : ")=="t":
                self.take_stockcard(stock)
            else:
                self.take_rowcard_fin()

    def __init__(self):
        self.stock=list(itertools.chain.from_iterable([i]*9 for i in range(7-2)))
        print(self.stock)
        self.players=[Coloretto.Player(),Coloretto.Player(True)]
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

    def play(self):
        while self.stock:
            for p in self.players:
                p.action(self.stock)

game=Coloretto()
game.play()
