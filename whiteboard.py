# # Return the "centered" average of an array of ints, 
# # which we'll say is the mean average of the values, 
# # except ignoring the largest and smallest values in the array. 
# # If there are multiple copies of the smallest value, remove all copies
# # and likewise for the largest value. 
# # return the smallest whole number integer average
# # You may assume that the array is length 3 or more.

# # Input
# nums1=[1, 2, 3, 4, 100]
# # Outputs:
# # 3

# # Input
# nums2=[1, 1, 5, 5, 10, 8, 7]
# # Outputs:
# # 6

# # Input
# nums3=[-10, -4, -2, -4, -2, 0]
# # Outputs:
# # -3

def mean(num):
    valu = set(num)
    value2 = list(valu)
    value2.sort()
    value2.pop()
    value2.pop(0)
    avg = sum(value2) // len(value2)
    return avg

print(mean([1, 1, 5, 5, 10, 8, 7]))
print(mean([-10, -4, -2, -4, -2, 0]))
print(mean([1, 2, 3, 4, 100]))


def mean1 (nums):
    mins = min(nums)
    maxs = max(nums)
    while mins in nums:
        nums.remove(mins)
        while maxs in nums:
            nums.remove(maxs)
    avg = sum(nums) // len(nums)
    return avg

print(mean1([1, 1, 5, 5, 10, 8, 7]))
print(mean1([-10, -4, -2, -4, -2, 0]))
print(mean1([1, 2, 3, 4, 100]))