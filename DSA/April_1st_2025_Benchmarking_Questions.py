"""
Sorting Algorithms and Analysis
"""
from typing import List

# ========================
# Selection Sort
# ========================
"""
Selection Sort:
- Repeatedly selects the smallest element from the unsorted portion and moves it to the beginning.
- Runtime: O(n^2) in all cases.
- Best-case: O(n^2) — selection sort always scans entire unsorted list.
- Worst-case: Any input (unsorted, reverse sorted, etc.) results in O(n^2).
- At each stage: The beginning of the array becomes sorted; smallest elements accumulate at the start.
"""
def selection_sort(arr: List[int]) -> int:
    n = len(arr)
    swaps = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return swaps

# ========================
# Insertion Sort
# ========================
"""
Insertion Sort:
- Builds the final sorted array one element at a time.
- Runtime: O(n^2)
- Best-case: O(n), when the array is already sorted.
- Best-case input: Already sorted array.
- At each stage: The left portion is sorted, new element inserted at correct place.
"""
def insertion_sort(arr: List[int]) -> int:
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
        arr[j + 1] = key
    return shifts

# ========================
# Sorting Concepts
# ========================
"""
Stable Sort:
- Maintains the relative order of equal elements.

In-place Sort:
- Uses constant extra space (no additional array).

Stability:
- Selection Sort: Not stable
- Merge Sort: Stable
- Quick Sort: Not stable
- Insertion Sort: Stable
"""

# ========================
# Merge Sort
# ========================
"""
Merge Sort:
- Recursively divides the array in half and merges sorted halves.
- Runtime: O(n log n)
  -> log n levels of division and O(n) merging per level.
- Intermediate stage: Array is broken into smaller pieces then rebuilt in order.
- Handles duplicates well due to stability in merge phase.
"""
def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ========================
# Quicksort
# ========================
"""
Quicksort:
- Picks a pivot and partitions array such that left < pivot and right > pivot.
- Recursively sorts the partitions.
- Average case: O(n log n)
  -> log n recursive depth, each taking linear partitioning time.
- Worst-case: O(n^2), happens when array is already sorted and pivot is poorly chosen.
- 3-Way Quicksort: Partitions into <, =, > sections — better with many duplicates.
- Quicksort on "SWIMPEATSFRIES" after partitioning on first 'S':
  - ['I', 'M', 'P', 'E', 'A', 'T', 'R', 'I', 'E', 'S'] | pivot 'S' | ['W', 'S', 'F']
- Quickselect: Finds the k-th smallest element using quicksort-like partitioning.
- Intermediate stage: Pivot divides array, then recursive sorting continues.
"""
def quicksort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr[1:] if x > pivot]
    return quicksort(less) + equal + quicksort(greater)

