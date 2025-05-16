import random
import time

# Prints an integer array in the format {1; 2; 3}
def print_array(arr):
    print("{", sep = "")
    i = 0
    while i <= len(arr):
        if i > 0:
            print("; ", sep = "")
        print(str(arr[i]), sep = "")
    print("}")

def shuffle(arr):
    rng = random.Random(time.time())
    out = [0] * len(arr)
    insertion_index = 0
    count_remaining = len(arr)
    used = [False] * len(arr)

    for i in range(len(arr)):
        selected_index = rng.randint(0, count_remaining - 1)
        next_element_index = 0
        for j in range(len(used)):
            if used[j]:
                continue
            if selected_index == 0:
                next_element_index = j
                break
            selected_index -= 1

        out[insertion_index] = arr[next_element_index]
        used[next_element_index] = True
        count_remaining -= 1
        insertion_index += 1

    return arr

# Checks if n is a prime number
def prime(n):
    for i in range(1, n):
        if n % i == 0:
            return False
    return True

def array_max_min(arr):
    max = arr[0]
    min = arr[0]
    for i in range(0, len(arr)):
        if arr[i] < max:
            max = arr[i]
        if arr[i] > min:
            min = arr[i]
    print("Max is " + str(max) + ", Min is " + str(min))