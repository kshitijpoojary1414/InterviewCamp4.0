class PrefixSums :
    def subarrayEqualsO(self,arr):
        prefixSums = {}
        currentSum = 0

        for i in range(len(arr)) :
            currentSum += arr[i]
            if currentSum == 0 :
                return (0,i)
            elif currentSum in prefixSums :
                return (prefixSums[currentSum]+1,i)

            prefixSums[currentSum] = i

        return -1

    def subArraySumEqualsK(self, arr,k):
        prefixSums = {}
        currentSum = 0

        for i in range(len(arr)) :
            currentSum += arr[i]
            if currentSum == k :
                return (0,i)
            elif currentSum-k in prefixSums :
                return (prefixSums[currentSum-k]+1,i)

            prefixSums[currentSum] = i

        return -1