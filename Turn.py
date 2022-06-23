from BaseClass import BaseClass
from Card import StandardPlayingCard

class Turn(BaseClass):

    TURN_STATE = {
        "starting" : 0,
        "playing": 1,
        "paused": 3,
        "ending": 4,
        "finished": 5
    }

    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self.state
        self.set_parms(kwargs)
        return

class HeartsTrick(Turn):
    
    def __init__(self, players, kwargs = {}):
        super().__init__(kwargs)
        self.players = players
        self._hearts_broken = False
        self._queen_spade_played = False
        self._lead_suit = StandardPlayingCard.SUIT['CLUB']
        self.set_parms(kwargs)
        return

    def determine_first_player(self):
        return

    def get_legal_move(self, player):
        

        return



