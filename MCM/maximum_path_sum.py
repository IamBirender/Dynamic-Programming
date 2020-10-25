class Node(object):
    def __init__(self, right, left, val):
        self.right = right
        self.left = left
        self.val = val

root = Node(None, None, 10)
root.left = Node(None, None, 9)
root.right = Node(None, None, 11)
root.left.left = Node(None, None, 8)
root.left.right = Node(None, None, 7)
root.left.right.right = Node(None, None, 5)
root.left.right.right.right = Node(None, None, 4)
root.left.left.left = Node(None, None, 6)

class get_diameter(object):
    def __init__(self, root):
        self.root = root
        self.answer = float("-inf")
        self.dic = dict()
    
    def _get_diameter(self):
        self._solve(self.root)
        print(self.answer)
        return self.answer
    
    def _solve(self, root):
        
        if root is None:
            return 0
        
        l = self._solve(root.left)
        r = self._solve(root.right)
        
        temp = max(l, r) + 1
        self.answer = max(temp, l + r + 1, self.answer)
        
        return temp
        
obj = get_diameter(root)
obj._get_diameter()
    