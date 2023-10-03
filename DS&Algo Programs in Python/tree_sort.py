class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.value < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)

def tree_sort(arr):
    root = None
    for item in arr:
        root = insert(root, item)
    inorder_traversal(root)

if __name__ == "__main__":
    input_list = [12, 4, 5, 6, 2, 7, 8, 1, 3, 9, 10, 11]
    print("Unsorted List:")
    print(input_list)

    print("\nSorted List using Tree Sort:")
    tree_sort(input_list)
