import time


# ==========================
# Insertion Sort
# ==========================
def insertion_sort(records, key):

    for i in range(1, len(records)):
        current = records[i]
        j = i - 1

        while j >= 0 and records[j][key] > current[key]:
            records[j + 1] = records[j]
            j -= 1

        records[j + 1] = current


# ==========================
# Binary Search
# ==========================
def binary_search(sorted_records, target_value, key):

    low = 0
    high = len(sorted_records) - 1

    while low <= high:

        mid = (low + high) // 2

        if sorted_records[mid][key] == target_value:
            return mid

        elif sorted_records[mid][key] < target_value:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# ==========================
# Linear Search
# ==========================
def linear_search(records, target_value, key):

    for index, record in enumerate(records):

        if record[key] == target_value:
            return index

    return -1


# ==========================================================
# Comparison-Counting Wrappers (Section 2, Task 5)
# Same logic as above, but return a comparison count instead
# of (or in addition to) the plain result.
# ==========================================================

def insertion_sort_count(records, key):
    """
    Sorts `records` in place exactly like insertion_sort, but
    returns only a single integer: the number of key comparisons
    performed (each 'records[j][key] > current[key]' check counts
    as one comparison).
    """
    comparisons = 0

    for i in range(1, len(records)):
        current = records[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if records[j][key] > current[key]:
                records[j + 1] = records[j]
                j -= 1
            else:
                break

        records[j + 1] = current

    return comparisons


def binary_search_count(sorted_records, target_value, key):
    """
    Same logic as binary_search, but returns a dict:
    {"index": <int>, "comparison_count": <int>}
    Each comparison against sorted_records[mid][key] counts once
    (even though it involves two Python operators, it is one
    logical comparison step in the algorithm).
    """
    low = 0
    high = len(sorted_records) - 1
    comparisons = 0
    index = -1

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if sorted_records[mid][key] == target_value:
            index = mid
            break
        elif sorted_records[mid][key] < target_value:
            low = mid + 1
        else:
            high = mid - 1

    return {"index": index, "comparison_count": comparisons}


def linear_search_count(records, target_value, key):
    """
    Same logic as linear_search, but returns a dict:
    {"index": <int>, "comparison_count": <int>}
    comparison_count == the number of records inspected, which
    for a total miss equals len(records).
    """
    comparisons = 0
    index = -1

    for i, record in enumerate(records):
        comparisons += 1
        if record[key] == target_value:
            index = i
            break

    return {"index": index, "comparison_count": comparisons}
