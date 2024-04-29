class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        cur = nums[0]
        for j in range(1,len(nums)):
            if cur  != nums[j]:
                nums[i] = nums[j]
                print(nums[i])
                cur = nums[j]
                i+=1
        return i
        