from typing import List, TypeVar

T = TypeVar('T')


def merge_lists(original: List[T], new_changes: List[T]):
    # We want to distribute the work such that we have the minimal number of changes.
    ids_to_ignore = []

    new_merged: List[T] = [None for _ in range(max(len(original), len(new_changes)))]

    # add all the ones that are not changing.
    for index, element in enumerate(original):
        if index < len(new_changes) and element == new_changes[index]:
            # No change here.
            new_merged[index] = element
            ids_to_ignore.append(index)

        # Add all the ones that aren't doing anything (None)
        if original[index] is None:
            new_merged[index] = new_changes[index]
            ids_to_ignore.append(index)

    for index in range(len(new_changes)):
        if index not in ids_to_ignore:
            # We still need to update this one.
            new_merged[index] = new_changes[index]

    # In case the original one was longer, iterate over the tail.
    for index in range(len(new_changes), len(original)):
        if index not in ids_to_ignore:
            # We still need to update this one.
            new_merged[index] = original[index]

    return new_merged
