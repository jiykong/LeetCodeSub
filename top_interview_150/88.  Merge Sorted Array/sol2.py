class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        write_index = m + n -1
        
        endof1 = m -1
        endof2 = n -1

        while endof2 >= 0:
            if endof1 >=0 and nums1[endof1] > nums2[endof2]:
                nums1[write_index] = nums1[endof1]
                endof1-=1
            else:
                nums1[write_index] = nums2[endof2]
                endof2-=1


            write_index-=1
