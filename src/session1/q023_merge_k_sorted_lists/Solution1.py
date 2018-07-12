from src.session1.common.ListBuilder import ListBuilder
from src.session1.common.PrintUtil import PrintUtil
from src.session1.common.ListNode import ListNode


class Solution1:
    def mergeKLists(self, lists):
        fakeNode = ListNode(0)
        self.backTracking(lists,fakeNode)
        return fakeNode.next

    def backTracking(self,lists,curr):
        if not self.allEmpty(lists):
            minIndex = -1
            minNode = None
            for i in range(0,len(lists)):
                if lists[i] is not None:
                    if minNode is None:
                        minIndex = i
                        minNode = lists[i]
                    else:
                        minIndex = i if lists[i].val < minNode.val else minIndex
                        minNode = lists[i] if lists[i].val < minNode.val else minNode
            keep = minNode.next
            lists[minIndex] = keep
            minNode.next = None
            curr.next = minNode
            self.backTracking(lists,curr.next)

    def allEmpty(self,lists):
        for i in range(0,len(lists)):
            if lists[i] is not None:
                return False
        return True


s = Solution1()
numsArr = [[1,4,5],[1,3,4],[2,6]]
lists = []
for nums in numsArr:
    listBuilder = ListBuilder(nums)
    lists.append(listBuilder.get_head())
PrintUtil.print_list(s.mergeKLists(lists))