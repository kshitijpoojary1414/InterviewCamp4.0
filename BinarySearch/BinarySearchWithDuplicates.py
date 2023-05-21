class BinarySearchWithDuplicates :
    def findFirstOccurence(self,nums,target) :
        start = 0
        end = len(nums)-1

        while start <= end :
            mid = start + (end - start)//2
            # print(mid,nums)
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target) :
                return mid
            elif nums[mid] < target :
                start = mid + 1
            else :
                end = mid - 1

        return -1
    ''' This is Template 1 of Binary Search 
        This works because whenever you find an element that is either less than or equal to target you keep the mid
        pointed at that element instead of moving backward, that way if our mid already points at the first occurence
        of the element , the binary search will just keep reducing the search space and eventually there will be just two 
        elements. Since we pick the mid such that , in case of two elements we will always pick the first one. This will force
        the binary search to reduce the search space because if mid is the first occuring element then mid -1 ie start willl be 
        less than mid and hence start = mid + 1 will be called 
    '''
    def findFirstOccurenceT1(self, nums, target):
        start = 0
        end = len(nums) - 1
        print(nums)
        while start < end:
            mid = start + (end - start) // 2
            if target <= nums[mid]:
                end = mid
            else:
                start = mid + 1

        if nums[start] == target:
            return start
        return -1

    def findLastOccurence(self,nums,target) :
        start = 0
        end = len(nums)-1

        while start <= end :
            mid = start + (end - start)//2

            if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] != target) :
                return mid
            elif nums[mid] > target :
                end = mid - 1
            else :
                start = mid + 1

        return -1

    ''' This is Template 1 of Binary Search 
        This works because whenever you find an element that is either greater than or equal to target you keep the mid
        pointed at that element instead of moving forward, that way if our mid already points at the last occurence
        of the element , the binary search will just keep reducing the search space and eventually there will be just two 
        elements. Since we pick the mid such that , in case of two elements we will always pick the second one(you do this
        by adding a +1 while selecting the mid). This will force the binary search to reduce the search space because if 
        mid is the first occuring element then mid -1 ie start willl be 
        less than mid and hence start = mid + 1 will be called 
    '''
    def findLastOccurence(self,nums,target) :
        start = 0
        end = len(nums)-1
        print(nums)
        while start < end :
            mid = start + (end - start + 1)//2
            print(start,mid,end)
            if target >= nums[mid] :
                start = mid
            else :
                end = mid - 1
        if nums[start] == target :
            return start
        return -1

    def searchInsertPosition(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end :
            mid = start + (end-start)//2

            if target >= nums[mid] :
                start = mid + 1
            else :
                end = mid - 1

        return start