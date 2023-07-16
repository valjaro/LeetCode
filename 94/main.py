# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res
        
if __name__ == "__main__":
    s = Solution()
    root = [1,'',2,3]
    root = TreeNode(val=1)
    root_right = TreeNode(val=2)
    root.right = root_right
    root_right.left = TreeNode(val=3)
    r = s.inorderTraversal(root)
    print(r)