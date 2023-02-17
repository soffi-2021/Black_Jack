from random import shuffle

class Deck(object):
    def __init__(self):
        ranks = "23456789TJQKA"
        suits = "DCHS"
        self.cards = [Card(r,s) for r in ranks for s in suits]
        shuffle(self.cards)
 
    def deal_card(self):
        
        return self.cards.pop()