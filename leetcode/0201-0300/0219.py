class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_index = {}
        for i in range(len(nums)):
            if last_index.get(nums[i], -1) == -1:
                last_index[nums[i]] = i
            else:
                if i - last_index[nums[i]] <= k:
                    return True
                else:
                    last_index[nums[i]] = i
        return False
