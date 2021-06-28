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
    # root.left.right.left = Node(200)
    return root

def preOrderRecusrsive(root):
    if root:
        print(root.data,end=" ")
        preOrderRecusrsive(root.left)
        preOrderRecusrsive(root.right)

def root_to_leaf_sum(root,sum):
    if root is None:
        return
    if root.left is None and root.right is None:
        print(sum+root.data , end=" ")
        return

    root_to_leaf_sum(root.left,sum+root.data)
    root_to_leaf_sum(root.right,sum+root.data)



roor = BuildTree()
preOrderRecusrsive(roor)
print()
root_to_leaf_sum(roor,0)
