#!/usr/bin/python3

"""
breadth-first search algorithm.
"""


def canUnlockAll(boxes):
    '''
    canUnlockAll
    Args:
      boxes: list of lists
    Returns:
      True if all boxes can be opened, else return False
    '''
    visited = [False] * len(boxes)
    visited[0] = True
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)
