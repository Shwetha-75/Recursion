# Sort the array - Merge Sort 

class Solution:
      def mergeSort(self,nums:list[int]):
          return self.divide(nums)
      def divide(self,nums:list[int]):
          if len(nums)==1:
              return nums 
          length=len(nums)
          mid=length//2
          left=self.divide(nums[:mid])
          right=self.divide(nums[mid:length])
          return self.conquer(left,right)
      def conquer(self,nums_1:list[int],nums_2:list[int]):
          result=[]
          n1,n2=len(nums_1),len(nums_2)
          i=j=0 
          while i<n1 and j<n2:
                if nums_1[i]<nums_2[j]:
                    result.append(nums_1[i])
                    i+=1
                else:
                    result.append(nums_2[j])
                    j+=1
          while i<n1:
               result.append(nums_1[i])
               i+=1
          while j<n2:
              result.append(nums_2[j])
              j+=1
          return result


class TestApp:
      def testCaseOne(self):
          assert Solution().mergeSort([4, 1, 3, 9, 7])==[1,3,4,7,9]
              
       
          