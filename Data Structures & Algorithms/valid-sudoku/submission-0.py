class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                if cell == '.':
                    continue
                box_index = (i//3) * 3 + (j//3)
                if cell in rows[i]:
                    return False
                if cell in cols[j]:
                    return False
                if cell in boxes[box_index]:
                    return False;

                rows[i].add(cell)
                cols[j].add(cell)
                boxes[box_index].add(cell)
        return True