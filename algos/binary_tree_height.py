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

    def getHeight(self, root):
        # Write your code here
        # count_right = 0
        # count_left = 0
        # cur = root.right
        # while cur:
        #     # print(cur.data)
        #     count_right += 1
        #     cur = cur.right
        if not root:
            return -1
        return 1 + max(self.getHeight(root.right), self.getHeight(root.left))


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
height = myTree.getHeight(root)
print(height)
