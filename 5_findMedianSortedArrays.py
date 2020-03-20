class Solution:
    def findMedianSortedArrays_1(self, nums1, nums2) -> float:
        nums = nums1 + nums2
        nums.sort()
        length = len(nums)
        if length % 2 == 0:
            return (nums[length // 2 - 1] + nums[length // 2])/2
        return nums[length // 2]


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    test = Solution()
    result = test.findMedianSortedArrays_1(nums1, nums2)
    print(result)
