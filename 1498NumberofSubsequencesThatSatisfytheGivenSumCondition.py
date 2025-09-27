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