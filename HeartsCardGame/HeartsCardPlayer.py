from CardGame.BaseCardPlayer import BaseCardPlayer
from CardGame.BaseCardPile import StandardPlayingCardPile

class HeartsCardPlayer(BaseCardPlayer):
    BaseCardPlayer.PLAYER_STATE.update({
        "passing" : 3,
    })

    def __init__(self, **kwargs):
        self.hand = StandardPlayingCardPile()
        self.tricks = StandardPlayingCardPile()
        self.pass_cards = StandardPlayingCardPile()
        self.legal_card_plays = StandardPlayingCardPile()
        super().__init__(**kwargs)