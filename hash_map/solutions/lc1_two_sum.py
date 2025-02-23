def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = dict()
    for i, num in enumerate(nums):
        if num not in hashmap:
            hashmap[target - num] = i
        else:
            return [hashmap[num], i]
