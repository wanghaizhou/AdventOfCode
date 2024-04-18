# https://leetcode.cn/problems/assign-cookies/description/

# 示例 1：
#
# 输入：g = [1,2,3], s = [1,1]
# 输出：1
# 解释：你有三个孩子和两块小饼干，3 个孩子的胃口值分别是：1, 2, 3。虽然你有两块小饼干，由于他们的尺寸都是 1，你只能让胃口值是 1 的孩子满足。所以应该输出 1。
# 示例 2：
#
# 输入: g = [1,2], s = [1,2,3]
# 输出: 2
# 解释: 你有两个孩子和三块小饼干，2个孩子的胃口值分别是1, 2。你拥有的饼干数量和尺寸都足以让所有孩子满足。所以你应该输出 2。


def calculate(g, s):
    g.sort()
    s.sort()
    matchL = []
    index = 0
    for i in range(len(g)):
        if index<=len(s)-1:
            for j in range(index,len(s)):
                if s[index] >= g[i]:
                    matchL.append(s[index])
                    index = index+1
                    break
                    pass
                index = index+1
        else:
            break
    return matchL
    pass

# g = [10,9,8,7]
# s = [5,6,7,8]

g = [1,2,3]
s = [3]


t = calculate(g,s)
print('t',t)

