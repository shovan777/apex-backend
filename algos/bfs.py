class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Write your code here
        queue = []
        print(root.data, end=" ")
        queue.append(root)
        while len(queue) > 0:
            cur = queue.pop(0)
            if cur.left:
                print(cur.left.data, end=" ")
                queue.append(cur.left)
            if cur.right:
                print(cur.right.data, end=" ")
                queue.append(cur.right)


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
