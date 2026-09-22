class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        l=0
        r=1
        maxp=0
        while(r <len(arr)):
            if arr[l]<arr[r]:
                profit=arr[r]-arr[l]
                maxp=max(maxp,profit)
            else:
                l=r
            r+=1
        return maxp