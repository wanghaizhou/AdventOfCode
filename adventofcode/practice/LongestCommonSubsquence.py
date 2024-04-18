# 示例：
#
# 示例 1：
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace"，它的长度为 3。
# 示例 2：
#
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。

#  s1[i]=s2[j] 时   arr[i][j] = arr[i-1][j-1]+1
#  s1[i]!=s2[j] 时   arr[i][j] = max(arr[i][j-1],arr[i-1][j])
#  初始状态

def calculate(s1, s2):

    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i:i+1] == s2[j:j+1]:
                dp[i+1][j+1] = dp[i][j]+1
                pass
            else:
                dp[i+1][j+1] = max([dp[i][j+1],dp[i+1][j]])
                pass
    return dp[len(s1)][len(s2)]
    pass

def calculate2(s1, s2):
    pass


v = calculate('abcde','ace')
print('v',v)

v = calculate2('abcde','ace')
print('v2',v)



