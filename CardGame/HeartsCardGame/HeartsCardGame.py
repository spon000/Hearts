import logging

from CardGame.BaseCardGame import BaseCardGame

class HeartsCardGame(BaseCardGame):
    VARIANT = {
        'STANDARD': 0
    }

    PASS = {
        'RIGHT' : 0,
        'LEFT': 1,
        'ACROSS': 2,
        'NONE': 3
    }    

    def __init__(self, **kwargs):
        # self._round_class = HeartsRound
        # self._player_class = HeartsPlayer
        self.losing_score = 200
        self.game_variant = self.VARIANT['STANDARD']
        self._passing = [self.PASS['RIGHT'], self.PASS['LEFT'], self.PASS['ACROSS'], self.PASS['NONE']]
        super().__init__(**kwargs)            

        if self.game_variant == self.VARIANT['STANDARD']:
            self.max_players = 4

        logging.debug(f"game_id = {self.game_id}")

    def shift_pass_type(self):
        self._passing.append(self._passing.pop(0))

    def check_game_over(self):
        for player in self.players:

            if player.score >= self.losing_score:
                return True

        return False


    # def start(self):
    #     logging.info("starting game...")
    #     self.state = self.GAME_STATE['starting']
    #     self.add_round(self._round_class(self.players, self._passing[0]))
    #     self.state = self.GAME_STATE['running']
    #     self.run()
    #     return

    # def run(self):
    #     logging.debug("running game...")

    #     while self.state == self.GAME_STATE['running']:
    #         self.rounds[-1].start()

    #         if self.check_game_over():
    #             self.state = self.GAME_STATE['ending']
            
    #     self.end()

    # def end(self):
    #     logging.info("ending game...")
    #     return
