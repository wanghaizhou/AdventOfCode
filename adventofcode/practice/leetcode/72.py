# https://leetcode.cn/problems/edit-distance/description/
# 描述：给定两个单词 word1word1word1、word2word2word2。
#
# 对一个单词可以进行以下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
# 要求：计算出将 word1word1word1 转换为 word2word2word2 所使用的最少操作数。
#
# 说明：
#
# 0≤word1.length,word2.length≤5000 \le word1.length, word2.length \le 5000≤word1.length,word2.length≤500。
# word1word1word1 和 word2word2word2 由小写英文字母组成。
# 示例：
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#     a 1 b 2 c 3 a b c 1
# a   0 1 2 3 4 5 6 7 8 9
# b   1 1 1 2 3 4 5 6 7 8
# c   2 2 2

def calculate(word1, word2):
    dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
    for i in range(len(word1)+1):
        dp[i][0] = i
    for j in range(len(word2)+1):
        dp[0][j] = j

    for i in range(1,len(word1)+1):
        for j in range(1,len(word2)+1):
            if word1[i-1:i] == word2[j-1:j]:
                dp[i][j] = dp[i-1][j-1]
                pass
            else:
                dp[i][j] = min([dp[i-1][j],dp[i][j-1],dp[i-1][j-1]])+1
                pass
            pass
    pass
    # 输出二维数组
    for row in dp:
        for value in row:
            print(value, end=" ")
        print()
    return dp[len(word1)][len(word2)]


# val = calculate(word1 = "intention", word2 = "execution")
val = calculate(word1 = "horse", word2 = "ros")
print('val',val)

