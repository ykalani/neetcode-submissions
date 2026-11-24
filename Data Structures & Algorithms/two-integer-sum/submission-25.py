from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)
        for i, num in enumerate(nums): 
            compliment = target - num 
            if compliment in seen: 
                return([seen[compliment], i])
            seen[num] = i 
            