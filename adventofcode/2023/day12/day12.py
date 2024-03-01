 # https://juejin.cn/post/6951922898638471181


with open('input_test','r') as file:
    content = file.readlines()


def deal(nodeneedtobefilled, node_num):
    nodeneedtobefilled
    pass


for line in content:
    arr = line.split(' ')
    length = len(arr[0])
    nums = arr[1].split(',')
    # max_i = max(nums)
    nodeneedtobefilled = length - sum(nums) - len(nums) + 1
    deal(nodeneedtobefilled,len(nums)+1)

