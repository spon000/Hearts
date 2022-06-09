from BaseClass import BaseClass
from Card import StandardPlayingCard

class Turn(BaseClass):

    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self.set_parms(kwargs)
        return

class HeartsTrick(Turn):
    
    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self._hearts_broken = False
        self._queen_spade_played = False
        self._lead_suit = StandardPlayingCard.SUIT['CLUB']
        self.set_parms(kwargs)
        return



