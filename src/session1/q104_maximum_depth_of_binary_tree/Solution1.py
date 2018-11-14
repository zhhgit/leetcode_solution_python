from src.session1.common.TreeBuilder import TreeBuilder

class Solution1:
    def maxDepth(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1

s = Solution1()
arr = [1,2,3]
treeBuilder = TreeBuilder(arr)
print(s.maxDepth(treeBuilder.get_root()))
