
# A Connect Four Board class


class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    ### add your constructor here ###
    def __init__(self, height, width): 
        ''' constructs a new Board object by initializing the following three attributes:'''
        
        self.height = height 
        self.width = width 
        self.slots =  [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object.
        """
        s = ''         #  begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        
        
        #1 Done 
        for x in range(1):
            ''' add a line of hyphen characters (-) that is wide enough to cover all of the columns.'''
            s += '-'
            for col in range(self.width): 
                s += '--'
                
            s += '\n'
            
            
        #2 Done 
        for x in range(self.width): 
            '''add a line of numeric column labels for all of the columns.'''
            s += ' ' + str(x % 10) 
            
        s += '\n'
                
        
        return s
    
    
    #3 done
    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        
        row = 0 
        
        while row < (self.height -1): 
            if self.slots[row][col] == ' ': 
                if self.slots[row + 1][col] == ' ':
                    row += 1 
                    
                elif self.slots[row + 1][col] != ' ': 
                    self.slots[row][col] = checker 
                    break
                    
        self.slots[row][col] = checker 

    #4  Done 
    def reset(self): 
        '''reset the Board object on which it is called by setting all slots to contain a space character.'''
        
        self.slots =  [[' '] * self.width for row in range(self.height)]
    
    
    ### add your reset method here ###
    
    #5 
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    #6  Done 
    def can_add_to(self, col) :
        '''True if it is valid to place a checker in the column col
        on the calling Board object. Otherwise, it should return False.'''
        
        if 0 > col or col > (self.width -1): 
            return False 
        else: 
            if self.slots[0][col] == ' ': 
                return True 
            elif self.slots[0][col] != ' ': 
                return False 
    
    #7 Done 
    def is_full(self): 
        '''True if the called Board object is completely
        full of checkers, and returns False otherwise.'''
        
        count = 0
        for cols in range(self.width): 
            column_full = self.can_add_to(cols)
            if column_full == False: 
                count += 1
            elif column_full == True: 
                count = count 
        
        if count == self.width: 
            return True 
        elif count != self.width: 
            return False
    
    #8 Done 
    def remove_checker(self, col): 
        '''removes the top checker from column col of the called Board object. 
        If the column is empty, then the method should do nothing.'''
        
        row = 0 
        if self.slots[0][col] != ' ':
            self.slots[0][col] = ' '
        
        elif self.slots[row][col] == ' ': 
            
            if row != self.height -1: 
                while self.slots[row][col] == ' ' and row != self.height - 1: 
                    row += 1
                    if self.slots[row][col] != ' ': 
                        self.slots[row][col] = ' '
                        break 
            elif row == self.height -1:
                self.slots[row][col] = ' '
                
        return self.slots
                
    #9 
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
    
        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker): 
        ''' checks for a vertizal win for the specified checker''' 
        
        for row in range(self.height - 3): 
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col] == checker and \
                    self.slots[row + 2][col] == checker and \
                    self.slots[row + 3][col] == checker:
                        return True
                      
        # if we make it here, there were no horizontal wins
        return False

    def is_down_diagonal_win(self, checker): 
        '''  (or diagonals that go down from left to right'''
        
        for row in range(0, self.height -3  ): 
            for col in range(self.width - 3): 
                if self.slots[row][col] == checker and \
                    self.slots[row + 1][col + 1] == checker and \
                    self.slots[row + 2][col + 2] == checker and \
                    self.slots[row + 3][col + 3] == checker : 
                        return True 
        return False 
                 
    def is_up_diagonal_win(self, checker): 
        '''  (or diagonals that go up from left to right'''
        
        for row in range(3, self.height): 
            for col in range(self.width - 3): 
                if self.slots[row][col] == checker and \
                    self.slots[row - 1][col + 1] == checker and \
                    self.slots[row - 2][col + 2] == checker and \
                    self.slots[row - 3][col + 3] == checker : 
                        return True 
        return False       
        
        
        
    def is_win_for(self, checker): 
        '''accepts a parameter checker that is either 'X' or 'O', and returns 
        True if there are four consecutive slots containing checker on the board. 
        Otherwise, it should return False.'''

        assert(checker == 'X' or checker == 'O')
        # call the helper functions and use their return values to
        # determine whether to return True or False
        
        if self.is_horizontal_win(checker) == True: 
            return True 
        else: 
            if self.is_vertical_win(checker) == True: 
                return True 
            else: 
                if self.is_down_diagonal_win(checker) == True: 
                    return True 
                else: 
                    if self.is_up_diagonal_win(checker) == True: 
                        return True 
                    else: 
                        return False 
                
            
            
            
            
        ''' use helper function go down each list
        if the first function returns true: 
            return true 
        else: 
            go to the second function and repeat code for the next 2 helper function '''



        