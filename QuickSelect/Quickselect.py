import random


class QuickSelect :
    def findKthSmallest(self, nums, k):
        return self.select(0, len(nums)-1, k)

    def findKthLargest(self, arr, k) -> int:
        return self.select(0, len(arr) - 1, arr, len(arr) - k)

    def singlePartiton(self, left, right, nums, pivot_index):
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

        for i in range(left, right):
            if nums[i] < nums[right]:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1

        nums[left], nums[right] = nums[right], nums[left]
        return left

    def select(self, left, right, nums, k):
        if right == left:
            return nums[left]

        pivot_index = random.randint(left, right)
        pivot_index = self.singlePartiton(left, right, nums, pivot_index)

        if pivot_index == k:
            return nums[pivot_index]
        elif k < pivot_index:
            return self.select(0, pivot_index - 1, nums, k)
        else:
            return self.select(pivot_index + 1, right, nums, k)

