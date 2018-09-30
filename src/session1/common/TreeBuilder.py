from src.session1.common.TreeNode import TreeNode

class TreeBuilder:

    __list = None

    def __init__(self, nums):
        self.__list = []
        for i in range(0,len(nums)):
            self.__list.append(TreeNode(nums[i]))

        lastIndex = len(nums) // 2 - 1
        for i in range(0,lastIndex + 1):
            # 左右节点都有
            if i != lastIndex:
                self.__list[i].left = self.__list[i * 2 + 1]
                self.__list[i].right = self.__list[i * 2 + 2]
            else:
                self.__list[i].left = self.__list[i * 2 + 1]
                if (len(nums) % 2 == 1):
                    self.__list[i].right = self.__list[i * 2 + 2]

    def get_root(self):
        return self.__list[0]