import logging

from BaseClass import BaseClass
from Player import Player, HeartsPlayer
from Round import Round, HeartsRound

class Game(BaseClass):
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

    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self._total_players = 0
        self._round_class = Round
        self._player_class = Player
        self._game_id = 1
        self.players = []
        self.rounds = []
        self._game_state = self.GAME_STATE['init']
        self._current_round = 0
        self.max_players = 4
        self.set_parms(kwargs)
        return 

    def add_player(self, kwargs = {}):
        if len(self.players) <= self.max_players:
            self.players.extend([self._player_class(kwargs)])
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

class Hearts(Game):
    VARIANT = {
        'STANDARD': 0
    }

    PASS = {
        'RIGHT' : 0,
        'LEFT': 1,
        'ACROSS': 2,
        'NONE': 3
    }    

    def __init__(self, kwargs = {}):
        super().__init__(kwargs)
        self._round_class = HeartsRound
        self._player_class = HeartsPlayer
        self.losing_score = 200
        self.game_variant = self.VARIANT['STANDARD']
        self._passing = [self.PASS['RIGHT'], self.PASS['LEFT'], self.PASS['ACROSS'], self.PASS['NONE']]
        
        if self.game_variant == self.VARIANT['STANDARD']:
            self.max_players = 4
        
        self.set_parms(kwargs)
        return 

    def shift_pass_type(self):
        self._passing.append(self._passing.pop(0))

    def check_game_over(self):
        for player in self.players:

            if player.score >= self.losing_score:
                return True

        return False


    def start(self):
        logging.info("starting game...")
        self.state = self.GAME_STATE['starting']
        self.add_round(self._round_class(self.players, self._passing[0]))
        self.state = self.GAME_STATE['running']
        self.run()
        return

    def run(self):
        logging.debug("running game...")

        while self.state == self.GAME_STATE['running']:
            self.rounds[-1].start()

            if self.check_game_over():
                self.state = self.GAME_STATE ['ending']
            
        self.end()

    def end(self):
        logging.info("ending game...")
        return

        



