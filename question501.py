# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    numofnodes = {}
    largekey = []
    largevalue = 1
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        if root == None:
            return None
        
        self.largekey.append(root.val)
        self.numofnodes[root.val] = 1
        if root.left != None:
            self.traverse(root.left)
        if root.right != None:
            self.traverse(root.right)
        
        return self.largekey
        
        
        
        
        
    def traverse(self,node):
        
        if node.val in self.numofnodes:
            self.numofnodes[node.val] += 1
        else:
            self.numofnodes[node.val] = 1
            
        self.repeaternode(node)
        if node.left != None:
            self.traverse(node.left)
        if node.right != None:
            self.traverse(node.right)
            
            
    def repeaternode(self,node):
        if self.numofnodes[node.val] > self.largevalue:
            del self.largekey [:]
            self.largekey.append(node.val)
            self.largevalue = self.numofnodes[node.val]
        elif self.numofnodes[node.val] == self.largevalue:
            if node.val in self.largekey:
                pass
            else:
                self.largekey.append(node.val)
        