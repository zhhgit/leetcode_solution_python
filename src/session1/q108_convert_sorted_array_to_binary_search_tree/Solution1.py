from src.session1.common.TreeNode import TreeNode

class Solution1:
    def sortedArrayToBST(self, nums):
        arrLen = len(nums)
        return self.buildTreeWithRange(nums,0,arrLen-1)

    def buildTreeWithRange(self,nums,start,end):
        arrLen = len(nums)
        if start > end or start < 0 or start >= arrLen or end < 0 or end >= arrLen:
            return None
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = self.buildTreeWithRange(nums,start,mid - 1)
        root.right = self.buildTreeWithRange(nums,mid + 1,end)
        return root

s = Solution1()
arr = [1,2,3,4,5,6,7]
root = s.sortedArrayToBST(arr)
print("finish")


