import logging

from BaseClass import BaseClass
from CardPile import CardPile, StandardPlayingCardPile
from Card import Card, StandardPlayingCard
from Turn import HeartsTrick

class Round(BaseClass):
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

    def __init__(self, players, kwargs = {}):
        super().__init__(kwargs)
        self.state = self.ROUND_STATE["init"]
        self._card_pile_class = CardPile
        self._card_class = Card
        self.players = players
        self.deck = CardPile
        self.table_cards = CardPile
        self.played_cards = CardPile                 # CardPile Object
        self.round_number = 0
        self.current_player = 0
        self.set_parms(kwargs)
        return

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

 
class HeartsRound(Round):
    Round.ROUND_STATE.update({
        'passing': 6
    })

    def __init__(self, players, pass_type, kwargs = {}):
        super().__init__(players, kwargs)
        self._card_pile_class = StandardPlayingCardPile
        self._card_class = StandardPlayingCard
        self._pass_type = pass_type
        
        self.set_parms({'deck': StandardPlayingCardPile(make_standard_deck = True)})
        return

    def start(self):
        logging.debug("starting round...")
        self.state = self.ROUND_STATE['dealing']
        self.deal_hand(shuffle = True, cards_per_player = int(StandardPlayingCardPile.FULL_DECK / len(self.players)))
        # print(f"cards = {self.players[0].hand.clone_cards()}")
        self.state = self.ROUND_STATE['passing']
        self.determine_first_player()
        self.state = self.ROUND_STATE['playing']
        self.run()

        return

    def run(self):
        logging.debug("running round...")

        while self.state == self.ROUND_STATE['playing']:

            for player in self.players:
                self.get_legal_move(player)

            trick = HeartsTrick()

            if len(self.players[0].hand) <= 0:
                self.state = self.ROUND_STATE['ending']

        self.end()        
        return

    def determine_first_player(self):
        
        return

    def get_legal_move(self, player):
        if self.state == self.ROUND_STATE['passing']:
            return 

        return

    def pass_cards(self, cards = StandardPlayingCardPile()):
        return

    def calculate_current_score(self):
        return

    def end(self):
        logging.debug("ending round...")
        return
