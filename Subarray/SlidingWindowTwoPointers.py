class SlidingWindow :
    def subarraySumPositive(self,arr, target):
        start  = 0
        end = 0
        currentSum = arr[start]

        while start < len(arr) :
            if end < start :
                end = start
                currentSum = arr[start]

            if currentSum > target :
                currentSum -= target
                start += 1

            elif currentSum < target :
                if end == len(arr)-1 :
                    break
                end += 1

                currentSum += arr[end]

            else :
                return (start,end)

        return -1

    def longestSubstringWithoutRepeatingCharacters(self, s):
        if len(s) == 0:
            return 0

        windowMap = {}
        start = 0
        end = 0
        result = 1

        while end < len(s):
            char = s[end]

            if char in windowMap and windowMap[char] >= start:
                start = windowMap[char] + 1

            windowMap[char] = end

            result = max(end - start + 1, result)
            end += 1

        return result