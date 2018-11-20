from src.session1.common.TreeBuilder import TreeBuilder

class Solution1:
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)
        if root.left is not None and root.right is None:
            return 1 + self.minDepth(root.left)
        if root.left is not None and root.right is not None:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        else:
            return 1

s = Solution1()
arr = [1,2,3,4]
treeBuilder = TreeBuilder(arr)
print(s.minDepth(treeBuilder.get_root()))


