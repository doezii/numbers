import time

def calculate_max(array):
    max = array[0]
    for element in array:
        if element > max:
            max = element
    return max

def calculate_min(array):
    min = array[0]
    for element in array:
        if (element < min):
            min = element
    return min

def calculate_sum(array):
    sum = 0
    for element in array:
        sum += element
    return sum

def calculate_mult(array):
    p = 1
    for element in array:
        p = p * element
    return p

def calculate_time(start_time):
    return time.time() - start_time

# additional func
def calculate_odds_count(array):
    odds = 0
    for element in array:
        if (element % 2 == 1):
            odds += 1
    return odds

# open file for readonly
file = open("file.txt", "r")
# split on space
file = file.read().split(' ')
# start timer
time_start = time.time()

if (len(file) > 1):
    nums = list(map(int, file))
else:
    print("File is empty")
    exit(0)

print("Min: %d" % calculate_min(nums))
print("Max: %d" % calculate_max(nums))

# catching OverflowError
try:
    print("Sum: %d" % calculate_sum(nums))
    print("Mult: %d" % calculate_mult(nums))
except OverflowError:
    print("Got overflow error on calculating sum or mult")

print("Run time: %f seconds" % calculate_time(time_start))