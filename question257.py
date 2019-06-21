# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.Paths = []
        if root == None:
            return self.Paths
        else:
            self.traversals(root,'')
            return self.Paths
        
        
    def traversals(self,node,string):
        if node.left == None and node.right == None:
            self.Paths.append(string + str(node.val))
        if node.left != None:
            self.traversals(node.left, string + str(node.val) + '->')
        if node.right != None:
            self.traversals(node.right, string + str(node.val) + '->')