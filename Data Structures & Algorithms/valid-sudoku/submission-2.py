class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create 2d arrays to map each row, col, box to a count of nums in an array of size 9 (1-9)
        #basic logic is that if ever the count already has a number that you are trying to add immediately exit and return false
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                index = (i//3)*3+(j//3)
                if board[i][j] != ".":
                    if board[i][j] in boxes[index]:
                        return False
                    elif board[i][j] in rows[i]:
                        return False
                    elif board[i][j] in cols[j]:
                        return False
                    else:
                        boxes[index].add(board[i][j])
                        rows[i].add(board[i][j])
                        cols[j].add(board[i][j])
                
        return True



