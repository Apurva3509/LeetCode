class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Hashset for row and column to keep count and meet conditions
        # Hashset for each 3x3 grid to keep count of elements in each sub-grid

        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        grid = collections.defaultdict(set) # key = (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue

                # checks if current element(r,c) is in the hashset of rows[key=current_row] 
                # and cols[key=current_col] or in the subgrid hashset grid[key = (r//3, c//3)]
                # we will say board is not valid

                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in grid[(r//3, c//3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grid[(r//3, c//3)].add(board[r][c])
        return True
        