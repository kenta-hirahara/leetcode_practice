import pytest
from solutions.lc1_two_sum import twoSum

@pytest.mark.parametrize(('nums', 'target', 'expected'),
    [
            ([2, 7, 11, 15], 9, [0, 1]),  
            ([3, 2, 4], 6, [1, 2]),  
            ([3, 3], 6, [0, 1]),  
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19, [8, 9]),  
            ([0, 4, 3, 0], 0, [0, 3]),  
            ([-3, 4, 3, 90], 0, [0, 2]),  
            ([1, 5, 1, 5], 10, [1, 3]),  
            ([1000000, 500000, -1500000], -1000000, [1, 2]),  
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 18, [7, 9]),  
    ]
)
def test_twoSum(nums, target, expected):
    assert twoSum(nums, target) == expected
