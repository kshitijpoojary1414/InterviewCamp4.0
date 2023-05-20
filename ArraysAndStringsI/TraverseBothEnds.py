class TraverseBothEnds :
    def reverseArray(self, arr):
        if arr is None or len(arr) == 0 :
            return arr

        start = 0
        end = len(arr) - 1

        while start < end :
            temp = arr[end]
            arr[end] = arr[start]
            arr[start] = temp
            end -= 1
            start += 1

        return arr


    def twoSumSorted(self, arr, target):
        if len(arr) < 2 :
            return -1

        start = 0
        end = len(arr) - 1

        while start < end :
            currentSum = arr[start] + arr[end]

            if currentSum > target :
                end -= 1
            elif currentSum < target :
                start += 1
            else :
                return (start,end)

        return -1

    def squaresOfEachNumberInNonDecreasingOrder(self, arr):

        result = [0]*len(arr)

        start = 0
        end = len(arr) - 1
        rI = end
        while start <= end :
            if abs(arr[start]) > abs(arr[end]) :
                result[rI] = (arr[start]**2)
                start += 1
            else :
                result[rI] = (arr[end] ** 2)
                end -= 1
            rI -= 1
        return

    def unsortedSubArray(self, arr):
        leftDip,rightDip = -1,-1

        for i in range(1, len(arr)) :
            if arr[i] < arr[i-1] :
                leftDip = i

        for i in range(len(arr)-2,-1,-1) :
            if arr[i] > arr[i+1] :
                rightDip = i

        maximum, minimum = max(arr[leftDip:rightDip+1]), min(arr[leftDip:rightDip+1])

        while leftDip > 0 and arr[leftDip-1] < minimum :
            leftDip -= 1
        while rightDip > 0 and arr[rightDip-1] < minimum :
            rightDip -= 1

        return (leftDip,rightDip)



