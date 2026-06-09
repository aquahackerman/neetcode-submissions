class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()

        m = len(matrix)
        n = len(matrix[0])

        # Find all rows and columns that contain a zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Zero out cells
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0