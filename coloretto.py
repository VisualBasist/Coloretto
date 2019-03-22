import random
import itertools
class Coloretto:
    class Player:
        def __init__(self,isbot=False):
            self.hand=[]
            self.isbot=isbot
            self.isfin=False
        def take_firstcard(self,stock,selected_first_cards):
            self.hand=random.sample(set(stock)-selected_first_cards,2)
            selected_first_cards.update(self.hand)
            for c in self.hand:
                stock.remove(c)
        def take_stockcard(self,game):
            #stockを引数で渡さなくていいようにするのがいい気がする
            #Colorettoを継承してPlayer作る?
            if all(len(r)>=m for r,m in zip(game.rowcards,game.rowcards_max)):
                print("もう取るしかありません")
                self.take_rowcard_fin()
                return

            takencard=game.stock.pop()
            print("取ったカード",takencard)
            if self.isbot:
                put_position=random.choices([i for i,(r,m) in enumerate(zip(game.rowcards,game.rowcards_max)) if len(r)<m])[0]
            else:
                put_position=int(input("どこに置く? : "))-1
            game.rowcards[put_position].append(takencard)
        def take_rowcard_fin(self):
            if self.isbot:
                put_position=random.choices([i for i,c in enumerate(game.rowcards) if c])[0]
            else:
                put_position=int(input("どれを取る? : "))-1
            self.hand.extend(game.rowcards[put_position])
            game.rowcards[put_position].clear()
            self.isfin=True
        def action(self,game):
            if self.isbot:
                if random.random()>0.1:
                    self.take_stockcard(game)
                else:
                    self.take_rowcard_fin()
            else:
                if input("t(take) or f(fin)? : ")=="t":
                    self.take_stockcard(game)
                else:
                    self.take_rowcard_fin()


    def __init__(self):
        self.stock=list(itertools.chain.from_iterable([i]*9 for i in range(7-2)))
        print(self.stock)
        self.players=[Coloretto.Player(),Coloretto.Player(True)]
        selected_first_cards=set()
        for i,p in enumerate(self.players):
            p.take_firstcard(self.stock,selected_first_cards)
            print(i,"の手札",p.hand)
        print("各自取った後の山札",self.stock)
        random.shuffle(self.stock)
        print("シャッフルした山札",self.stock)

        self.rowcards_max=[1,2,3]
        print("列カード最大",self.rowcards_max)

    def play(self):
        self.rowcards=[[] for i in range(3)]
        while self.stock:
            if all(p.isfin for p in self.players):
                #HACK:再確保よりclearがいい?
                self.rowcards=[[] for i in range(3)]
                #HACK:変更する時はリスト内包表記で書く?
                for i,p in enumerate(self.players):
                    self.players[i].isfin=False
            for i,p in enumerate(self.players):
                if p.isfin:
                    continue
                print(i,"の番")
                p.action(self)
                print("列カード",self.rowcards)
                print("手札",p.hand)
                print()

game=Coloretto()
game.play()
