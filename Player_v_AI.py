
# AI Player for use in Connect Four  


import random  
from Player_v_Player import *

class AIPlayer(Player): 
    #2
    def __init__(self, checker, tiebreak, lookahead):
        '''constructs a new AIPlayer object.'''
        
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        
        super().__init__(checker)
        self.tiebreak = tiebreak 
        self.lookahead = lookahead
     #3  
    def __repr__(self): 
        return 'Player ' + str(self.checker) + ' (' + str(self.tiebreak) + ', ' + str(self.lookahead) + ')'
    
    #4 Done 
    def max_score_column(self, scores): 
        ''' takes a list scores containing a score for each column of the board, 
        and that returns the index of the column with the maximum score. '''
        
        numbers = [x for x in scores] 
        numbers = max(numbers)

        
        list = [] 
        for score in range(len(scores)): 
            if numbers == scores[score]: 
                list += [score]
        
        middle_index = len(list) // 2 
        if self.tiebreak == 'RANDOM': 
            return random.choice(list)
        
        elif self.tiebreak == "LEFT": 
            return list[middle_index - self.lookahead]
        
        elif self.tiebreak == "RIGHT": 
            return list[middle_index + self.lookahead]
                   
    '''def opponent_score(scores): 
        if len(score) == 1: 
            return scores[0]
        else: 
            scores_rest = opponent_score(scores[1:])
            if scores[0] > scores_rest: 
                return score[0] 
            else: 
                return scores_rest'''
    #5 
    def scores_for(self, b): 
        scores=  [50, 50, 50, 50, 50, 50, 50 ]
        opponentchecker = self.opponent_checker() 
        
        for x in range(b.width):
            
            if b.can_add_to(x) == False: 
                scores[x] = -1
            else:    
                if b.is_win_for(self.checker) == True: 
                     scores[x] = 100 
                elif b.is_win_for(opponentchecker) == True: 
                    scores[x] == 0
                
                elif self.lookahead == 0: 
                    scores[x] = 50
                    
                else: 
                    b.add_checker(self.checker, x)
                    opponent = AIPlayer(opponentchecker, self.tiebreak, self.lookahead - 1)
                    opponentscore = opponent.scores_for(b)
                        
                    max_score = max(opponentscore)
                        
                    if max_score == 0: 
                        scores[x] = 100
                        
                    elif max_score == 100: 
                        scores[x] = 0 
                        
                    elif max_score == 50: 
                        scores[x] = 50 
                        
                    b.remove_checker(x)

                                
                    
        return scores
            
    
    #6 
    def next_move(self, b): 
        '''return the called AIPlayer‘s judgment of its best possible move.'''
        
        return self.max_score_column(self.scores_for(b))
    
    
    
#Deploying the Code 
connect_four(Player('X'), AIPlayer('O', 'RANDOM', 3))