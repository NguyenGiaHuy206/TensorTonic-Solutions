from collections import defaultdict
def deduplicate(records, key_columns, strategy):
    """
    Deduplicate records by key columns using the given strategy.
    """
    # Write code here

    groups = defaultdict(list)
    first_index = {}

    for i, rec in enumerate(records):
        key = tuple(rec.get(col) for col in key_columns)
        groups[key].append((i, rec))

        if key not in first_index:
            first_index[key] = i

    def missing_count(rec):
        return sum(v is None for v in rec.values())

    selected = []

    for key, items in groups.items():

        if strategy == "first":
            chosen = min(items, key=lambda x: x[0])[1]

        elif strategy == "last":
            chosen = max(items, key=lambda x: x[0])[1]

        elif strategy == "most_complete":
            chosen = min(items, key=lambda x: (missing_count(x[1]), x[0]))[1]

        else:
            raise ValueError("Unknown strategy")

        selected.append((first_index[key], chosen))

    selected.sort(key=lambda x: x[0])

    return [rec for _, rec in selected]
    pass