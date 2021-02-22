class Node(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)

def BuildTree():
    root=Node(50)
    root.left=Node(20)
    root.left.left=Node(10)
    root.left.right=Node(30)
    root.right=Node(80)
    root.right.left=Node(60)
    root.right.right=Node(100)
    return root

def preOrderRecusrsive(root):
    if root:
        print(root.data,end=" ")
        preOrderRecusrsive(root.left)
        preOrderRecusrsive(root.right)

def inOrderRecursive(root):
    if root:
        inOrderRecursive(root.left)
        print(root.data,end=" ")
        inOrderRecursive(root.right)

def postOrderRecursive(root):
    if root:
        postOrderRecursive(root.left)
        postOrderRecursive(root.right)
        print(root.data,end=" ")


def postOrderIterative(root):
    if root:
        s1=[]
        s2=[]
        s1.append(root)
        while s1:
            node=s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:
            node=s2.pop()
            print(node.data,end=" ")

def preOrderIterative(root):
    if root:
        stack=[]
        stack.append(root)
        while len(stack)>0:
            node=stack.pop()
            print(node.data,end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

def inOrderIterative(root):
    if root:
        stack=[]
        stack.append(root)
        current=root.left
        while len(stack)>0 or current:
            if current:
                stack.append(current)
                current=current.left
            else:
                node=stack.pop()
                print(node.data,end=" ")
                current=node.right

root=BuildTree()

preOrderRecusrsive(root)
print()
preOrderRecusrsive(root)
print()
inOrderRecursive(root)
print()
inOrderIterative(root)
print()
postOrderRecursive(root)
print()
postOrderIterative(root)

