class SpecialTricks :
    def minimumiNumberInASortedArray(self, nums):
        start = 0
        originalEnd = len(nums) - 1
        end = len(nums) - 1

        while start <= end :
            mid = start + (end - start)//2

            if nums[mid] < nums[originalEnd] and (mid != 0 and nums[mid-1] < nums[mid]) :
                end = mid - 1
            elif nums[mid] > nums[originalEnd] :
                start = mid + 1
            else :
                return nums[mid]

        return -1

    def minimumiNumberInASortedArray2(self, nums):
        start = 0
        originalEnd = len(nums) - 1
        end = len(nums) - 1

        while start <= end :
            mid = start + (end - start)//2

            if nums[mid] <= nums[originalEnd] and (mid == 0 or nums[mid - 1] > nums[mid]):
                return nums[mid]
            elif nums[mid] > nums[originalEnd]:
                start = mid + 1
            else:
                end = mid - 1

        return -1

    def findEndRange(self, nums):
        start = 2

        while True :
            try :
                num = nums[start]
                start *= 2
            except :
                return (start/2, start )

    def findExactEnd(self, nums, start, end):

        while start <= end :
            mid = start + (end - start)//2
            try :
                num = nums[mid]
            except :
                end = mid - 1
                continue

            try :
                num = nums[mid+1]
            except :
                return mid

            start = mid + 1



    def binarySearchOnNoLengthArray(self, nums, target):
        start,end = self.findEndRange(nums)
        end = self.findExactEnd(nums, start, end )
        start = 0
        while start <= end :
            mid = start + (end - start) // 2

            if target < nums[mid] :
                end = mid - 1
            elif target > nums[mid] :
                start = mid + 1
            else :
                return mid
        return -1

    def findPeakElement(self, nums):
        nums.append(float('inf'))

        start = 0
        end = len(nums) - 1

        while start <= end :
            mid = start + (end - start)//2

            if nums[mid-1] < nums[mid] and nums[mid+1]  > nums[mid] :
                start = mid + 1
            elif nums[mid-1] > nums[mid] and nums[mid +1] > nums[mid] :
                end = mid - 1
            elif nums[mid+1] > nums[mid] and nums[mid + 1] > nums[mid] :
                end = mid - 1
            else :
                return mid

        return -1