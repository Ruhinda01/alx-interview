#!/usr/bin/python3
"""
Lockboxes problem:
n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """
    checks if all boxes can be opened
    Param:
    boxes (list): list of list of boxes
    Return:
    True if all boxes can be opened
    False if not
    """
    box_size = len(boxes)

    unlocked = set()

    for idx, box in enumerate(boxes):
        if idx == 0:
            unlocked.add(idx)
        for key in box:
            if key < box_size and key not in unlocked and key != idx:
                unlocked.add(key)
    return len(unlocked) == box_size
