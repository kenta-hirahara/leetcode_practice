def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    set_nums2 = set(nums2)
    result = []
    for num in nums1:
        if num in set_nums2:
            result.append(num)
            set_nums2.remove(num)
    return result

print(intersection([1,2,2,1], [2,2]))
print(intersection([4,9,5], [9,4,9,8,4]))
