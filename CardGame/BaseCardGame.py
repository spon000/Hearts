import logging

from CardGame.BaseClass import BaseClass

class BaseCardGame(BaseClass):
    DIRECTION = {
        "CLOCKWISE": 0,
        "COUNTER_CLOCKWISE": 1
    }

    GAME_STATE = {
        "init" : 0,
        "starting" : 1,
        "running": 2,
        "paused": 3,
        "ending": 4,
        "finished": 5
    }

    def __init__(self, **kwargs):
        self._total_players = 0
        # self._round_class = Round
        # self._player_class = Player
        self.game_id = 1
        self.players = []
        self.rounds = []
        self._game_state = self.GAME_STATE['init']
        self._current_round = 0
        self.max_players = 4
        super().__init__(**kwargs)

    def add_player(self, player):
        logging.debug(f"Adding Player: {player.name}...")
        if len(self.players) <= self.max_players:
            self.players.extend([player])
            # self.players.extend([self._player_class(kwargs)])
        return

    def add_round(self, round):
        self.rounds.extend([round])
        return

    def set_first_player(self, player):
        while self.players.index(player) != 0:
            self.shift_player()
        return

    def shift_player(self, direction = DIRECTION['CLOCKWISE']):
        if direction == self.DIRECTION['CLOCKWISE']:
            self.players.append(self.players.pop(0)) 
        else: 
            self.players.insert(0, self.players.pop())
        return

    def start(self):
        return

    def run(self):
        return

    def end(self):
        return


        



