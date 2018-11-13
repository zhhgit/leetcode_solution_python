from src.session1.common.TreeBuilder import TreeBuilder

class Solution1:
    def isSymmetric(self, root):
        if root is None:
            return True
        if root.left is None and root.right is None:
            return True
        return self.isMirror(root.left,root.right)

    def isMirror(self,root1,root2):
        if root1 is None and root2 is not None:
            return False
        if root1 is not None and root2 is None:
            return False
        if root1 is None and root2 is None:
            return True
        return self.isMirror(root1.left,root2.right) and self.isMirror(root1.right,root2.left) and root1.val == root2.val

s = Solution1()
arr1 = [1,2,3]
treeBuilder1 = TreeBuilder(arr1)
print(s.isSymmetric(treeBuilder1.get_root()))