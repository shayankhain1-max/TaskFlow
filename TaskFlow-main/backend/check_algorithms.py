"""
check_algorithms.py

Run with:  python3 check_algorithms.py
(or        python check_algorithms.py   on Windows)

Prints one PASS/FAIL line per test case for insertion_sort,
binary_search, linear_search, and their comparison-counting
wrapper versions. Uses plain if/else, no assert / pytest / unittest.
"""

from algorithms import (
    insertion_sort,
    binary_search,
    linear_search,
    insertion_sort_count,
    binary_search_count,
    linear_search_count,
)


def check(case_name, result, expected):
    if result == expected:
        print(f"PASS: {case_name}")
    else:
        print(f"FAIL: {case_name} — expected {expected}, got {result}")


# ------------------------------------------------------------
# 1. insertion_sort on an empty list
# ------------------------------------------------------------
records = []
insertion_sort(records, "value")
check("insertion_sort empty list stays empty", records, [])

# ------------------------------------------------------------
# 2. insertion_sort on a single-element list
# ------------------------------------------------------------
records = [{"value": 42}]
insertion_sort(records, "value")
check("insertion_sort single element unchanged", records, [{"value": 42}])

# ------------------------------------------------------------
# 3. binary_search: first, last, middle of a sorted list
# ------------------------------------------------------------
sorted_records = [{"value": v} for v in [10, 20, 30, 40, 50]]

result = binary_search(sorted_records, 10, "value")
check("binary_search finds first index", result, 0)

result = binary_search(sorted_records, 50, "value")
check("binary_search finds last index", result, 4)

result = binary_search(sorted_records, 30, "value")
check("binary_search finds middle index", result, 2)

# ------------------------------------------------------------
# 4. binary_search: value absent
# ------------------------------------------------------------
result = binary_search(sorted_records, 999, "value")
check("binary_search returns -1 when absent", result, -1)

# ------------------------------------------------------------
# 5. insertion_sort_count on a small hand-checkable list
# ------------------------------------------------------------
records = [{"value": 3}, {"value": 1}, {"value": 2}]
comparisons = insertion_sort_count(records, "value")

check(
    "insertion_sort_count leaves list correctly sorted",
    [r["value"] for r in records],
    [1, 2, 3],
)
check(
    "insertion_sort_count returns a plain int > 0",
    (type(comparisons) == int and comparisons > 0),
    True,
)

# ------------------------------------------------------------
# 6. binary_search_count: value present at a known index
# ------------------------------------------------------------
sorted_records = [{"value": v} for v in [5, 15, 25, 35, 45]]
result = binary_search_count(sorted_records, 25, "value")

check("binary_search_count finds correct index", result["index"], 2)
check(
    "binary_search_count comparison_count is int > 0",
    (type(result["comparison_count"]) == int and result["comparison_count"] > 0),
    True,
)

# ------------------------------------------------------------
# 7. linear_search_count: value absent
# ------------------------------------------------------------
records = [{"value": v} for v in [1, 2, 3, 4, 5]]
result = linear_search_count(records, 999, "value")

check("linear_search_count index is -1 (not found)", result["index"], -1)
check(
    "linear_search_count comparison_count equals list length",
    result["comparison_count"],
    len(records),
)
