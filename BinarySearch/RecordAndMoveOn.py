class RecordAndMoveOn :
    def closestElement(self, nums, target ):
        result = float('inf')
        index = 0
        start = 0
        end = len(nums) - 1

        while start <= end :
            mid = start + (end - start )//2

            if result == float('inf') or abs(nums[mid]-target) < result :
                result = abs(nums[mid]-target)
                index = mid

            if nums[mid] == target :
                return mid
            elif target < nums[mid] :
                end = mid - 1
            else :
                start = mid + 1

        return index

