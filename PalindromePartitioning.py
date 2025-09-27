'''

Given a string s, partition s such that every substring of the 

partition is a palindrome. Return all possible palindrome partitioning of s.


Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''
class Solution:
      def partition(self, s: str) -> list[list[str]]:
          result=[]
          self.helper(s,0,len(s),[],result)
          return result
          
      def helper(self,string:str,index:int,n:int,subset:list[int],result:list[list[str]]):
          if index>=n:
             result.append(subset[::])
             return 
          for i in range(index,n):
              if(self.isPalindrome(index,i,string)):
                  subset.append(string[index:i+1])
                  self.helper(string,i+1,n,subset,result)
                  subset.pop()

      def isPalindrome(self,start:int,end:int,string:str):
          while start<=end:
                if string[start]!=string[end]:
                    return False 
                start+=1
                end-=1
          return True
          
class TestApp:
      def testCaseOne(self):
          assert Solution().partition("aab")==[["a","a","b"],["aa","b"]]
      def testCaseTwo(self):
          assert Solution().partition("a")==[["a"]]