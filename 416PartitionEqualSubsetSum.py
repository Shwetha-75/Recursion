'''

Given an integer array nums, return true if you can partition the array 
into two subsets such that the sum of the elements in both subsets 
is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100

'''

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total=sum(nums)
        return self.helper(0,len(nums),0,total,nums)
    def helper(self,index:int,n:int,sum:int,total:int,nums:list[int]):
        if index==n:
            if total-sum==sum:
                return True 
            return False 
        if total-(sum+nums[index])==sum+nums[index]:
            return True 
        if (sum+nums[index])>total//2: return False 
        left=self.helper(index+1,n,sum+nums[index],total,nums)
        right=self.helper(index+1,n,sum,total,nums)
        return left or right
class TestApp:
      def testCaseOne(self):
          assert Solution().canPartition([1,5,11,5])==True 
      def testCaseTwo(self):
          assert Solution().canPartition([1,2,3,5])==False