from BaseClass import BaseClass
from CardPile import CardPile, StandardPlayingCardPile

class Player(BaseClass):
    PLAYER_STATE = {
        "starting" : 0,
        "playing" : 1,
        "finished" : 2
    }

    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self._player_state = self.PLAYER_STATE['starting']
        self._player_id = 0
        self.name = "player_name"
        self.p_type = 'AI'
        self.score = 0
        self.set_parms(kwargs)
        return

    def assign_id(self, player_id):
        self._player_id = player_id
        return

class HeartsPlayer(Player):
    Player.PLAYER_STATE.update({
        "passing" : 3,
    })

    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self.hand = StandardPlayingCardPile()
        self.tricks = StandardPlayingCardPile()
        self.set_parms(kwargs)
        return

