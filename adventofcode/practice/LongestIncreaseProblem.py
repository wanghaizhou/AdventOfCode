# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

# 输入：nums = [0,1,0,3,2,3]
# 输出：4


def calculate(nums):
    dp = [0]*len(nums)
    dp[0] = 1
    for i in range(1,len(nums)):
        # max(dp)+1,
        # for j in range(i):

        list = [0]
        for j in range(0,i):
            if nums[j] < nums[i]:
                list.append(dp[j])
        dp[i] =  max(list)+1
        pass

    print(dp)
    return max(dp)
    pass

# lenth = calculate([10,9,2,5,3,7,101,18])
lenth = calculate([2,3,7,101])
print('lenth',lenth)