import numpy as np


def sliding_window_sum(data,k):
    sums = []
    for i in range(len(data) - k + 1):
        window = data[i:i+k]
        sums.append(np.sum(window))
    return np.array(sums)



data = np.array([1,2,3,4,5])
k = 3
print(sliding_window_sum(data,k))