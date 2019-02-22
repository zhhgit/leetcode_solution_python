二分查找，外层分为三种情况：
1.左侧单调增，转轴在右侧，nums[mid] > nums[right]；
2.右侧单调增，转轴在左侧，nums[mid] < nums[right]；
3.其他，其实就是nums[mid] == nums[right]

内层：
1、2两种情况，分别在单调增的一侧判断target是否在其中。
3的情况，因为target不与nums[mid]相等，所以也不与nums[right]相等，right减1。