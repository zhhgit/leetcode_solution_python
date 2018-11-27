1.range()，创建一个整数列表，一般用在for循环中

2.len()，返回对象（字符、列表、元组等）长度或项目个数

3.if True:
    do something
  else:
    do something

4. key in dict，返回True或者False

5.面向对象：s = Solution()

6.print(list)

7.函数
def funcName(self,param1,param2):
    do something
    return something

8.字典dict[key] = value

9.@staticmethod：类方法，方法参数中没有self

10.与或非： and or not

11.from src.session1.common.PrintUtil import PrintUtil

12.函数尽量用下划线命名的方式：def some_method(self)

13.类中的某个方法调用其他方法：self.another_method()

14.is None, is not None 返回True或者False

15.while condition :
    do something

16.取整 //,取余 %

17.类的私有属性：self.__attr

18.数字次方，2**31

19.数字数组遍历
    for i in arr
        print(i)

20.for i in range(0,len(nums)):
    do_something(nums[i])

21.if condition1:
    do something1
  elif condition2:
    do something2
  else:
    do something3

22.字符串str中某一位str[i],字符创中截取某一段str[i:j]

23.字符串比较 s1 == s2,s1 != s2

24.最大、最小值函数max(),min()

25.arr.append(i)，数组末尾添加元素

26.数字转字符串str("123")，字符串转数字int("9")

27.字符串拼接 str1 + str2

28.倒序遍历for i in range(len(arr) - 1,-1,-1)，range()函数返回的不是数组，而是一个整数序列的对象

29.反转数组list.reverse(),该方法没有返回值，需要注意

30.输出不换行print("something",end=' '),自定义输出末尾是什么

31.构造函数
    def __init__(self, x):
        self.val = x
        self.next = None

32.队列，from collections import deque，有append(),popleft()方法

33.str.lower(),str.uppper()转化字符串为小写、大写字母

34.str.strip(), str.lstrip(), str.rstrip()去除两侧、左侧、右侧空格

35.str.isspace()是否为空字符串，str.isalpha()是否为字母，str.isdigit()是否为数字