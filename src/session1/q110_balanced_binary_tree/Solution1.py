from src.session1.common.TreeBuilder import TreeBuilder

class Solution1:
    def isBalanced(self, root):
        if root is None:
            return True
        return abs(self.getTreeDepth(root.left) - self.getTreeDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getTreeDepth(self,root):
        if root is None:
            return 0
        return max(self.getTreeDepth(root.left),self.getTreeDepth(root.right)) + 1

s = Solution1()
arr = [1,2,3,4]
treeBuilder = TreeBuilder(arr)
print(s.isBalanced(treeBuilder.get_root()))