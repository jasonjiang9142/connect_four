
# Playing the game 
 

from Board import Board
from Classes import Player
import random
    
def connect_four(p1, p2): # Not Done 
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    while True:
        
        if process_move(p1, b) == True:
            
            return b

        if process_move(p2, b) == True:
            return b

 
def process_move(p, b):
    count = 0
    print(p, "'s", 'turn')
    print()
    nextmove = p.next_move(b)
    b.add_checker(p.checker, nextmove)
    count += 1
    print() 
    
    print(b) 

    if b.is_win_for(p.checker) == True: 
        print(p, 'wins in', count, "move") 
        print("Congratulations!" )
        return True 
            
    elif b.is_win_for(p.opponent_checker()) == True: 
        print(p.opponent_checker(), 'wins in', count, "move") 
        print("Congratulations!" )
        return True 
            
            
    elif b.is_full() == True and b.is_win_for(p.checker) == False and b.is_win_for(p.opponent_checker()) == False: 
        print("It's a tie!")
        return True 
            
    else: 
        return False 
            

#3 Done 
class RandomPlayer(Player): 
    '''used for an unintelligent computer player that chooses at random from the available columns.'''
    
    def next_move(self, b): 
        '''choose at random from the columns in the board b that are not yet full, 
        and return the index of that randomly selected column.'''
        
        list = [] 
        count = 0 
        
        for col in range(b.width): 
            if b.can_add_to(col) == True: 
                list += [col]
        
        return random.choice(list)
        
        
        ''' create a list that represents items in the columns that are not full. 
        then use the random method to randomly make a choice form the list '''
    

    
connect_four(Player('X'), RandomPlayer('O'))
    
        
    
        