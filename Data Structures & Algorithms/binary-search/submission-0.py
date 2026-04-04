class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        # find middle element 
        middle_element = nums[size//2]
        if target<middle_element:
            for i in range(0,size):
                if nums[i] == target:
                    return i
        else:
            for i in range(size//2, size):
                if nums[i] == target:
                    return i

        return -1