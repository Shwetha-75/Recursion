class Solution:
      def checkStringPalindrome(self,string:str)->bool:
          return self.helper(0,len(string)-1,string)

      def helper(self,left:int,right:int,string:int)->None:
          if left>=right:
              return True 
          if string[left]!=string[right]:
              return False 
          return self.helper(left+1,right-1,string)
import re      
      
class Solution:
    def checkStringPalindrome(self,string:str)->bool:
        string=re.sub(r"[^a-zA-Z0-9]","",string).lower()
        return self.helper(0,len(string)-1,string)
    def helper(self,left:int,right:int,string:str)->bool:
        if left>=right:
            return True 
        if string[left]!=string[right]:
            return False 
        return self.helper(left+1,right-1,string)
        
class Solution:
    def checkStringPalindrome(self,string:str)->bool:
        string=re.sub(r"[^a-zA-Z0-9]","",string).lower()
        return self.helper(0,len(string),string)
    def helper(self,index:int,n:int,string:str)->bool:
        if index>=n//2:
            return True 
        if string[index]!=string[n-index-1]:
            return False 
        return self.helper(index+1,len(string),string)
               
               
# print(Solution().checkStringPalindrome("apple"))
class TestApp:
      def testCaseOne(self):
          assert Solution().checkStringPalindrome("poop")==True 
      def testCaseTwo(self):
          assert Solution().checkStringPalindrome("apple")==False 
      def testCaseThree(self):
          assert Solution().checkStringPalindrome("lplplplplplpl")==True