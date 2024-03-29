# go left to right then right to left
class Solution:
    def productExceptSelf(self, nums):
        res = [1]*len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

        # res = [1]*len(nums)
        # left = [1]*len(nums)
        # right = [1]*len(nums)
        
        # prefix = 1
        # for i in range(len(nums)):
        #     left[i] = prefix
        #     prefix *= nums[i]
        
        # postfix = 1
        # for i in range(len(nums)-1,-1,-1):
        #     right[i] = postfix
        #     postfix *= nums[i]
        
        # for i in range(len(nums)):
        #     res[i] = left[i]*right[i]
        # return res