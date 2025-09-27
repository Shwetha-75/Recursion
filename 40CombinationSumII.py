class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result={}
        candidates.sort()
        self.helper(0,len(candidates),target,[],result,candidates)
        result=list(result.values())
        # result.sort()
        return result
    def helper(self,index:int,n:int,target:int,subset:list[int],result,candidates:list[int]):
        if index==n:
            if not target:
                if str(subset) not in result:
                    result[str(subset[:])]=subset[:]
            return 
        if candidates[index]<=target:
            subset.append(candidates[index])
            self.helper(index+1,n,target-candidates[index],subset,result,candidates)
            subset.pop()
        self.helper(index+1,n,target,subset,result,candidates)
               
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result=[]
        candidates.sort()
        self.helper(0,len(candidates),target,[],result,candidates)
        return result
               
    def helper(self,index:int,n:int,target:int,subset:list[int],result:list[list],candidates:list[int]):
        if not target:
            result.append(subset[:])
            return 
        for i in range(index,n):
            if i>index and candidates[i-1]==candidates[i]: continue 
            if candidates[i]>target: break 
            subset.append(candidates[i])
            self.helper(i+1,n,target-candidates[i],subset,result,candidates)
            subset.pop()
                                                                                                      
        
class TestApp:
    
    def testCaseOne(self):
        assert Solution().combinationSum2([10,1,2,7,6,1,5],8)==[[1,1,6],[1,2,5],[1,7],[2,6]]
    def testCaseTwo(self):
        assert Solution().combinationSum2([2,5,2,1,2],5)==[[1,2,2],[5]]