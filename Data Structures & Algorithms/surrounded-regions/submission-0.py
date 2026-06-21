class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c, island):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] == "X" or
                (r, c) in visit
            ):
                return False

            visit.add((r, c))
            island.append((r, c))

            touches_border = (
                r == 0 or c == 0 or
                r == ROWS - 1 or c == COLS - 1
            )

            touches_border |= dfs(r + 1, c, island)
            touches_border |= dfs(r - 1, c, island)
            touches_border |= dfs(r, c + 1, island)
            touches_border |= dfs(r, c - 1, island)

            return touches_border

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in visit:
                    island = []
                    border = dfs(r, c, island)

                    if not border:
                        for i, j in island:
                            board[i][j] = "X"