class BackTracking :
    def pathExists(self, graph):
        memo = [[0 for i in range(len(graph[0]))] for j in range(len(graph))]
        self.backtrack(0,0,graph, memo , (len(graph)-1, len(graph[0]-1)))

    def backtrack(self, row, col, graph, memo, target):
        if self.outOfBounds(row,col) or graph[row][col] != 0 :
            return

        if row == target[0] and col == target[1] :
            return

        memo[row][col] = 1

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        for neighbor in directions :
            nRow = neighbor[0] + row
            nCol = neighbor[1] + col

            self.backtrack(nRow, nCol,graph, memo, target )

        return

    def outOfBounds(self, row, col, graph):
        if row < 0 or row >= len(graph ) or col <0 or col >= len(graph[0]) :
            return True

        return False
    def isInDictionary(self, word):
        return

    def wordBreak(self, s):
        memo = [0]* len(s)
        result = []
        if self.wordBreakHelper(s, 0, memo, result, []) :
            return result

    def wordBreakHelper(self, s, startIndex, memo, result, wordList):
        if startIndex == len(s) :
            result.append(wordList[::])
            return True

        if memo[startIndex] != 0 :
            return False


        word = ""
        for i in range(startIndex, len(s)) :
            word += s[i]

            if self.isInDictionary(word) :
                wordList.append(word)
                if self.wordBreakHelper(s, i + 1, memo, result) :
                    return True
                memo[i + 1] = 2
                wordList.pop()

        return False


