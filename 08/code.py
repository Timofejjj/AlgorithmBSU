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

    def search_min_left_key_Adres(self):
        current = self
        while current.left:
            current = current.left
        return current

    def delite(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.delite(key)
            return self
        elif key > self.key:
            if self.right:
                self.right = self.right.delite(key)
            return self
        else:
            if (self.left is None) and (self.right is None):
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right

            most_left_node = self.right.search_min_left_key_Adres()
            self.key = most_left_node.key
            self.right = self.right.delite(most_left_node.key)
            return self

def main():
    key_to_delete = int(input().strip())
    input()  
    tree_keys = []

    while True:
        first_line = input().strip()
        if first_line != "":
            tree_keys.append(int(first_line))
        else:
            break

    root = Node(tree_keys[0])
    for key in tree_keys[1:]:
        root.insert(key)
    
    root = root.delite(key_to_delete)
    
    result = root.pre_order_traversal() if root else []
    print("\n".join(map(str, result)))

if __name__ == '__main__':
    main()
