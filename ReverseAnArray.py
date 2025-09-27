# Reversing an array

# Using Two pointers Approach 
class Solution:
      def reverseAnArray(self,arr:list[int]):
          self.helper(arr,0,len(arr)-1)

      def helper(self,arr:list[int],left:int,right:int)->None:
          if left>=right:
              return 
          arr[left],arr[right]=arr[right],arr[left]
          return self.helper(arr,left+1,right-1)
# Using one single pointers 
class Solution:
      def reverseAnArray(self,arr:list[int]):
          self.helper(0,len(arr),arr)
         
      def helper(self,index:int,n:int,arr):
          if index==n//2:
              return 
          arr[index],arr[n-index-1]=arr[n-index-1],arr[index]
          self.helper(index+1,n,arr)
      
class TestApp:
      def testCaseOne(self):
          arr=[1,2,3,4,5]
          Solution().reverseAnArray(arr) 
          assert arr==[5,4,3,2,1]
      def testCaseTwo(self):
          arr=[40,10,30,88,91]
          Solution().reverseAnArray(arr)  
          assert arr==[91,88,30,10,40]  