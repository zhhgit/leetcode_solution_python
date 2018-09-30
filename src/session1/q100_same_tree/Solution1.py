from src.session1.common.TreeBuilder import TreeBuilder

class Solution1:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

s = Solution1()
nums1 = [1,2]
nums2 = [1,2,1]
treeBuilder1 = TreeBuilder(nums1)
treeBuilder2 = TreeBuilder(nums2)
print(s.isSameTree(treeBuilder1.get_root(),treeBuilder2.get_root()))