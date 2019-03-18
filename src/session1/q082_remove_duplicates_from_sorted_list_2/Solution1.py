from src.session1.common.ListBuilder import ListBuilder
from src.session1.common.PrintUtil import PrintUtil
from src.session1.common.ListNode import ListNode

class Solution1:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        fakeHead = ListNode(0)
        fakeHead.next = head
        curr = fakeHead
        while curr.next is not None:
            nextNode = curr.next
            if nextNode.next is not None and nextNode.next.val == nextNode.val:
                while nextNode.next is not None and nextNode.next.val == nextNode.val:
                    nextNode = nextNode.next
                curr.next = nextNode.next
            else:
                curr = curr.next
        return fakeHead.next

s = Solution1()
arrs = [[1,2,3,3,4,4,5],[1,1,1,2,3]]
for i in range(0,len(arrs)):
    listBuilder = ListBuilder(arrs[i])
    PrintUtil.print_list(listBuilder.get_head())
    print("----------------------")
    PrintUtil.print_list(s.deleteDuplicates(listBuilder.get_head()))
    print("----------------------")