from typing import List, Tuple

def calculate_max_value_and_range(arr: List[int]) -> Tuple[int, Tuple[int, int]]:
    """
    Given a list of integers, this function calculates the maximum sum of a contiguous subarray
    and returns that sum along with the start and end indices (1-based) of that subarray.
    """
    L = len(arr)
    values = [0] + arr  # 1-based indexing
    total = calculate_prefix_sums(L, values)

    max_value, max_range = find_max_subarray(L, total)

    return max_value, max_range

def calculate_prefix_sums(L: int, values: List[int]) -> List[int]:
    """
    Given a list of integers, this function calculates the prefix sums and returns them.
    """
    prefix_sums = [0] * (L + 1)
    for i in range(1, L + 1):
        prefix_sums[i] = prefix_sums[i - 1] + values[i]
    return prefix_sums

def find_max_subarray(L: int, prefix_sums: List[int]) -> Tuple[int, Tuple[int, int]]:
    """
    Given the length of the list and its prefix sums, this function finds the subarray with the maximum sum
    and returns the sum along with the start and end indices (1-based) of that subarray.
    """
    max_value = -int(1e9)
    max_range = (0, 0)

    for i in range(L + 1):
        for j in range(i):
            max_value, max_range = update_max_subarray(i, j, max_value, max_range, prefix_sums)
    return max_value, max_range

def update_max_subarray(i: int, j: int, max_value: int, max_range: Tuple[int, int], prefix_sums: List[int]) -> Tuple[int, Tuple[int, int]]:
    """
    Updates the maximum subarray if a new maximum is found.
    """
    current_value = prefix_sums[i] - prefix_sums[j]

    if max_value < current_value:
        max_value = current_value
        max_range = (j + 1, i)

    if max_value == current_value and (i - (j + 1)) < max_range[1] - max_range[0]:
        max_range = (j + 1, i)

    return max_value, max_range

if __name__ == "__main__":
    N = int(input())
    total_max_value = 0
    max_value_ranges = []

    for _ in range(N):
        L = int(input())
        values = list(map(int, input().split()))
        max_value, max_range = calculate_max_value_and_range(values)
        total_max_value += max_value
        max_value_ranges.append(max_range)

    print(total_max_value)
    for start, end in max_value_ranges:
        print(start, end)