class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #create 2d arrays to map each row, col, box to a count of nums in an array of size 9 (1-9)
        #basic logic is that if ever the count already has a number that you are trying to add immediately exit and return false
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        def cube(i,j,rows,cols,boxes, index):  
            print(f"index: {index}")
            for k in range(i,i+3):
                for l in range(j,j+3):
                    
                    if board[k][l] != ".":
                        print(f"l: {l}, k: {k}")
                        print(board[k][l])
                        if board[k][l] in boxes[index]:
                            return False
                        elif board[k][l] in rows[k]:
                            return False
                        elif board[k][l] in cols[l]:
                            return False
                        else:
                            boxes[index].add(board[k][l])
                            rows[k].add(board[k][l])
                            cols[l].add(board[k][l])
                        print(boxes)
                        print(cols)
                        print(rows)
            
            return True
        count = 0
        for i in range(0,9,3):
            for j in range(0,9,3):
                
                print(i,j)
                if not cube(i,j,rows,cols,boxes,count):
                    return False
                count+=1
        return True



