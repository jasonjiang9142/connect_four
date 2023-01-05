
# A Connect-Four Player class 


from Board import Board

# write your class below.
#
class Player: 
    
    #1 Done
    def __init__(self, checker): 
    
        assert(checker == 'X' or checker == 'O')
        # call the helper functions and use their return values to
        # determine whether to return True or False
        
        '''constructs a new Player object by initializing the following two attributes:'''
        self.checker = checker 
        self.num_moves = 0
    
    #2 Done 
    def __repr__(self): 
        ''' returns a string representing a Player object.'''
        return 'Player ' + str(self.checker) 
        
    #3 Done
    def opponent_checker(self): 
        '''returns a one-character string representing the checker of the Player object’s opponent. '''
        if self.checker == 'X': 
            return 'O'
        elif self.checker == 'O': 
            return 'X'
        
    #4 Done 
    def next_move(self, b): 
        '''accepts a Board object b as a parameter and returns the column 
        where the player wants to make the next move. '''
        
        self.num_moves += 1 
        
        while True: 
            
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True: 
                return col
                break 
            elif b.can_add_to(col) == False: 
                print('Try Again!')
                      
    
        
        
    