'''

You are given an integer array nums and an integer k. 
You want to find a subsequence of nums of length k that has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another 
array by deleting some or no elements without changing the 
order of the remaining elements.

 

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]
Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]
Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]
Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].
 

Constraints:

1 <= nums.length <= 1000
-105 <= nums[i] <= 105
1 <= k <= nums.length

'''

class Solution:
    def __init__(self):
        self.max_sum=0
        self.result=[]
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        self.helper(nums,0,len(nums),k,0,[])
        return self.result
        pass
    def helper(self,nums:list[int],index:int,n:int,k:int,sum:int,subset:list[int]):
        if index>=n:
            if len(subset)==k:
                if self.max_sum<sum:
                    self.result=subset[::]
                    self.max_sum=sum 
            return
        subset.append(nums[index])
        sum+=nums[index]
        self.helper(nums,index+1,n,k,sum,subset)
        subset.pop()
        sum-=nums[index]
        self.helper(nums,index+1,n,k,sum,subset) 
class TestApp:
    def testCaseOne(self):
        assert Solution().maxSubsequence([2,1,3,3],2)==[3,3]
    def testCaseTwo(self):
        assert Solution().maxSubsequence([-1,-2,3,4],3)==[-1,3,4]
    def testCaseThree(self):
        assert Solution().maxSubsequence([3,4,3,3],2)==[3,4]
        
            
        