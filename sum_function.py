# Write a function that replicates Python's built-in "sum()" function. 
# It should receives a parameter named "nums" (a list of numbers) and returns the sum of those numbers.
# Obviously, your code should not use the built-in "sum()" function
#  - you should implement the functionality yourself, e.g. using a loop and addition.


def sum(nums):
    ret = 0
    for i in nums:
        ret += i
    print(ret)
num = [2, 3, 4, 5]
sum(num)
