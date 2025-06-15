import random
import time
import matplotlib.pyplot as plt
import numpy as np

# Part 1: Randomized Quicksort Implementation
def randomized_partition(arr, low, high):
    pivot_idx = random.randint(low, high)
    arr[high], arr[pivot_idx] = arr[pivot_idx], arr[high]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

def deterministic_partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def deterministic_quicksort(arr, low, high):
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pi - 1)
        deterministic_quicksort(arr, pi + 1, high)

# Comparison
input_sizes = [100, 500, 1000, 5000, 10000]
time_randomized = []
time_deterministic = []

for size in input_sizes:
    arr_random = np.random.randint(0, 100000, size).tolist()
    arr_deterministic = arr_random.copy()

    start = time.time()
    randomized_quicksort(arr_random, 0, len(arr_random) - 1)
    time_randomized.append(time.time() - start)

    start = time.time()
    deterministic_quicksort(arr_deterministic, 0, len(arr_deterministic) - 1)
    time_deterministic.append(time.time() - start)

plt.plot(input_sizes, time_randomized, label="Randomized Quicksort")
plt.plot(input_sizes, time_deterministic, label="Deterministic Quicksort")
plt.xlabel("Input Size")
plt.ylabel("Time (s)")
plt.title("Performance Comparison")
plt.legend()
plt.show()
