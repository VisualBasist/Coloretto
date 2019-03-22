import random
import itertools
class Coloretto:
    class Player:
        def __init__(self,isbot=False):
            self.hand=[]
            self.isbot=isbot
            self.isfin=False
        def print_hand(self):
            print(" ".join(Coloretto.colorize(c) for c in sorted(self.hand)))
        def take_firstcard(self,stock,selected_first_cards):
            self.hand=random.sample(set(stock)-selected_first_cards,2)
            selected_first_cards.update(self.hand)
            for c in self.hand:
                stock.remove(c)
        def take_stockcard(self,game):
            #stockを引数で渡さなくていいようにするのがいい気がする
            #Colorettoを継承してPlayer作る?
            if all(len(r)>=m for r,m in zip(game.rowcards,game.rowcards_max) if r is not None):
                print("もう取るしかありません")
                self.take_rowcard_fin()
                return

            takencard=game.stock.pop()
            print("取ったカード",Coloretto.colorize(takencard))
            if self.isbot:
                put_position=random.choices([i for i,(r,m) in enumerate(zip(game.rowcards,game.rowcards_max)) if (r is not None) and len(r)<m])[0]
            else:
                put_position=int(input("どこに置く? : "))-1
            game.rowcards[put_position].append(takencard)
        def take_rowcard_fin(self):
            if self.isbot:
                put_position=random.choices([i for i,c in enumerate(game.rowcards) if c])[0]
            else:
                put_position=int(input("どれを取る? : "))-1
            self.hand.extend(game.rowcards[put_position])
            game.rowcards[put_position]=None
            self.isfin=True
        def action(self,game):
            if self.isbot:
                if any(game.rowcards):
                    if random.random()>0.1:
                        self.take_stockcard(game)
                    else:
                        self.take_rowcard_fin()
                else:
                    self.take_stockcard(game)
            else:
                if input("t(take) or f(fin)? : ")=="t":
                    self.take_stockcard(game)
                else:
                    self.take_rowcard_fin()
        def calc_score(self):
            scorechart=lambda x:21 if x>=6 else [0,1,3,6,10,15][x]

            #TODO:もっと綺麗に
            plus_cards_and_num=sorted(((h,self.hand.count(h)) for h in set(self.hand)),key=lambda x:x[1])[-3:]
            score=sum(scorechart(pc) for _,pc in plus_cards_and_num)
            minus_cards=set(self.hand)-set(i for i,_ in plus_cards_and_num)
            score-=sum(scorechart(self.hand.count(h)) for h in minus_cards)
            return score

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

    @classmethod
    def colorize(cls,n):
        return "\033[30m"+"\033[4"+str(n+1)+"m"+str(n)+"\033[0m"

    def play(self):
        self.rowcards=[[] for i in range(3)]
        while True:
            if all(p.isfin for p in self.players):
                print("ラウンド終了")
                self.rowcards=[[] for i in range(3)]
                #HACK:変更する時はリスト内包表記で書く?
                for i,p in enumerate(self.players):
                    self.players[i].isfin=False
            for i,p in enumerate(self.players):
                if p.isfin:
                    continue
                if not self.stock:
                    for i,p in enumerate(self.players):
                        print(i,"の得点",p.calc_score())
                    return
                print(i,"の番")
                p.action(self)
                print("列カード",self.rowcards)
                p.print_hand()
                print()

game=Coloretto()
game.play()
