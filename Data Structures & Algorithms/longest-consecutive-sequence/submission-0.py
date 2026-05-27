class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Get hashmap of seen values
        seen = {}
        for num in nums:
            seen[num] = 1

        # Use keys to find start of sequences
        max_con = 0
        for key in seen.keys():
            if seen.get(key-1, 0) == 0:
                next_key = key+1
                while seen.get(next_key, 0) != 0:
                    seen[key] += 1
                    next_key += 1
            max_con = max(max_con, seen.get(key, 0))

        return max_con
