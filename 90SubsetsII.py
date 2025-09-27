'''
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        result=[]
        nums.sort()
        self.helper(0,len(nums),[],result,nums)
        return result
        pass
    def helper(self,index:int,n:int,subset:list[int],result:list[list[int]],nums:list[int]):
        result.append(subset[::])
        for i in range(index,n):
            if i!=index and nums[i]==nums[i-1]: continue 
            subset.append(nums[index])
            self.helper(i+1,n,subset,result,nums)
            subset.pop()


class TestApp:
      def testCaseOne(self):
          assert Solution().subsetsWithDup([1,2,2])==[[],[1],[1,2],[1,2,2],[2],[2,2]]
      def testCaseTwo(self):
          assert Solution().subsetsWithDup([0])==[[],[0]]