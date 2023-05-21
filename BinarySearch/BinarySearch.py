class BinarySearch :
    def binarySearch(self, arr, target):
        start = 0
        end = len(arr)- 1

        while start <= end :
            mid = start + (end-start + 1)//2

            if arr[mid] < target :
                start = mid + 1
            elif arr[mid] > target :
                end = mid - 1
            else :
                return mid

        return -1