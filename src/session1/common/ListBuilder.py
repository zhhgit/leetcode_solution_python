from src.session1.common.ListNode import ListNode


class ListBuilder:
    __head = None
    __tail = None

    def __init__(self, nums):
        for i in range(len(nums)):
            num = nums[i]
            if self.__head is None:
                self.__tail = ListNode(num)
                self.__head = self.__tail
            else:
                self.__tail.next = ListNode(num)
                self.__tail = self.__tail.next

    def get_head(self):
        return self.__head