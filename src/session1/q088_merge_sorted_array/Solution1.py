class Solution1:
    def merge(self, nums1, m, nums2, n):
        temp = []
        i = 0
        j = 0
        while i < m and j < n:
            if (nums1[i] <= nums2[j]):
                temp.append(nums1[i])
                i = i + 1
            else:
                temp.append(nums2[j])
                j = j + 1
        if i == m:
            while j < n:
                temp.append(nums2[j])
                j = j + 1
        elif j == n:
            while i < m:
                temp.append(nums1[i])
                i = i + 1
        for i in range(0,m + n):
            nums1[i] = temp[i]

s = Solution1()
nums1 = [1]
nums2 = []
m = 1
n = 0
s.merge(nums1,m,nums2,n)
print(nums1)