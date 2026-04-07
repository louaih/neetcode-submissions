class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ignore = {"."}
        for i in range(len(board)):
            row_vals = [x for x in board[i] if x != "."]
            if len(set(row_vals)) != len(row_vals):
                # Rows
                print("in rows")
                return False

        transpose = [list(row) for row in zip(*board)]
        for col in range(len(transpose)):
            col_vals = [x for x in transpose[col] if x != "."]
            if len(set(col_vals)) != len(col_vals):
                # Cols
                print("in cols")
                return False
            
        # 3x3
        square_counter = [[] for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[0])):
                square_index = (col // 3) + (row // 3) * 3
                if board[row][col] != '.':
                    square_counter[square_index].append(board[row][col])

        for square in square_counter:
            if len(set(square)) != len(square):
                print("in square")
                return False

        return True

        