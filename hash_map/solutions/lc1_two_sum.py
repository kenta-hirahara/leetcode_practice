def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = dict()
    for i, num in enumerate(nums):
        if num not in hashmap:
            hashmap[target - num] = i
        else:
            return [hashmap[num], i]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
