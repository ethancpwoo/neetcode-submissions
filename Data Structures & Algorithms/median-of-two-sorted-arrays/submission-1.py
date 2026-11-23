class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # l1, r1 = 0, len(nums1)-1
        # l2, r2 = 0, len(nums2)-1
        # while l1+1 < r1 or l2+1 < r2:
        #     m1 = (l1+r1)//2
        #     m2 = (l2+r2)//2
        #     if m1 <= m2:
        #         l2 = m2
        #         r1 = m1
        #     else: 
        #         l1 = m1
        #         r2 = m2
        # 
        # # theoretically should end up with arrays of (2,) and (2,) max
        # print(max(nums1[l1], nums2[l2]))
        # print(min(nums1[r1], nums2[r2]))
        # median = (max(nums1[l1], nums2[l2]) + min(nums1[r1], nums2[r2]))/2
        # return median

        # num of elements in left half of sorted array
        half = (len(nums1) + len(nums2)+1)//2
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        lo, hi = 0, len(nums1)

        while lo <= hi: 
            i = (hi+lo)//2 
            j = half - i
            l1 = nums1[i - 1] if i > 0 else float("-inf")
            r1 = nums1[i] if i < len(nums1) else float("inf")
            l2 = nums2[j - 1] if j > 0 else float("-inf")
            r2 = nums2[j] if j < len(nums2) else float("inf")
            
            if l1 > r2:
                hi = i-1
            elif l2 > r1:
                lo = i+1
            else:
                break
        
        if (len(nums1) + len(nums2)) % 2 == 0: 
            return (max(l1, l2) + min(r1, r2)) / 2
        else:
            return float(max(l1, l2))
            
            

