# Counts how many times the value n appears in the array arr
def count_occurences(arr, n):
    return 0


# Checks if the value n is between top and bottom
# Returns true if it is, false otherwise
def in_range(n, top, bottom):
    return False

# Returns an integer which is a reverse of the input integer
# For example, reverse(1234) -> 4321
def reverse(n):
    return 0

# Prints the input array in reverse oreder
# E.g. for array [1, 2, 3, 4] it prints "4 3 2 1"
def print_array_reverse(arr):
    pass

# Returns the sum of the smallest and largest numbers form an array
def max_plus_min(arr):
    if not arr:
        raise ValueError("Array should not be empty")
    return max(arr) + min(arr)

# If x is even, returns x/2
# If x is odd, returns 3x+1
def three_x_plus_one(x):
    if x % 2 == 0:
        return x // 2
    else:
        return 3 * x + 1

# Prints the number n to console n times
# E.g. for n = 3, it should print "3 3 3"
def print_n_n_times(n):
    print(" ".join(str(n) * n))
    pass

# Returns n to the power of e
# E.g. power(2, 3) should return 8
def power(n, e):
    print(n**e)

# Returns true if values a b c d are in ascending order
# False otherwise
# E.g. ordered(1, 2, 3, 4) is true but ordered(1, 2, 4, 3) is false
def ordered(a, b, c, d):
    return False

power(3,2)