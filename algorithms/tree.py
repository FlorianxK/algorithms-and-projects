from collections import deque
from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DeepestLevel:
    def __init__(self):
        self.target_node = None
        self.min_depth = float('inf')
        self.max_depth = -1

    def dfs(self, root, depth):
        if root is None:
            return depth-1

        depth_l = self.dfs(root.left,depth+1)
        depth_r = self.dfs(root.right,depth+1)

        if depth_l == depth_r:
            if depth_l > self.max_depth or \
            (depth_l == self.max_depth and depth < self.min_depth):
                self.target_node = root
                self.min_depth = depth
                self.max_depth = depth_l

        return max(depth_l,depth_r)
    
    def subtreeWithAllDeepest(self, root):
        self.dfs(root, 0)
        return self.target_node

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    
    def invert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        self.invert(root.left)
        self.invert(root.right)
        root.left,root.right = root.right,root.left
        return root 
    
    def printLevel(self, root: Optional[TreeNode]):
        level = deque([root])
        nextLevel = deque([])
        while level:
            cur = level.popleft()
            print(cur.val,"",end="")
            if cur.left:
                nextLevel.append(cur.left)
            if cur.right:
                nextLevel.append(cur.right)

            if len(level) <= 0:
                print()
                level = nextLevel
                nextLevel = deque([])

    def preOrder(self, root):
        if root is None:
            return
        print(root.val, end=' ')
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.val, end=' ')
        self.inOrder(root.right)

    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.val, end=' ')

    def sumLeaves(self,root):
        if root.left is None and root.right is None:
            return root.val
        return self.sumLeaves(root.left) + self.sumLeaves(root.right)
    
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        while i < len(traversal):
            depth = 0
            while traversal[i] == '-':  
                depth += 1
                i += 1
            
            num = i
            while i < len(traversal) and traversal[i].isdigit():  
                i += 1
            val = int(traversal[num:i])  

            node = TreeNode(val)

            while stack and stack[-1][1] >= depth:
                stack.pop()

            if stack:
                parent = stack[-1][0]
                if parent.left == None:
                    parent.left = node
                else:
                    parent.right = node
            
            stack.append((node, depth))  

        return stack[0][0]

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)
        j = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            
            while stack[-1].val == postorder[j]:
                stack.pop()
                j += 1
            
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
                
            stack.append(node)
        
        return root

    def dfs(self,root):
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            print(curr.val, end=' ')

    def segmentTree(self,arr: List[int]) -> Optional[TreeNode]:
        n = len(arr)
        left,right = 0,0
        l1,l2,nxt = None,None,None
        for i in range(n):
            if i < n//2:
                print("left")
                left += arr[i]
                if l1 == None and l2 == None:
                    l1 = TreeNode(arr[i])
                elif l2 == None:
                    l2 = TreeNode(arr[i])

                if l1 and l2:
                    nxt = TreeNode(arr[i],l1,l2)
                    l1 = nxt
                    l2 = None

            else:
                print("right")
        print(nxt.val)
        return TreeNode(0)

n1 = TreeNode(4)
n2 = TreeNode(5)
n3 = TreeNode(6)
n4 = TreeNode(7)
n5 = TreeNode(2,n1,n2)
n6 = TreeNode(3,n3,n4)
root = TreeNode(1,n5,n6)

'''
n1 = TreeNode(15)
n2 = TreeNode(7)
n3 = TreeNode(20,n1,n2)
n6 = TreeNode(1)
n4 = TreeNode(9,n6)
n5 = TreeNode(3,n4,n3)

n1 = TreeNode(7)
n2 = TreeNode(4)
n3 = TreeNode(2,n1,n2)
n4 = TreeNode(6)
n5 = TreeNode(5,n4,n3)
n6 = TreeNode(0)
n7 = TreeNode(8)
n8 = TreeNode(1,n6,n7)
root = TreeNode(3,n5,n8)
'''
arr = [1,3,5,7,9,11]
s = Solution()
print("Hwello")
segRoot = s.segmentTree(arr)
s.printLevel(segRoot)

#s.dfs(root)
#preorder = [1,2,4,5,3,6,7]
#postorder = [4,5,2,6,7,3,1]
#node = s.constructFromPrePost(preorder,postorder)
#s.printLevel(node)
#s.printLevel(root)
#v = s.sumLeaves(root)
#print(v)
#traversal = "1-2--3--4-5--6--7"
#res = s.recoverFromPreorder(traversal)
#s.printLevel(res)