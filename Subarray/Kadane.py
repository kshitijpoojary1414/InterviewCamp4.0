class Kadane :
    def kadane(self, arr):
        maxSoFar = arr[0]
        result = arr[0]

        for i in range(1,len(arr)) :
             val = arr[i]
             maxSoFar = max(val, val + maxSoFar)
             result = max(result,maxSoFar)

        return result