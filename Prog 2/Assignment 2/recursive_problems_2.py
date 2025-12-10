import numpy as np

def move_max_rec(arr: np.ndarray[int]) -> np.ndarray[int]:
    if len(arr) <= 1:
        return arr
    if arr[0] > arr[1]:
        return np.concatenate((arr[1:2], move_max_rec(np.concatenate((arr[0:1], arr[2:])))))
    else:
        return np.concatenate((arr[0:1], move_max_rec(arr[1:])))


def is_substring(big_string: str, sub_string: str) -> bool:
    if len(big_string) < len(sub_string) or not len(big_string) :
        return False
    i = 0
    for i in range(0,len(big_string)):
        if i == len(sub_string):
            return True
        if big_string[i] != sub_string[i]:
            return is_substring(big_string[i + 1:], sub_string)
        i = i + 1
    return False


def find_combinations(input: list, target: int) -> int:
    if target == 0:
        return 1
    elif target < 0 or not len(input):
        return 0
    branch_1 = find_combinations(input[1:], target - input[0])
    branch_2 = find_combinations(input[1:], target)
    return branch_1 + branch_2


def sort_array(arr: np.ndarray[int]) -> np.ndarray[int]:
    if len(arr) == 1:
        return arr
    head = arr[0:1]
    sorted_arr = sort_array(arr[1:])
    i = 0
    while i < len(sorted_arr) and head[0] > sorted_arr[i]:
        i += 1
    new_arr = np.concatenate((sorted_arr[0: i], head, sorted_arr[i:]) )
    return new_arr

















    # sorted_arr = np.asarray([1, 2, 5, 10])
    # new_value = 8
    # i = 0
    # while new_value > sorted_arr[i]:
    #     i += 1
    #     if i == sorted_arr.shape[0]:
    #         break
    #     new_arr = np.concatenate((sorted_arr[0: i], np.asarray ([new_value]), sorted_arr[i:]))
    #
    # print(sorted_arr)
    # print(new_arr)
    # return new_arr
    #
