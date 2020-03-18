class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getPreIndex():
    return constructTreeUtil.preIndex


def incrementPreIndex():
    constructTreeUtil.preIndex += 1


def constructTreeUtil(pre, low, high, size):
    # Base Case
    if (getPreIndex() >= size or low > high):
        return None
    root = Node(pre[getPreIndex()])
    incrementPreIndex()

    if low == high:
        return root

    for i in range(low, high + 1):
        if pre[i] > root.data:
            break

    root.left = constructTreeUtil(pre, getPreIndex(), i - 1, size)

    root.right = constructTreeUtil(pre, i, high, size)

    return root


def constructTree(pre):
    size = len(pre)
    constructTreeUtil.preIndex = 0
    return constructTreeUtil(pre, 0, size - 1, size)


def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print
    root.data,
    printInorder(root.right)


pre = [35, 23, 26, 46, 40, 39, 41, 52]

root = constructTree(pre)
print

printInorder(root)
