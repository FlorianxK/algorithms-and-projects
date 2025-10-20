from typing import *

class Solution:
    def part(self, arr:List[int], l:int, r:int):
        x = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[r] = arr[r], arr[i]
        return i

    def quickselect(self, arr:List[int], l:int, r:int, k:int):
        if (k > 0 and k <= r-l+1):
            index = self.part(arr,l,r)
            
            if (index-l == k-1):
                return arr[index]

            if (index-l > k-1):
                return self.quickselect(arr,l,index-1,k)
            
            return self.quickselect(arr,index+1,r,k-index+l-1)

    def get_median(self, group:List[int]) -> int:
        group.sort()
        return group[len(group)//2]

    def part_Pivot(self, arr:List[int], l:int, r:int, x:int):
        for i in range(l, r):
            if arr[i] == x:
                break
        arr[i], arr[r] = arr[r], arr[i]
    
        i = l
        for j in range(l, r):
            if arr[j] <= x:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                
        arr[i], arr[r] = arr[r], arr[i]
        return i
    
    def selectKthSmallest(self, arr:List[int], l:int, r:int, k:int):
        if k > 0 and k <= r-l+1:
            n = r-l+1
            medians = []

            i = 0
            while i < n//5:
                group = arr[l+i*5: l+i*5+5]
                medians.append(self.get_median(group))
                i += 1

            if i*5 < n:
                lastGroup = arr[l+i*5: l+i*5+(n%5)]
                medians.append(self.get_median(lastGroup))

            if len(medians) == 1:
                pivot = medians[0]
            else:
                pivot = self.selectKthSmallest(medians, 0, len(medians)-1, len(medians)//2 +1)

            pos = self.part_Pivot(arr, l, r, pivot)

            if pos-l == k-1:
                return arr[pos]
            
            if pos-l > k-1:
                return self.selectKthSmallest(arr, l, pos-1, k)

            return self.selectKthSmallest(arr, pos+1, r, k-pos+l-1)
        return float('inf')

    def median_of_medians(self, arr: List[int], k:int):
        return self.selectKthSmallest(arr,0,len(arr)-1,k)

arr = [7,10,4,3,20,15]
k = 3
sol = Solution()
print("hwello")
#res = sol.quickselect(arr,0,len(arr)-1,k)
res = sol.median_of_medians(arr,k)
print(arr)
print(res)