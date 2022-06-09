from BaseClass import BaseClass

### Card Class
class Card(BaseClass):
    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self.card_id = 1
        self.card_name = ""
        self.card_name_abbreviate = ""
        self.card_set = ""
        self.set_parms(kwargs)
        return

### PlayingCard inherited from Card
class StandardPlayingCard(Card):
    # Class Variables
    SUIT = dict(
        CLUB = {
            'symbol': "\u2663",
            'name': 'clubs'
        },
        SPADE = {
            'symbol': "\u2660",
            'name': 'spades'
        },
        DIAMOND = {
            'symbol': "\u2666",
            'name': 'diamonds'
        },
        HEART = {
            'symbol': "\u2665",
            'name': 'hearts'
        }
    )

    VALUE = dict(
        TWO = {
            'symbol': "2",
            'name': 'two'
        },
        THREE = {
            'symbol': "3",
            'name': 'three'
        },
        FOUR = {
            'symbol': "4",
            'name': 'four'
        },
        FIVE = {
            'symbol': "5",
            'name': 'five'
        },
        SIX = {
            'symbol': "6",
            'name': 'six'
        },
        SEVEN = {
            'symbol': "7",
            'name': 'seven'
        },
        EIGHT = {
            'symbol': "8",
            'name': 'eight'
        },
        NINE = {
            'symbol': "9",
            'name': 'nine'
        },
        TEN = {
            'symbol': "10",
            'name': 'ten'
        },
        JACK = {
            'symbol': "J",
            'name': 'jack'
        },
        QUEEN = {
            'symbol': "Q",
            'name': 'queen'
        },
        KING = {
            'symbol': "K",
            'name': 'king'
        },
        ACE = {
            'symbol': "A",
            'name': 'ace'
        }
    )
    
    # Constructor
    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self.card_set = "StandardPlayingCard"  
        self.card_suit = self.SUIT['CLUB']
        self.card_value = self.VALUE['TWO']
        self.card_name = ""
        self.card_name_abbreviate = ""
        self.set_parms(kwargs)
        self.set_card_name()        
        return

    def set_card_name(self):
        self.card_name = self.card_value['name'] + " of " + self.card_suit['name']
        self.card_name_abbreviate = self.card_value['symbol'] + self.card_suit['symbol']
        return
