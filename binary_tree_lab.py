from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right)) 

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is None:
        print(f"Reached None while looking for LCA of {p.val} and {q.val}")
        return None

    # If root matches p or q, return root (LCA found)
    if root.val == p.val or root.val == q.val:
        return root

    # Both p and q less than root? Go left
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)

    # Both greater? Go right
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)

    # Otherwise root splits p and q -> LCA found
    return root

    
    
    
