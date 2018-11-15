from src.session1.common.TreeBuilder import TreeBuilder
from collections import deque

class Solution1:
    def levelOrderBottom(self, root):
        lists = []
        queue = deque()
        if root is None:
            return lists
        queue.append(root)
        while(len(queue) > 0):
            size = len(queue)
            addList = []
            for i in range(0,size):
                curr = queue.popleft()
                addList.append(curr.val)
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)
            lists.append(addList)
        return self.reverseList(lists)

    def reverseList(self,lists):
        # ret = []
        # for i in range(len(lists) - 1,-1,-1):
        #     ret.append(lists[i])
        # return ret
        lists.reverse()
        return lists

s = Solution1()
arr = [1,2,3,4,5,6]
treeBuilder = TreeBuilder(arr)
lists = s.levelOrderBottom(treeBuilder.get_root())
print(lists)