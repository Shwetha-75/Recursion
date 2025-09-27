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
        
            
        