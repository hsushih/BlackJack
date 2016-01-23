import random  # needed for shuffling a Deck

class Card(object):
    
    def __init__(self, r, s):
        self.r=r
        self.s=s.upper()

    def __str__(self):
        return str(self.get_rank())+ str(self.get_suit())

    def get_rank(self):
        ''' get rank'''
        return self.r

    def get_suit(self):
        ''' get suit'''
        return self.s

class Deck():
     
    def __init__(self):
        self.deck = []
        ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        suits = ['S','C','H','D']
        for rank in ranks:
            for suit in suits:
                self.deck.append([rank,suit])
        
    def shuffle(self):
        ''' shuffle the deck'''
        random.shuffle(self.deck)
        

    def get_deck(self):
        ''' get deck'''
        return self.deck

    def deal(self):
        ''' deal a card from the deck'''
        return self.deck.pop()
    
    def __str__(self):
        self.card_list=[]
        for card in self.deck:
            self.card_list.append(str(card))
        return '\n'.join(self.card_list)


