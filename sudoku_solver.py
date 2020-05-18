class Board:
    def __init__(self):
        self.sudoku_matrix = None
        self.numbers = []
        self.count = None


    def setup(self): # Define a sudoku puzzle here
        self.sudoku_matrix = [  [ 2, 0, 0, 0, 4, 0, 7, 0, 0, ], 
                                [ 0, 1, 0, 0, 0, 0, 0, 0, 0, ], 
                                [ 0, 0, 0, 0, 2, 0, 1, 3, 4, ], 
                                [ 4, 5, 0, 0, 0, 8, 0, 0, 0, ], 
                                [ 7, 0, 2, 0, 1, 0, 0, 0, 0, ], 
                                [ 1, 0, 0, 0, 0, 0, 3, 6, 0, ], 
                                [ 0, 0, 0, 0, 0, 0, 6, 0, 8, ], 
                                [ 0, 0, 8, 0, 5, 4, 0, 0, 3, ], 
                                [ 0, 0, 0, 0, 0, 7, 0, 0, 0, ] ]

        self.count = 1


    def draw_board(self): # draws the sudoku board
        print(" ")
        print(f"******** Solution {self.count} ********")
        for item in range(9):
            print(self.sudoku_matrix[item])    
        print("****************************")

        self.count = self.count + 1 # Update count for nest solution


    def possible(self, y, x, n):
    # determines if it is possible for number [n] to be in the square[y][x]
    # Inputs: y = column number, x = row number, n = number to be checked
        for i in range(9): # Check column y for n
            if self.sudoku_matrix[y][i] == n:
                return False
        for i in range(9): # Check row x for n
            if self.sudoku_matrix[i][x] == n:
                return False
        x0 = (x//3)*3 # Check box for n
        y0 = (y//3)*3
        for i in range(3):
            for j in range(3):
                if self.sudoku_matrix[y0+i][x0+j] == n:
                    return False
        return True


    def solver(self): # Solves sudoku using backtracking and recursion
        for y in range(9): # find empty position
            for x in range(9):
                if self.sudoku_matrix[y][x] == 0:
                    for n in range(1, 10): # checks possible answers for empty square
                        if self.possible(y,x,n):
                            self.sudoku_matrix[y][x] = n # Enter possible answer
                            self.solver() # continue to solve puzzle
                            self.sudoku_matrix[y][x] = 0 # backtrack if solution impossible
                    return
        self.draw_board() # print once a solution is found

    
def main():
    s1 = Board()
    s1.setup()
    s1.solver()

if __name__ == "__main__":
    main()


# possibly insert testing
# def test_solve():
#     s1 = Board()
#     s1.setup()
#     s1.solver()

#     assert s1.sudoku_matrix == [
# [2, 9, 5, 3, 4, 1, 7, 8, 6],
# [3, 1, 4, 7, 8, 6, 5, 9, 2],
# [8, 6, 7, 5, 2, 9, 1, 3, 4],
# [4, 5, 6, 9, 3, 8, 2, 1, 7],
# [7, 3, 2, 6, 1, 5, 8, 4, 9],
# [1, 8, 9, 4, 7, 2, 3, 6, 5],
# [5, 4, 1, 2, 9, 3, 6, 7, 8],
# [6, 7, 8, 1, 5, 4, 9, 2, 3],
# [9, 2, 3, 8, 6, 7, 4, 5, 1],
#     ]