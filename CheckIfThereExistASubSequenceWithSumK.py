class Solution:
      def checkSubsequenceSum(self, N:int, arr:list[int], K:int):
          total_sum=sum(arr)
          if total_sum<K:
              return "No"
          return "Yes" if self.helper(0,len(arr),arr,K,[],0) else "No"
      def helper(self,index:int,n:int,nums:list[int],k:int,subset:list,sum:int)->bool:
          if index>=n:
              return True if sum==k else False 
          subset.append(nums[index])
          sum+=nums[index]
          if self.helper(index+1,n,nums,k,subset,sum) : return True
          subset.pop()
          sum-=nums[index]
          if self.helper(index+1,n,nums,k,subset,sum) : return True 
          return False  
Solution().checkSubsequenceSum(6,[2,3,4,5,7,9],100)        