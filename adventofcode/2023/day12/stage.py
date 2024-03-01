
import time

# no suggest,when the num is big, it can't work out.
def maxStepByRecurse(num):
    if num == 1:
        return 1
    if  num == 2:
        return 2
    return maxStepByRecurse(num-1)+maxStepByRecurse(num-2)

# dynamic programming
def maxStep(num):
    if num == 1:
        return 1
    if  num == 2:
        return 2

    dp = [0]*num
    dp[0] = 1
    dp[1] = 2
    for i in range(2,num):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[num-1]

start_time = time.time()
# print(maxStepByRecurse(30))
print(maxStep(30))
end_time = time.time()
execution_time = end_time - start_time
print("code cost time: {} s".format(execution_time))
