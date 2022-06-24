from CardGame.BaseClass import BaseClass
 
class BaseCardPlayer(BaseClass):
    PLAYER_STATE = {
        "starting" : 0,
        "playing" : 1,
        "finished" : 2
    }

    PLAYER_TYPE = {
        "AI" : 0,
        "HUMAN" : 1
    }

    def __init__(self, **kwargs):
        self._player_state = self.PLAYER_STATE['starting']
        self._player_id = 0
        self.name = "player_name"
        self.p_type = self.PLAYER_TYPE['AI']
        self.score = 0
        super().__init__(**kwargs)

    def assign_id(self, player_id):
        self._player_id = player_id
        return



