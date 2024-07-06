class Solution(object):
    def sortColors(self, nums):
        def quicksort(arr):
            if len(arr) <= 1:
                return arr
            else:
                pivot = arr[len(arr) // 2]
                left = [x for x in arr if x < pivot]
                middle = [x for x in arr if x == pivot]
                right = [x for x in arr if x > pivot]
                return quicksort(left) + middle + quicksort(right)
        
        sorted_nums = quicksort(nums)
        
        for i in range(len(nums)):
            nums[i] = sorted_nums[i]