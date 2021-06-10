class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
  
class Tree():
  
    def leftRotate(self, x):
        y = x.right
        sub2 = y.left
        y.left = x
        x.right = sub2
  
        x.height = max(self.getHeight(x.left), self.getHeight(x.right)) +1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) +1
  
        return y
  
    def rightRotate(self, x):
        y = x.left
        sub3 = y.right
        y.right = x
        x.left = sub3
  
        x.height = max(self.getHeight(x.left), self.getHeight(x.right)) +1
        y.height = max(self.getHeight(y.left), self.getHeight(y.right)) +1
  
        return y
  
    def getHeight(self, root):
        if not root:
            return 0
  
        return root.height #height gets updated by itself
  
    def getDisparity(self, root):
        if not root:
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right)
  
    def getMinNode(self, root):
        if root is None or root.left is None:
            return root
  
        return self.getMinNode(root.left)
  
    def insert(self, root, key):
        if not root:
            return Node(key)
        
        elif root.data > key:
            root.left = self.insert(root.left, key)
            
        else:
            root.right = self.insert(root.right, key)
  
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) +1
        disparity = self.getDisparity(root)
  
        if disparity > 1 and key < root.left.data:
            return self.rightRotate(root)
        
        if disparity > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if disparity < -1 and key > root.right.data:
            return self.leftRotate(root)
  
  
        if disparity < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
  
        return root
  
    def delete(self, root, key):
        if not root:
            return root
  
        elif root.data > key:
            root.left = self.delete(root.left, key)
  
        elif root.data < key:
            root.right = self.delete(root.right, key)
  
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
  
            if root.right is None:
                temp = root.left
                root = None
                return temp
  
            temp = self.getMinNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
            
        if root is None:
            return root
  
        root.height = max(self.getHeight(root.left), self.getHeight(root.right)) +1
        disparity = self.getDisparity(root)
  
        if disparity > 1 and self.getDisparity(root.left) >= 0:
            return self.rightRotate(root)
        
        if disparity > 1 and self.getDisparity(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if disparity < -1 and self.getDisparity(root.right) <= 0:
            return self.leftRotate(root)
    
        if disparity < -1 and self.getDisparity(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
  
        return root  
    
def traverse(root, space):
    if not root:
        return

    space +=10
    traverse(root.right, space)
    print()
    
    for i in range(10, space):
        print(end = " ")
   
    print(root.data)
    traverse(root.left, space)

  
myTree = Tree()
root = None
nums = [4,8,8,69,420,4,-1,1]
  
for num in nums:
    root = myTree.insert(root, num)
  
print("Preorder Traversal after insertion -")
traverse(root, 0)
  
root = myTree.delete(root, 8)
  
print("Preorder Traversal after deletion -")
traverse(root, 0)