#TC:0(n)+3n
#Sc:3n+n

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:  
        
        #dfs
        
        parentNodes = {}
        parentNodes = self.nodeToParents(root, parentNodes,None)
        
        res = self.nodesAtDistanceK(target, k, parentNodes )
        
        return res
    
    ## To find the nodes at distance K 
    def nodesAtDistanceK(self, node, k, parentNodes):
        
        queue = deque([(node, 0)])
        visited = set()
        result = []
        while queue:
            
            curNode, dist = queue.popleft()
            visited.add(curNode.val)
            if dist == k:
                result.append(curNode.val)
                pass
            
            if curNode.left: 
                if curNode.left.val not in visited:
                    queue.append((curNode.left, dist+1))
            
            if curNode.right:
                if curNode.right.val not in visited:
                    queue.append((curNode.right, dist+1))
            
            if parentNodes[curNode]:
                if parentNodes[curNode].val not in visited:
                    queue.append((parentNodes[curNode], dist+1))
            
        return result
            
        
    
    ## To get all the parent nodes in a dictonary
    def nodeToParents(self,node, parentNodes, parent ):
        
        if not node:
            return 
        
        parentNodes[node] = parent
        self.nodeToParents(node.left, parentNodes, node)
        self.nodeToParents(node.right, parentNodes, node)
        
        return parentNodes
    