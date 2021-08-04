import numpy as np
import random




'''
6. 背包具有价值和重量，如何选择背包使得满足重量不超的情况下价值最大
'''
def most_value_of_bags(bags_list, index, cur_weight, max_weight, cur_value, max_value):
    # 传入当前选择的总价值、总重量和全局总重量阈值，每次更新全局最大价值
    if index==len(bags_list):
        return max(max_value, cur_value)
    max_value = most_value_of_bags(bags_list, index+1, cur_weight, max_weight, cur_value, max_value)
    cur_weight = bags_list[index].weight + cur_weight
    cur_value = bags_list[index].value + cur_value
    if cur_weight<=max_weight:
        max_value = most_value_of_bags(bags_list, index+1, cur_weight, max_weight, cur_value, max_value)
    return max_value

def get_most_value_of_bags(bags_list, max_weight):
    return most_value_of_bags(bags_list, 0, 0, max_weight, 0, -float('inf'))

def most_value_of_bags_2(bags_list, index, cur_weight, max_weight):
    # 传入当前选择的总重量和全局总重量阈值，返回当前节点及后面的最大价值
    if index==len(bags_list):
        return 0
    v1 = most_value_of_bags_2(bags_list, index+1, cur_weight, max_weight)
    cur_weight = cur_weight + bags_list[index].weight
    if cur_weight<=max_weight:
        v2 = bags_list[index].value + most_value_of_bags_2(bags_list, index+1, cur_weight, max_weight)
        return max(v1, v2)
    else:
        return v1
    

def get_most_value_of_bags_2(bags_list, max_weight):
    return most_value_of_bags_2(bags_list, 0, 0, max_weight)


def most_value_of_bags_3(weights, values, rest_weight, index):
    if index==len(weights):
        return 0
    v1 = most_value_of_bags_3(weights, values, rest_weight, index+1)
    if weights[index]<=rest_weight:
        v2 = values[index]+most_value_of_bags_3(weights, values, rest_weight-weights[index], index+1)
        v1 = max(v1, v2)
    return v1

def get_most_value_of_bags_3(weights, values, max_weight):
    return most_value_of_bags_3(weights, values, max_weight, 0)

def get_most_value_of_bags_dp(weights, values, max_weight):
    dp = np.array([0]*(len(weights)*(max_weight+1))).reshape(len(weights), max_weight+1)
    for index in range(max_weight+1-weights[-1]):
        dp[len(weights)-1][index] = values[-1]
    for index in range(len(weights)-2, -1, -1):
        for i in range(max_weight+1):
            if i+weights[index]<=max_weight:
                dp[index][i] = max(dp[index+1][i], values[index]+dp[index+1][i+weights[index]])
            else:
                dp[index][i] = dp[index+1][i]
    return dp[0][0]

def get_most_value_of_bags_dp_rest(weights, values, max_weight):
    dp = np.array([0]*(len(weights)*(max_weight+1))).reshape(len(weights), max_weight+1)
    for rest in range(weights[-1], max_weight+1):
        dp[-1][rest] = values[-1]
    for index in range(len(weights)-2, -1, -1):
        for rest in range(max_weight+1):
            dp[index][rest] = dp[index+1][rest]
            if weights[index]<=rest:
                dp[index][rest] = max(dp[index+1][rest], values[index]+dp[index+1][rest-weights[index]])
    return dp[0][max_weight]


'''
        cur_weight
index   
        0   1   2   3
0       19  19  0   0
1       2   0   0   0
2       1   1   0   0
3       0   0   0   0
4       0   0   0   0

        cur_weight
index   
        0            1           2           3         4           5         6       7
0       0            0           0           0         0           0         0       0
1       0            0           0           0         2           0         0       0
2       4            2           max()           max(0,c+0)max(0,c+0)  max(0,c+0)0       0
3       max(e, d+0)  max(e,d+0)  max(e,d+0)  0         0           0         0       0
4       e            e           e           0         0           0         0       0
'''

class Bag:
    def __init__(self, weight, value) -> None:
        self.weight = weight
        self.value = value

def get_most_value_of_bags_test():
    weights = [6, 4, 9, 2, 5]
    values = [10, 2, 8, 7, 1]
    bags_list = [Bag(i, j) for i, j in zip(weights, values)]
    print(get_most_value_of_bags(bags_list, 7))
    print(get_most_value_of_bags_2(bags_list, 7))
    print(get_most_value_of_bags_3(weights, values, 7))
    print(get_most_value_of_bags_dp(weights, values, 7))
    print(get_most_value_of_bags_dp_rest(weights, values, 7))

def get_most_value_of_bags_random_test():
    error = 0
    for _ in range(100):
        weights = [random.randint(1,10) for _ in range(5)]
        values = [random.randint(1,10) for _ in range(5)]
        max_weight = random.randint(5,30)
        bags_list = [Bag(i, j) for i, j in zip(weights, values)]
        if get_most_value_of_bags(bags_list, max_weight)!=get_most_value_of_bags_dp_rest(weights, values, max_weight):
            error += 1
            print(weights, values, max_weight)
    print('error: {}'.format(error))


if __name__ == '__main__':

    # get_most_value_of_bags_test()
    get_most_value_of_bags_random_test()

