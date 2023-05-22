class PermuationsAndCombinations :
    def getCombos(self, nums):
        buffer = []
        result = []
        self.getCombosHelper(nums, 0, buffer)

    def getCombosHelper(self, nums, startIndex, buffer, result):
        if startIndex >= len(nums) :
            return

        if len(buffer) == len(nums) :
            result.append(buffer[::])
            return

        for i in range(startIndex, len(nums)) :
            buffer.append(nums[i])
            self.getCombosHelper(nums, i + 1, buffer, result)
            buffer.pop()

        return

    def get_letters(self,digit):
        if digit == 0:
            return []
        elif digit == 1:
            return []
        elif digit == 2:
            return ['a', 'b', 'c']
        elif digit == 3:
            return ['d', 'e', 'f']
        elif digit == 4:
            return ['g', 'h', 'i']
        elif digit == 5:
            return ['j', 'k', 'l']
        elif digit == 6:
            return ['m', 'n', 'o']
        elif digit == 7:
            return ['p', 'q', 'r', 's']
        elif digit == 8:
            return ['t', 'u', 'v']
        elif digit == 9:
            return ['w', 'x', 'y', 'z']

        raise ValueError("Invalid Digit " + str(digit))

    def getPhoneNumberMnemonics(self, digits):
        if len(digits) == 0 :
            return []
        buffer = []
        result = []
        self.getPhoneNumbersHelper(digits, 0, buffer, result )
        return result

    def getPhoneNumbersHelper(self, string, startIndex, buffer, result ):
        if len(buffer) == len(string) or startIndex == len(string) :
            result.append(buffer[::])
            return

        letters = self.get_letters(string[startIndex])

        for i in range(len(letters)) :
            buffer.append(letters[i])
            self.getPhonNumbersHelper(string, startIndex + 1 , buffer, result)
            buffer.pop()

        return

    def subsets(self, nums):
        buffer = []
        result = []

        self.subsetHelper(nums, 0, buffer, result)

    def subsetHelper(self, nums, startIndex, buffer, result):
        result.append(buffer[::])

        # not needed but good for understanding
        if startIndex == len(nums) :
            return

        for i in range(startIndex, len(nums)) :
            buffer.append(nums[i])
            self.subsetHelper(nums, i + 1 , buffer, result)
            buffer.pop()
        
        return

    def permutations(self, nums, X):
        result = []
        buffer = [0]*X
        isInBuffer = [False]*len(nums)
        self.permutationsHelper(nums, buffer, 0, isInBuffer, result)

    def permutationsHelper(self, nums, buffer, bufferIndex, isInBuffer, result):
        if bufferIndex == len(buffer) :
            result.append(buffer[::])
            return

        for i in range(len(nums)) :
            if not isInBuffer[i] :
                isInBuffer[i] = True
                buffer[bufferIndex] = nums[i]
                self.permutationsHelper(nums, buffer, bufferIndex + 1, isInBuffer, result)
                isInBuffer[i] = False

        return

    def coinChangeAllPossibilities(self, coins, target):
        result = []
        buffer = []
        self.coinChangeHelper(coins, 0, buffer, 0, result, target)

    def coinChangeHelper(self, coins, startIndex, buffer, currentSum, result, target):
        if startIndex == len(coins) :
            return

        if currentSum > target :
            return

        if currentSum == target :
            result.append(buffer[::])
            return

        for i in range(startIndex, len(coins)) :
            buffer.append(coins[i])
            currentSum += coins[i]
            self.coinChangeHelper(coins, i + 1, buffer, currentSum , result, target)
            buffer.pop()

        return


