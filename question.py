# Sum of two interview question.
# Find if a target can be added by two numbers in a list and show the indices. Return none if otherwise.
# Time complexity is not allowed to be O(n^2). No nested for or while loops are allowed.
def two_sums(nums, target):
    pair = []
    for i, v in enumerate(nums):
        if (target - v) in nums and i != nums.index(target - v):
            pair = [i, nums.index(target - v)]
            break
    if pair != []:
        return pair
    else:
        return None

print(two_sums([1,2,3,4,5,6],10))
