"""
benchmark.py

Run with:  python3 benchmark.py

Uses the comparison-counting wrapper functions (Section 2, Task 5) against
synthetic in-memory task dicts shaped like the app's real tasks (title,
priority, due_date), at three sizes: 10, 500, 3000.
Prints the results and writes them to benchmark_results.txt.
"""

import random

from algorithms import (
    insertion_sort_count,
    binary_search_count,
    linear_search_count,
)

SIZES = [10, 500, 3000]
PRIORITIES = ["low", "medium", "high"]
priority_rank = {"low": 1, "medium": 2, "high": 3}


def make_records(n):
    records = []
    for i in range(n):
        records.append({
            "title": f"Task {i:05d}",
            "priority": priority_rank[random.choice(PRIORITIES)],
            "due_date": random.choice(["today", "tomorrow", "next friday", None]),
        })
    return records


def run():
    lines = []
    lines.append(f"{'Size':>6} | {'InsertionSort (comparisons)':>28} | "
                  f"{'BinarySearch (comparisons)':>26} | {'LinearSearch (comparisons)':>26}")
    lines.append("-" * 100)

    for n in SIZES:
        records = make_records(n)

        # Insertion sort comparison count (sorts by priority rank)
        sort_data = [dict(r) for r in records]
        sort_comparisons = insertion_sort_count(sort_data, "priority")

        # Binary search: search for a title known to exist, on data
        # already sorted by title
        by_title = sorted([dict(r) for r in records], key=lambda r: r["title"])
        target_title = by_title[n // 2]["title"] if n > 0 else None
        bsearch_result = binary_search_count(by_title, target_title, "title") if n > 0 else {"comparison_count": 0}

        # Linear search: same target, unsorted order
        lsearch_result = linear_search_count(records, target_title, "title") if n > 0 else {"comparison_count": 0}

        line = (f"{n:>6} | {sort_comparisons:>28} | "
                f"{bsearch_result['comparison_count']:>26} | {lsearch_result['comparison_count']:>26}")
        lines.append(line)

    output = "\n".join(lines)
    print(output)

    with open("benchmark_results.txt", "w") as f:
        f.write(output + "\n")


if __name__ == "__main__":
    run()
