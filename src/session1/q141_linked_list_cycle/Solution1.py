from src.session1.common.ListBuilder import ListBuilder

class Solution1:
    def hasCycle(self, head):
        if head is None:
            return False
        fast = head
        slow = head
        while slow.next is not None and fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

s = Solution1()
arr = [1,2,3,4]
listBuilder = ListBuilder(arr)
print(s.hasCycle(listBuilder.get_head()))


