class PrintUtil:

    @staticmethod
    def print_list(head):
        curr = head
        while curr is not None:
            print(curr.val)
            curr = curr.next