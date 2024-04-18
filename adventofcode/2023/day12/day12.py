 # https://juejin.cn/post/6951922898638471181

 # 3    2 1
 # ##.##.#
 # ?###????????
 # ?????????????
 # ??.??????????
 # ??#??????????
from functools import cache


@cache
def deal(string, nums):
    if not nums:
        return '#' not in string
    result = 0
    current, nums = nums[0], nums[1:]
    l = len(string)-(sum(nums)+len(nums)-1)-current
    for i in range(l):
        pre = string[:i]
        if '#' in pre:
            break
        index = i+current
        assumedNode = string[i:index]
        suffix = string[index:index+1]
        # if (index<=len(string) and '.' not in assumedNode and '#' not in suffix):
        if (index<=len(string) and '.' not in assumedNode and '#' not in suffix):
            result += deal(string[index+1:],nums)
    return result


with open('input.txt', 'r') as file:
    content = [line.split() for line in file.readlines()]
    p1 = 0
    p2 = 0
    for l in content:
        springs = tuple(map(int, l[1].split(',')))
        p1 += deal(l[0], springs)
        p2 += deal("?".join([l[0]] * 5), springs * 5)
    print('p1',p1)
    print('p2',p2)