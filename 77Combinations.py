class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        array=[i for i in range(1,n+1)]
        result=[]
        self.helper(array,result,[],n,0,k)
        return result
    def helper(self,array:list[int],result:list[list[int]],subset:list[int],n:int,index:int,k:int):
        if index==n:
           if len(subset)==k:
               result.append(subset[::])
           return 
        subset.append(array[index])
        self.helper(array,result,subset,n,index+1,k)
        subset.pop()
        self.helper(array,result,subset,n,index+1,k)
class TestApp:
      def testCaseOne(self):
          assert Solution().combine(4,2)
        
        