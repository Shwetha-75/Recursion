'''

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.


'''
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result=[]
        n=len(nums)
        subset=[]
        freq=[False]*n 
        self.helper(freq,nums,subset,result,n)
        return result

    def helper(self,freq:list[bool],nums:list[int],subset:list[int],result:list[list[int]],n:int):
        if len(subset)==n:
            result.append(subset[::])
            return 
        for i in range(n):
            if not freq[i]:
                freq[i]=True 
                subset.append(nums[i])
                self.helper(freq,nums,subset,result,n)
                subset.pop()
                freq[i]=False
                
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result=[]
        self.helper(0,nums,result)
        return result

    def helper(self,index:int,nums:list[int],result:list[list[int]],):
        if index==len(nums):
            result.append(nums[::])
            return 
        for i in range(index,len(nums)):
            nums[index],nums[i]=nums[i],nums[index]
            self.helper(index+1,nums,result)
            nums[index],nums[i]=nums[i],nums[index]


Solution().permute([1,2,3])
