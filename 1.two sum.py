class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashTable={}
        for i in range(len(nums)):
            if target-nums[i] in hashTable:
                return [hashTable[target-nums[i]],i]
            else:
                hashTable[nums[i]]=i
