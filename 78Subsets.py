'''

Given an integer array nums of unique elements,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets. 
Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

'''

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result=[]
        self.helper(0,len(nums),nums,[],result)
        return result
        
    def helper(self,index:int,n:int,nums:list[int],subset:list[int],result:list[list[int]]):
        if index==n:
            result.append(subset[::])
            return 
        subset.append(nums[index])
        self.helper(index+1,n,nums,subset,result)
        subset.pop()
        self.helper(index+1,n,nums,subset,result)
class TestApp:
      def testCaseOne(self):
          assert Solution().subsets([1,2,3])==[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]] or [[1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], []]
      def testCaseTwo(self):
          assert Solution().subsets([0])==[[],[0]] or [[0],[]]