class PartitioningArrays :
    def dutchNationalFlag(self, arr, pivot):
        leftBoundary = 0
        rightBoundary = len(arr)-1
        i = 0
        while i < len(arr) :
            temp = arr[i]
            if arr[i] < pivot :
                arr[i] = arr[leftBoundary]
                arr[leftBoundary] = temp
                i += 1
                leftBoundary += 1
            elif arr[i] > pivot :
                arr[i] = arr[rightBoundary]
                arr[rightBoundary] = temp
                rightBoundary -= 1
            else :
                i += 1

        return arr
