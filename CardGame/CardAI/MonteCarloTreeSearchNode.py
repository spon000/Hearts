import numpy as np
from collections import defaultdict

# This example comes from:
# https://ai-boson.github.io/mcts/

# Define MCTS class.
class MonteCarloTreeSearchNode():
    # Constructor function:
    # 
    # state:    For our game it represents the board state. Generally the board state is 
    #           represented by an array. For normal Tic Tac Toe, it is a 3 by 3 array.
    # 
    # parent:   It is None for the root node and for other nodes it is equal to the node 
    #           it is derived from. For the first turn as you have seen from the game it 
    #           is None.
    # 
    # children: It contains all possible actions from the current node. For the second turn 
    #           in our game this is 9 or 8 depending on where you make your move.
    # 
    # parent_action:    None for the root node and for other nodes it is equal to the action 
    #                   which it’s parent carried out.
    # 
    # _number_of_visits:    Number of times current node is visited
    # 
    # results:  It’s a dictionary
    # 
    # _untried_actions:     Represents the list of all possible actions
    # 
    # action:    Move which has to be carried out.
    def __init__(self, state, parent=None, parent_action=None):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        self._untried_actions = None
        self._untried_actions = self.untried_actions()
        return

    # Returns the list of untried actions from a given state. For the first turn of our 
    # game there are 81 possible actions. For the second turn it is 8 or 9. This varies 
    # in our game.
    def untried_actions(self):
        self._untried_actions = self.state.get_legal_actions()
        return self._untried_actions

    # Returns the difference of wins - losses
    def q(self):
        wins = self._results[1]
        loses = self._results[-1]
        return wins - loses

    # Returns the number of times each node is visited.
    def n(self):
        return self._number_of_visits

    # From the present state, next state is generated depending on the action which is 
    # carried out. In this step all the possible child nodes corresponding to generated 
    # states are appended to the children array and the child_node is returned. The states 
    # which are possible from the present state are all generated and the child_node 
    # corresponding to this generated state is returned.
    def expand(self):
        action = self._untried_actions.pop()
        next_state = self.state.move(action)
        child_node = MonteCarloTreeSearchNode(next_state, parent=self, parent_action=action)
        self.children.append(child_node)
        return child_node

    # This is used to check if the current node is terminal or not. Terminal node is reached 
    # when the game is over.
    def is_terminal_node(self):
        return self.state.is_game_over()

    # From the current state, entire game is simulated till there is an outcome for the game. 
    # This outcome of the game is returned. For example if it results in a win, the outcome 
    # is 1. Otherwise it is -1 if it results in a loss. And it is 0 if it is a tie. If the 
    # entire game is randomly simulated, that is at each turn the move is randomly selected 
    # out of set of possible moves, it is called light playout.
    def rollout(self):
        current_rollout_state = self.state
        
        while not current_rollout_state.is_game_over():
            
            possible_moves = current_rollout_state.get_legal_actions()
            
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.game_result()

    # In this step all the statistics for the nodes are updated. Untill the parent node is reached, 
    # the number of visits for each node is incremented by 1. If the result is 1, that is it resulted 
    # in a win, then the win is incremented by 1. Otherwise if result is a loss, then loss is 
    # incremented by 1.
    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)

    # All the actions are poped out of _untried_actions one by one. When it becomes empty, that 
    # is when the size is zero, it is fully expanded.
    def is_fully_expanded(self):
        return len(self._untried_actions) == 0


    # Once fully expanded, this function selects the best child out of the children array. The 
    # first term in the formula corresponds to exploitation and the second term corresponds to 
    # exploration.
    def best_child(self, c_param=0.1):
        choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]

    # Randomly selects a move out of possible moves. This is an example of random playout.
    def rollout_policy(self, possible_moves):
        return possible_moves[np.random.randint(len(possible_moves))]


    # Selects node to run rollout.
    def _tree_policy(self):
        current_node = self
        while not current_node.is_terminal_node():
            
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                current_node = current_node.best_child()
        return current_node


    # This is the best action function which returns the node corresponding to best possible 
    # move. The step of expansion, simulation and backpropagation are carried out by the code 
    # above.
    def best_action(self):
        simulation_no = 100
        
        for i in range(simulation_no):
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        
        return self.best_child(c_param=0.)



    def get_legal_actions(self): 
        '''
        Modify according to your game or
        needs. Constructs a list of all
        possible actions from current state.
        Returns a list.
        '''

    def is_game_over(self):
        '''
        Modify according to your game or 
        needs. It is the game over condition
        and depends on your game. Returns
        true or false
        '''

    def game_result(self):
        '''
        Modify according to your game or 
        needs. Returns 1 or 0 or -1 depending
        on your state corresponding to win,
        tie or a loss.
        '''

    def move(self,action):
        '''
        Modify according to your game or 
        needs. Changes the state of your 
        board with a new value. For a normal
        Tic Tac Toe game, it can be a 3 by 3
        array with all the elements of array
        being 0 initially. 0 means the board 
        position is empty. If you place x in
        row 2 column 3, then it would be some 
        thing like board[2][3] = 1, where 1
        represents that x is placed. Returns 
        the new state after making a move.
        '''
















