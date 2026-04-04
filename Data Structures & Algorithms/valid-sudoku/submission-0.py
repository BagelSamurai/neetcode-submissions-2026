class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
      
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {(r, c): set() for r in range(3) for c in range(3)}

        for row in range(9):
            for column in range(9):
                val = board[row][column]

                if val == ".":
                    continue
                
              
                if val in rows[row] or val in cols[column] or val in boxes[(row//3, column//3)]:
                    return False
                
                rows[row].add(val)
                cols[column].add(val)
                boxes[(row//3, column//3)].add(val)
        print(boxes)
         
        return True