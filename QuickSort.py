# sort the array - Quick Sort Technique

class Solution:
    def quickSort(self,nums:list[int]):
        self.quickSortingDivide(nums,0,len(nums)-1)
        return nums
    def quickSortingDivide(self,arr:list[int],low:int=None,high:int=None):
        
        
        if low<high:
            pivotIndex=self.findPivotIndex(low,high,arr) 
            self.quickSortingDivide(arr,low,pivotIndex-1)
            self.quickSortingDivide(arr,pivotIndex+1,high)
    def findPivotIndex(self,low:int,high:int,arr:list[int]):
        pivot=arr[low]
        i,j=low,high 
        while i<j:
              while i<=high and arr[i]<=pivot:
                     i+=1
             
              while j>=low and arr[j]>pivot:
                     j-=1
              if i<j:
                  arr[i],arr[j]=arr[j],arr[i]

        arr[low],arr[j]=arr[j],arr[low]
        
        return j 
   
class TestApp:
      def testCaseOne(self):
          assert Solution().quickSort([5,2,3,1])==[1,2,3,5]
      def testCaseTwo(self):
          assert Solution().quickSort([5,1,1,2,0,0])==[0,0,1,1,2,5]    
      def testCaseThree(self):
          assert Solution().quickSort([3,-1])==[-1,3]
