import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def partition(arr, pivot):
    left, right = [], []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
    return left, right

def quick_select(arr, k):

    # sort the individual groups using insertion sort
    if len(arr) <= 5:
        insertion_sort(arr)
        return arr[k]
    
    # Divide into groups of 5
    groups = [arr[i:i + 5] for i in range(0, len(arr), 5)]

    # Collect n/5 medians
    medians = [quick_select(group, len(group) // 2) for group in groups]

    # Recursively find n/5 medians
    median_of_medians = quick_select(medians, len(medians) // 2)

    # Partition array on median of medians
    left, right = partition(arr, median_of_medians)

    # Recursively run quickselect on the partitioned array
    if k < len(left):
        return quick_select(left, k)
    elif k >= len(arr) - len(right):
        return quick_select(right, k - (len(arr) - len(right)))
    else:
        return median_of_medians

# Driver code
# arr = input("Enter array elements separated by space: ").strip(" ").split(" ")
# arr = list(map(int,arr))

# Time complexity analysis code
n = int(input("enter number of elements of array: "))
arr = random.sample(range(n+1),n)
# print(arr)


k = int(input("Enter the value of k: "))
start_time = time.time()
result = quick_select(arr, k-1)
end_time = time.time() - start_time
print(f"The {k}-th smallest element is {result}")
print(f"time taken to run code is: {end_time}")