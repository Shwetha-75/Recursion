'''

You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the 
sum of the minimum and maximum element on it is less or equal to target. 
Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106

'''
class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        result=[]
        self.helper(nums,[],result,len(nums),0)
        count=0
        for res in result:
            if not res:
                continue 
            if min(res)+max(res)<=target:
                count+=1
        return count
        
        
    def helper(self,nums:list,subset:list[int],result:list[list[int]],n:int,index:int):
        if index==n:
            result.append(subset[::])
            return 
        subset.append(nums[index])
        self.helper(nums,subset,result,n,index+1)
        subset.pop()
        self.helper(nums,subset,result,n,index+1)
        
class Solution:
    def __init__(self):
        self.count=0
    def numSubseq(self, nums: list[int], target: int) -> int:
        self.findMinMaxCount(target,nums,float('inf'),float('-inf'),0,len(nums))
        return self.count
    def findMinMaxCount(self,target:int,nums:list[int],min_value:int,max_value:int,index:int,n:int):
        if index>=n:
            if min_value!=float('inf') and min_value+max_value<=target:
                self.count+=1
                
            return 
        self.findMinMaxCount(target,nums,min(min_value,nums[index]),max(max_value,nums[index]),index+1,n)
        self.findMinMaxCount(target,nums,min_value,max_value,index+1,n)       

class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        return self.helper(nums,len(nums),0,[],target,float('inf'),float('-inf'))

    def helper(self,nums:list[int],n:int,index:int,subset:list[int],target:int,min_value:int,max_value:int)->int:
        if index>=n:
            return 1 if min_value!=float('inf')and min_value+max_value <=target else 0 
        subset.append(nums[index])
        left=self.helper(nums,n,index+1,subset,target,min(min_value,nums[index]),max(max_value,nums[index]))
        subset.pop()
        right=self.helper(nums,n,index+1,subset,target,min_value,max_value)
        return left+right

# class Solution:
#       def numSubseq(self, nums: list[int], target: int) -> int:
#           n=len(nums)
#           powerExponent=[1]*(n+1)
#           mod=10**9+7
#           count=0
#           for i in range(1,n+1):
#               powerExponent[i]=(powerExponent[i-1]<<1)%mod 
#           low,high=0,n-1 
#           while low<=high:
#                 if nums[low]+nums[high]<=target:
#                     count=(count+powerExponent[high-low]%mod)
#                     low+=1
#                 else:
#                     high-=1
#           return count
                    
             

class TestApp:
      def testCaseOne(self):
          assert Solution().numSubseq([3,5,6,7],9)==4
      def testCaseTwo(self):
          assert Solution().numSubseq([3,3,6,8],10)==6
      def testCaseThree(self):
          assert Solution().numSubseq([2,3,3,4,6,7],12)==61