class Solution:
      def factorialOfN(self,n:int)->int:
          return self.helper(n)
      def helper(self,n:int):
          if n==1:
              return 1 
          return n*self.helper(n-1)
      
class TestApp:
      def testCaseOne(self):
          assert Solution().factorialOfN(5)==120
      def testCaseTwo(self):
          assert Solution().factorialOfN(4)==24