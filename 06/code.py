class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)

        elif key > self.key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)

    def pre_order_traversal(self):
        result = [self.key]

        if self.left:
            result += self.left.pre_order_traversal()
        if self.right:
            result += self.right.pre_order_traversal()
        return result


with open('input.txt', 'r') as file:
    arr = [int(line.strip()) for line in file]

root = Node(arr[0])

for x in arr[1:]:
    root.insert(x)

result = root.pre_order_traversal()

with open('output.txt', 'w') as file:

    file.write("\n".join(map(str, result)))