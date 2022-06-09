from MonteCarloTreeSearchNode import MonteCarloTreeSearchNode as MCTSN
from Game import Hearts

import sys, codecs

stdoutOrigin=sys.stdout 
sys.stdout = codecs.open("log.txt", "w", "utf-8")

# from players import player_data
# from cards import card_data

game_of_hearts = Hearts({'winning_score': 1000})

for index in range(1, game_of_hearts.max_players + 1):
    game_of_hearts.add_player({
       'name': f"player_{index}"
    })

game_of_hearts.start()
# print(game_of_hearts)


# print(deck)




# deck = CardPile([
#     PlayingCard(card_id = j+(i*len(PlayingCard.VALUE.items()))+1, card_suit = suit, card_value = value) for i, (skey, suit) in enumerate(PlayingCard.SUIT.items()) for j, (vkey, value) in enumerate(PlayingCard.VALUE.items())
# ])

# game_of_hearts.add_deck_of_cards(deck)

# for i in range(4):
#     game_of_hearts.add_player(HeartsPlayer("player_" + str(i+1)))

# # while game_of_hearts.get_game_status() != "finished":
# #     game_of_hearts.add_round(HeartsRound(game_of_hearts.get_players(), game_of_hearts.)
    

# # rounds = list([Round()])
# # print(f"length of VALUE items = {len(PlayingCard.VALUE.items())}")
# # deck = CardPile([
# #     PlayingCard(card_id = j+(i*len(PlayingCard.VALUE.items()))+1, card_suit = suit, card_value = value) for i, (skey, suit) in enumerate(PlayingCard.SUIT.items()) for j, (vkey, value) in enumerate(PlayingCard.VALUE.items())
# # ])
# # print(deck.shuffle()[13])
# print(game_of_hearts.players[3])
# # print(rounds[0])
# print(deck)
# round = Round()


# def card_shuffle(cards=[]):
#     shuffled_cards = cards[:]
#     random.shuffle(shuffled_cards)
#     return(shuffled_cards)

# def init_game():
#     game['players'] = players
#     game['round'] = 1
#     game['state'] = 'init'
#     game['number_of_players'] = 4
#     game['current_player_order'] = [player['id'] for player in players]
#     game['pass_type'] = [1, 2, 3, 0]
#     game['table_cards'] = []
#     game['trick_number'] = 1
#     game['lead_suit'] = constants.CLUB
#     game['hears_broken'] = False
#     game['tricks_per_round'] = 13
#     return

# def init_round():
#     deck = card_shuffle(cards)

#     while not deck == []:
#         # Sort players by player_order_number
#         # game['players'] = sorted(game['players'], key = lambda player: player['order_number'])
#         for player in players:
#             player['hand'].append(deck.pop())

#     for player in game['players']:
#         player['state'] = 'round_passing'

# def set_first_player():
#     for player in game['players']:
#         if "2" + constants.CLUB in player['hand']:
#             while game['current_player_order'][0] != player['id']:
#                 set_next_player()

# def set_next_player():
#     game['current_player_order'].append(game['current_player_order'].pop(0)) 
#     game['players'].append(game['players'].pop(0)) 

# def get_legal_move(game):
#     if game['trick_number'] == 1 and game['table_cards'] == []:
#         return ["2" + constants.CLUB]
#     if 

# def pass_cards():
#     pass

# def play_cards():
#     set_first_player()
#     while game['trick_number'] <= game['tricks_per_round']:
#         legal_moves = get_legal_move(game)
#         game['trick_number'] += 1
#         # if game['current_player_order'] = 
    
# def play_round():
#     pass_cards()
#     play_cards()
#     return



            
def main():
#     # print(os.linesep.join(cards))
#     init_game()
#     init_round()
#     play_round()
#     print(game)

    sys.stdout.close()
    sys.stdout=stdoutOrigin
    pass


#     # root = MCTSN(state = game)
#     # selected_node = root.best_action()
#     return 


if __name__ == '__main__':
    main()