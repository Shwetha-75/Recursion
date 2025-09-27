'''
Given an interger n. Your task is to cslculate the sum of all natural numbers from 
1 up to n (inclusive). If n is 0, the sum should be 0.

Examples:

Input: n = 3
Output: 6
Explanation: The numbers from 1 to 3 are 1, 2, and 3. 
Their sum is 1 + 2 + 3 = 6.

Input: n = 5
Output: 15
Explanation: The numbers from 1 to 5 are 1, 2, 3, 4, and 5. 

Their sum is 1 + 2 + 3 + 4 + 5 = 15.
Constraints:
1 ≤ n ≤ 104

'''

class Solution:
      def sumOfNNumbers(self,n:int)->int:
          return n*((n+1))//2
          
class Solution:
    def sumOfNNumbers(self,n:int)->int:
        return self.helper(n,1,0)
    def helper(self,n:int,value:int,sum:int)->int:
        if value==n+1:
            return sum 
        return self.helper(n,value+1,sum+value)
        
# backtracking
class Solution:
    def sumOfNNumbers(self,n:int)->int:
        return self.helper(n,0)

    def helper(self,n:int,sum:int)->int:
        if n==0:
            return sum 
        return self.helper(n-1,sum+n)
         
class Solution:
    def sumOfNNumbers(self,n:int)->int:
        return self.helper(n)

    def helper(self,n:int)->int:
        if n==0:
            return 0 
        return n+self.helper(n-1)
        
          
class TestApp:
      def testCaseOne(self):
          assert Solution().sumOfNNumbers(30)==465
      def testCaseTwo(self):
          assert Solution().sumOfNNumbers(5)==15