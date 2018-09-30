from src.session1.common.ListBuilder import ListBuilder
from src.session1.common.ListNode import ListNode
from src.session1.common.PrintUtil import PrintUtil

class Solution1:
    def deleteDuplicates(self, head):
        if (head is None) or (head.next is None):
            return head
        map = {}
        fakeHead = ListNode(0)
        fakeHead.next = head
        curr = fakeHead
        while curr.next is not None:
            if curr.next.val not in map:
                map[curr.next.val] = 1
                curr = curr.next
            else:
                keep = curr.next.next
                curr.next = keep
        return fakeHead.next

s = Solution1()
arr = [1,1]
listBuilder = ListBuilder(arr)
head = listBuilder.get_head()
PrintUtil.print_list(s.deleteDuplicates(head))

