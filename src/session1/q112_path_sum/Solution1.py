from src.session1.common.TreeBuilder import TreeBuilder

class Solution1:
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return sum == root.val
        if root.left is None and root.right is not None:
            return self.hasPathSum(root.right,sum - root.val)
        if root.left is not None and root.right is None:
            return self.hasPathSum(root.left,sum - root.val)
        else:
            return self.hasPathSum(root.right,sum - root.val) or self.hasPathSum(root.left,sum - root.val)

s = Solution1()
arr = [1,2,3,4]
targets = [4,7,8]
treeBuilder = TreeBuilder(arr)
for i in targets:
    print(s.hasPathSum(treeBuilder.get_root(),i))
