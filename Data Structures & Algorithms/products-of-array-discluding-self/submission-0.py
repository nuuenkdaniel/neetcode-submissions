class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_arr = [1]*n
        final_arr = [1]*n
        # Product of number left to right
        for i in range(1, n):
            prefix_arr[i] = prefix_arr[i-1]*nums[i-1]

        # Product of numbers right to left
        for i in range(n-2, -1, -1):
            final_arr[i] = final_arr[i+1]*nums[i+1]

        # Product of the 2 arrays
        for i in range(1, n):
            final_arr[i] = final_arr[i]*prefix_arr[i]

        return final_arr
