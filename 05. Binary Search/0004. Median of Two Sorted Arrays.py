from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search range
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)  # Lengths of the two arrays
        half_len = (m + n + 1) // 2  # Half the combined length, handles both even and odd cases
        low, high = 0, m  # Binary search bounds for nums1

        while low <= high:
            # Binary search on nums1
            i = (low + high) // 2  # Partition index for nums1
            j = half_len - i  # Corresponding partition index for nums2

            # Boundary values for partitions (handling out-of-bound cases)
            nums1_left = nums1[i - 1] if i > 0 else float("-inf")  # Left max of nums1 partition
            nums1_right = nums1[i] if i < m else float("inf")  # Right min of nums1 partition
            nums2_left = nums2[j - 1] if j > 0 else float("-inf")  # Left max of nums2 partition
            nums2_right = nums2[j] if j < n else float("inf")  # Right min of nums2 partition

            # Check if partitions are correct (i.e., left max <= right min on both sides)
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # If total length is odd, return max of left halves as the median
                if (m + n) % 2 == 1:
                    return max(nums1_left, nums2_left)
                # If total length is even, return the average of max of left halves and min of right halves
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

            # Adjust binary search range if partitions are not correct
            elif nums1_left > nums2_right:
                high = i - 1  # Move search to the left (reduce i)
            else:
                low = i + 1  # Move search to the right (increase i)
