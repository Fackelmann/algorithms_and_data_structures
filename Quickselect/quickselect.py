from random import randint
from time import time
import matplotlib.pyplot as plt
from scipy import stats

def partition(input_list: list, left: int, right: int, pivot_index: int):
    pivot_value = input_list[pivot_index]
    input_list[pivot_index], input_list[right] = input_list[right], input_list[pivot_index]
    store_index = left
    for i in range(left, right):
        if input_list[i] < pivot_value:
            input_list[store_index], input_list[i] = input_list[i], input_list[store_index]
            store_index += 1
    input_list[store_index], input_list[right] = input_list[right], input_list[store_index]
    return store_index

def select(input_list: list, left: int, right: int, k: int):
    if left == right:
        return input_list[left]
    pivot_index = randint(left, right)
    pivot_index = partition(input_list, left, right, pivot_index)
    if k == pivot_index:
        return input_list[k]
    if k < pivot_index:
        return select(input_list, left, pivot_index - 1, k)
    return select(input_list, pivot_index + 1, right, k)

if __name__ == "__main__":
    n = 5000
    end = 1e6
    exec_time = []
    x = []
    while n <= end:
        x.append(n)
        a = [randint(0,n) for r in range(n)]
        k = randint(0,n-1)
        temp = []
        for _ in range(10):
            t0 = time()
            select(a, 0, len(a)-1, k)
            t1 = time()
            temp.append((t1-t0)*1e6)
        exec_time.append(sum(temp)/10)
        n *= 2
    plt.plot(x, exec_time, marker='o')
    plt.title('Time complexity of QuickSelect')
    plt.ylabel("Execution time (us)")
    plt.xlabel("N")
    plt.grid(True)
    plt.show()
