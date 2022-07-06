import logging

from CardGame.BaseClass import BaseClass
from CardGame.BaseCardPile import BaseCardPile
from CardGame.BaseCard import BaseCard

class BaseCardRound(BaseClass):
    # Class Variables
    ALL_CARDS = -1

    ROUND_STATE = {
        "init" : 0,
        "dealing" : 1,
        "playing": 2,
        "paused": 3,
        "ending": 4,
        "finished": 5
    }

    @classmethod
    def CHANGE_ROUND_PARMS(cls, new_round_parm):
        cls.ROUND_STATE = new_round_parm
        return

    def __init__(self, **kwargs):
        self.state = self.ROUND_STATE["init"]
        # self._card_pile_class = BaseCardPile
        # self._card_class = BaseCard
        self.players = []
        self.deck = BaseCardPile
        self.table_cards = BaseCardPile
        self.played_cards = BaseCardPile                 # CardPile Object
        self.round_number = 0
        self.current_player = 0
        super().__init__(**kwargs)

    def deal_cards(self):
        logging.debug("dealing cards...")

        for player in self.players:
            logging.debug(f"Deal card to {player.name}")
            if len(self.deck) > 0:  
                player.hand.add_cards(self.deck.draw_cards())
            else:
                break
        return 

    def deal_hand(self, shuffle = False, cards_per_player = 1):
        logging.debug("dealing hand...")

        if shuffle:
            self.deck.shuffle()

        while cards_per_player > 0 and len(self.deck) > 0:
            logging.debug(f"Deck length = {len(self.deck)}\nCards to Deal = {cards_per_player}")
            self.deal_cards()
            cards_per_player -= 1
        return

    def start(self):
        return

    def run(self):
        return

 
