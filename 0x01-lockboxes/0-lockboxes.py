#!/usr/bin/python3
"""Lockboxes Module"""


def DFS(boxes, box, visited):
    """Dipth First Algorithm"""
    for x in box:
        if x < len(boxes) and visited.count(x) == 0:
            visited.append(x)
            DFS(boxes, boxes[x], visited)


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, else return False"""
    visited = [0]
    DFS(boxes, boxes[0], visited)
    if len(boxes) == len(visited):
        return True
    return False
