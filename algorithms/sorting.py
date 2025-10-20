from typing import *

class Solution:
    def bubbleSort(self, arr:List[int]):
        for n in range(len(arr)-1,0,-1):
            for i in range(n):
                if arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]

    def selectionSort(self, arr:List[int]):
        for i in range(len(arr)-1):
            indexMin = i
            for j in range(i+1,len(arr)):
                if arr[j] < arr[indexMin]:
                    indexMin = j
            if arr[i] > arr[indexMin]:
                arr[i],arr[indexMin] = arr[indexMin],arr[i]

    def insertionSort(self, arr:List[int]):
        for i in range(len(arr)):
            for j in range(i,0,-1):
                if arr[j-1] <= arr[j]:
                    break
                else:
                    arr[j],arr[j-1] = arr[j-1],arr[j]

    def part(self, arr:List[int], l:int, r:int):
        pivot = arr[r]
        i = l-1
        for j in range(l,r):
            if arr[j] <= pivot:
                i += 1
                arr[i],arr[j] = arr[j],arr[i]
        
        arr[i+1],arr[r] = arr[r],arr[i+1]
        return i+1

    def quickSort(self, arr:List[int], l:int, r:int):
        if l < r:
            mid = self.part(arr,l,r)
            self.quickSort(arr,l,mid-1)
            self.quickSort(arr,mid+1,r)

    def merge(self, arr:List[int], l:int, m:int, r:int):
        n1 = m-l+1
        n2 = r-m
        L = [0]*n1
        R = [0]*n2
        
        for i in range(0,n1):
            L[i] = arr[l+i]
        for i in range(0,n2):
            R[i] = arr[m+1+i]

        i = 0
        j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
    
    def mergeSort(self, arr:List[int], l:int, r:int):
        if l < r:
            m = (l+r)//2
            self.mergeSort(arr,l,m)
            self.mergeSort(arr,m+1,r)
            self.merge(arr,l,m,r)

    def heapify(self, arr:List[int], n:int, i:int):
        largest = i
        l = 2*i+1
        r = 2*i+2

        if l<n and arr[i]<arr[l]:
            largest = l

        if r<n and arr[largest]<arr[r]:
            largest = r
        
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
        
            self.heapify(arr,n,largest)

    def heapSort(self, arr:List[int]):
        n = len(arr)
        for i in range(n//2,-1,-1):
            self.heapify(arr,n,i)
        for i in range(n-1,0,-1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr,i,0)

arr = [9,-3,5,2,6,8,-6,1,3]
sol = Solution()
print("hwello")
#sol.mergeSort(arr,0,len(arr)-1)
sol.heapSort(arr)
#sol.bubbleSort(arr)
print(arr)