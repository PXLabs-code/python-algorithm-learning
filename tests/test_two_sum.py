import pytest

from algorithms.two_sum import two_sum


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, (0, 1)),
        ([3, 2, 4], 6, (1, 2)),
        ([3, 3], 6, (0, 1)),
        ([-3, 4, 3, 90], 0, (0, 2)),
        ([0, 4, 3, 0], 0, (0, 3)),
    ],
)
def test_two_sum(nums: list[int], target: int, expected: tuple[int, int]) -> None:
    assert two_sum(nums, target) == expected


@pytest.mark.parametrize(("nums", "target"), [([], 0), ([1], 1), ([1, 2], 4)])
def test_two_sum_raises_when_no_pair_exists(nums: list[int], target: int) -> None:
    with pytest.raises(ValueError, match="No two sum solution"):
        two_sum(nums, target)
