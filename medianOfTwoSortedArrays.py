class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m= len(nums1)
        n= len(nums2)
        nums3 = [None]*(n+m)
        i=0
        j=0
        k=0
        
        while i<m and j<n:
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                i+=1
                k+=1
            else:
                nums3[k] = nums2[j]
                j+=1
                k+=1
            
        while(i<m):
            nums3[k] = nums1[i]
            i+=1
            k+=1
            
        while(j<n):
            nums3[k] = nums2[j]
            j+=1
            k+=1
      
        if ((m+n) % 2 == 1):
            #print((m+n+1)/2)
            return nums3[int((m+n-1)/2)]
        else:
            #print((m+n)/2)
            return (nums3[int((m+n)/2)] + nums3[(int((m+n)/2) -1)])/2
             
