#  print all sub sequence of an array

class Solution:
      def printSubSequence(self,nums:list[int]):
          result=[]
          self.helper(len(nums),nums,0,[],result) 
          print(result)
          return result
      def helper(self,n:int,nums:list[int],index:int,subset:list[int],result:list[int]):
          if index>=n:
              result.append(subset[::])
              return 
          subset.append(nums[index])
          self.helper(n,nums,index+1,subset,result)
          subset.pop()
          self.helper(n,nums,index+1,subset,result)
          
class TestApp:
      def testCaseOne(self):
          assert Solution().printSubSequence([3,1,2])==[[3,1,2],[3,1],[3,2],[3],[1,2],[1],[2],[]]
    