class TwoDArrays:
    def rotateImage(self, matrix):
        l = 0
        r = len(matrix) - 1
        grid = matrix
        while l < r:
            for i in range(r - l):
                top, bottom = l, r

                temp = grid[top][l + i]
                grid[top][l + i] = grid[bottom - i][l]
                grid[bottom - i][l] = grid[bottom][bottom - i]
                grid[bottom][bottom - i] = grid[top + i][bottom]
                grid[top + i][bottom] = temp

            r -= 1
            l += 1
