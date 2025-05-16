# Returns the largest number in an array
def max(arr):
    max = arr[0]
    for i in range(2, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max

# Returns the smallest number in an array
def min(arr):
    min = 0
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

# Returns the largest of three numbers
def largest(a, b, c):
    if a > b or a > c:
        return a
    else:
        if b > c:
            return b
    return c

# Returns the first digit of a number
def first_digit(n):
    nStr = str(n)
    return nStr[0]

# Returhs the nth fibonacci munber
def fibonacci(n):
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)