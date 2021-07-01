# https://leetcode.com/problems/two-sum/

def sortSecond(num):
    return num[0]

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_pair_with_index = []
        for i in range(len(nums)):
            nums_pair_with_index.append([nums[i],i])
        
        nums_pair_with_index.sort(key = sortSecond)
        i = 0
        j = len(nums_pair_with_index)-1
        while(i < j):
            if nums_pair_with_index[i][0] + nums_pair_with_index[j][0] > target:
                j = j - 1
            elif nums_pair_with_index[i][0] + nums_pair_with_index[j][0] < target:
                i = i + 1
            else:
                return [nums_pair_with_index[i][1],nums_pair_with_index[j][1]]