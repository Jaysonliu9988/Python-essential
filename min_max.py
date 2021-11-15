# Write functions that replicate Python's built-in "min()" and "max()" functions. 
# They should receives a parameter named "nums" (a list of numbers) and return the smallest or largest of those numbers. 
# These are two separate functions. Feel free to just create one of them, since the process is essentially the same.
# Obviously, your code should not use the built-in "min()" or "max()" functions 
# - you should implement the functionality yourself, e.g. using a loop and a comparison.



def min(nums):
    mini = nums[0]
    for i in nums[0:]:
        if i < mini:
            mini = i
        print('This is minimun number {0}'.format(mini))
    return mini
nums = [21, 31, 11, 10, 9, 8, 7, 77, 99, 88]
print(min(nums))


def max(nums):
    max = nums[0]
    for i in nums[0:]:
        if i > max:
            max = i
        print('This is the maxmun number {0}'.format(max))
    return max
    
nums = [21, 31, 11, 10, 9, 8, 7, 77, 99, 88]
print(max(nums))