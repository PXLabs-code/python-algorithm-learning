"""Solution for the Two Sum problem."""


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    """Return indices of two distinct values whose sum equals target."""
    seen: dict[int, int] = {}

    for index, value in enumerate(nums):
        complement = target - value
        if complement in seen:
            return seen[complement], index
        seen[value] = index

    raise ValueError("No two sum solution")
