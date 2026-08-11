import re


# Group (i) -> high priority keywords
GROUP_HIGH = ["urgent", "asap"]

# Group (ii) -> low priority keywords
GROUP_LOW = ["whenever", "low priority"]

# Due-date keywords, checked in this exact order (spec Section 3, Task 3c)
DATE_KEYWORDS_ORDER = [
    "today",
    "tomorrow",
    "next week",
    "next monday",
    "next tuesday",
    "next wednesday",
    "next thursday",
    "next friday",
    "next saturday",
    "next sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday",
]


def parse_task(description: str):
    """
    Deterministic, rule-based mock parser (no network calls, no API key).
    Implements the exact algorithm specified in Section 3, Task 3.
    Returns {"title": str, "priority": "low"|"medium"|"high", "due_date": str|None}
    """

    original_text = description
    text = description.lower()

    # -------------------------------------------------
    # b. Priority — group (i) checked before group (ii)
    # -------------------------------------------------
    matched_high = any(word in text for word in GROUP_HIGH)
    matched_low = any(word in text for word in GROUP_LOW)

    if matched_high:
        priority = "high"
    elif matched_low:
        priority = "low"
    else:
        priority = "medium"

    # -------------------------------------------------
    # c. Due-date hint — first matching keyword in fixed order
    # -------------------------------------------------
    due_date = None
    for word in DATE_KEYWORDS_ORDER:
        if word in text:
            due_date = word
            break

    # -------------------------------------------------
    # d. Title — remove only the spans that actually matched.
    # Every occurrence of every matched group (i)/(ii) keyword
    # is stripped (not just the one that decided priority),
    # plus every occurrence of the matched due-date phrase.
    # Word-boundary aware so we don't corrupt unrelated words
    # (e.g. "low" inside "flower").
    # -------------------------------------------------
    spans_to_remove = []

    if matched_high:
        spans_to_remove.extend(GROUP_HIGH)
    if matched_low:
        spans_to_remove.extend(GROUP_LOW)
    if due_date:
        spans_to_remove.append(due_date)

    title = original_text
    for phrase in spans_to_remove:
        pattern = r"\b" + re.escape(phrase) + r"\b"
        title = re.sub(pattern, "", title, flags=re.IGNORECASE)

    title = re.sub(r"\s+", " ", title).strip()

    if title == "":
        title = "Untitled task"

    return {
        "title": title,
        "priority": priority,
        "due_date": due_date,
    }


if __name__ == "__main__":
    # Quick manual check against the four spec worked examples
    examples = [
        "This is urgent, mark it ASAP please",
        " ",
        "Finish the report next Friday, it's urgent",
        "tomorrow review tomorrow",
    ]
    for e in examples:
        print(repr(e), "->", parse_task(e))
