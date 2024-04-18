# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/
# 描述：给定两个整数数组 nums1nums1nums1、nums2nums2nums2。
#
# 要求：计算两个数组中公共的、长度最长的子数组长度。
#
# 说明：
#
# 1≤nums1.length,nums2.length≤10001 \le nums1.length, nums2.length \le 10001≤nums1.length,nums2.length≤1000。
# 0≤nums1[i],nums2[i]≤1000 \le nums1[i], nums2[i] \le 1000≤nums1[i],nums2[i]≤100。
# 示例：
#
# 示例 1：
#
# 输入：nums1 = [1,2,3,2,1,2], nums2 = [3,2,1,4,7]
# 输出：3
# 解释：长度最长的公共子数组是 [3,2,1] 。
# 示例 2：
#
# 输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# 输出：5

def calculate(nums1, nums2):
    dp = [ [0 for _ in range(len(nums1)+1)] for _ in range(len(nums2)+1)]

    v = 0
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if nums1[i] == nums2[j]:
                dp[j+1][i+1] = dp[j][i]+1
                v = max([dp[j+1][i+1],v])
            else:
                dp[j+1][i+1] = 0
    return v
    pass


print('v',calculate([1,2,3,2,1,2],[3,2,1,4,7]))
