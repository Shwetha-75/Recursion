'''

Given an array arr[] of non-negative integers and a value sum, 
the task is to check if there is a subset of the given array 
whose sum is equal to the given sum. 

Examples: 

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 9
Output: True
Explanation: There is a subset (4, 5) with sum 9.

Input: arr[] = [3, 34, 4, 12, 5, 2], sum = 30
Output: False
Explanation: There is no subset that add up to 30.


'''
class Solution:
    def isSubsetSum (self, arr:list[int], sum:int):
        return self.helper(0,len(arr),0,sum,arr)
    def helper(self,index:int,n:int,sum:int,target:int,nums:list[int]):
        if index==n:
            if target==sum:
                return True 
            return False 
        if sum+nums[index]==target:return True
        left=self.helper(index+1,n,sum+nums[index],target,nums)
        right=self.helper(index+1,n,sum,target,nums)
        return left or right
        
class TestApp:
      def testCaseOne(self):
          assert Solution().isSubsetSum([3, 34, 4, 12, 5, 2],9)==True 
      def testCaseTwo(self):
          assert Solution().isSubsetSum([3, 34, 4, 12, 5, 2],30)==False 
      def testCaseThree(self):
          assert Solution().isSubsetSum([1,2,3],6)==True