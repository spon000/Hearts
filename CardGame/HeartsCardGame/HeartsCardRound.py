from CardGame.BaseCardRound import BaseCardRound
from CardGame.BaseCardPile import StandardPlayingCardPile
from CardGame.BaseCard import StandardPlayingCard


class HeartsCardRound(BaseCardRound):
    BaseCardRound.ROUND_STATE.update({
        'passing': 6
    })

    def __init__(self, **kwargs):
        self._card_pile_class = StandardPlayingCardPile
        self._card_class = StandardPlayingCard
        self.deck = StandardPlayingCardPile(make_standard_deck = True)
        self._pass_type = 'NONE'
        super().__init__(**kwargs)        

    # def start(self):
    #     logging.debug("starting round...")
    #     self.state = self.ROUND_STATE['dealing']
    #     self.deal_hand(shuffle = True, cards_per_player = int(StandardPlayingCardPile.FULL_DECK / len(self.players)))
    #     # print(f"cards = {self.players[0].hand.clone_cards()}")
    #     self.state = self.ROUND_STATE['passing']
    #     self.determine_first_player()
    #     self.state = self.ROUND_STATE['playing']
    #     self.run()

    #     return

    # def run(self):
    #     logging.debug("running round...")

    #     while self.state == self.ROUND_STATE['playing']:

    #         for player in self.players:
    #             self.get_legal_move(player)

    #         trick = HeartsTrick()

    #         if len(self.players[0].hand) <= 0:
    #             self.state = self.ROUND_STATE['ending']

    #     self.end()        
    #     return

    # def pass_cards(self, cards = StandardPlayingCardPile()):
    #     if self._pass_type  != Hearts.PASS['NONE']:
    #         self.pick_3_cards(3)
    #     return

    # def calculate_current_score(self):
    #     return

    # def pick_3_cards(self):
    #     for player in self.players:
    #         if player.p_type == ''


    #     return

    # def end(self):
    #     logging.debug("ending round...")
    #     return
