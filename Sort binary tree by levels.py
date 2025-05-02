from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(root):
    if root is None:
        return []
    work_list = deque([root])
    res = []

    while work_list:
        work_el = work_list.popleft()
        res.append(work_el.value)

        if work_el.left:
            work_list.append(work_el.left)
        if work_el.right:
            work_list.append(work_el.right)

    return res
