
class Node(object):
    def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


def findIndex(curr, inorder, low, high):
    for i in range(low, high+1):
        if inorder[i] == curr:
            return i

    return -1


def buildBinaryTree(inorder, preorder, low, high):
    if low > high:
        return None

    if currnt_index[0] == len(preorder): return None

    curr = preorder[currnt_index[0]]
    root = Node(curr)
    currnt_index[0] += 1
    if low == high:
        return root

    index_in_inorder = findIndex(curr, inorder, low, high)


    root.left = buildBinaryTree(inorder, preorder, low, index_in_inorder-1)

    root.right = buildBinaryTree(inorder, preorder, index_in_inorder + 1, high)

    return root


def preorderTraversal(root):
    if root:
        print(root.data,end =" ")
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.data,end =" ")
        inOrderTraversal(root.right)


inorder = ['D', 'B', 'E', 'A', 'F', 'C']
preorder = ['A', 'B', 'D', 'E', 'C', 'F']
currnt_index = [0]

root = buildBinaryTree(inorder, preorder,0,len(preorder)-1)
preorderTraversal(root)
print()
inOrderTraversal(root)
print()