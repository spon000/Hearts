import random
from BaseClass import BaseClass
from Card import Card, StandardPlayingCard


class CardPile(BaseClass):
    TOP = -1
    BOTTOM = 0
    FULL_DECK = 52
    
    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self._card_class = Card
        self.cards = []
        self.card_pile_id = 1
        self.set_parms(kwargs)
        return 

    def __len__(self):
        return len(self.cards)

    def  __add__(self, cards):
        self.add_cards(cards)
        return

    def __sub__(self, cards):
        self.remove_cards(cards)
        return

    def shuffle(self):
        random.shuffle(self.cards)
        return

    def add_cards(self, cards = [], position = TOP):
        self.cards.insert(position, cards)
        return 

    def remove_cards(self, cards = []):
        return_cards = []
        
        for card in cards:
            return_cards.append(card)
            self.cards.remove(card)
        return return_cards 
    
    def clone_cards(self, start = 0, end = None):
        return self.cards[start:end]

    def draw_cards(self, number_of_cards = 1, position = TOP):
        drawn_cards = self.cards[:]

        if position == self.TOP:
            position = 0
            drawn_cards.reverse()

        drawn_cards = drawn_cards[position:position + number_of_cards]
        self.remove_cards(drawn_cards)
        return drawn_cards

    def take_cards(self, cards):
        taken_cards = self.find_cards(cards)
        self.remove_cards(taken_cards)
        return taken_cards

    def find_cards(self, cards):
        return [card for card in self.cards if card in cards]

    def get_number_of_cards(self):
        return len(self.cards)

###
class StandardPlayingCardPile(CardPile):
    def __init__(self, make_standard_deck = False, kwargs = {}):
        super().__init__(kwargs)
        self._card_class = StandardPlayingCard

        if make_standard_deck:
            self.create_standard_deck()
            
        self.set_parms(kwargs)
        return

    def create_standard_deck(self):
        self.cards = [
                self._card_class({
                    'card_id': j+(i*len(StandardPlayingCard.VALUE.items()))+1, 
                    'card_suit': suit, 
                    'card_value': value
                }) 
                for i, (skey, suit) in enumerate(StandardPlayingCard.SUIT.items()) 
                for j, (vkey, value) in enumerate(StandardPlayingCard.VALUE.items())
            ]
        return


    