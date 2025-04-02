class Tree:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        # Общее число вершин в поддереве
        self.overall_count = 0

    def insert(self, key):
        if key == self.key:
            return
     
        if key < self.key:
            if self.left is None:
                self.left = Tree(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = Tree(key)
            else:
                self.right.insert(key)


class FoundNode(Exception):
    def __init__(self, node):

        # Сохраняем узел, который вызвал исключение
        self.node = node

def compute_counts(node):
    global count
    if node is None:
        return 0

    left_overall_count = compute_counts(node.left)
    right_overall_count = compute_counts(node.right)

    node.overall_count = left_overall_count + right_overall_count + 1

    if node.left and node.right:
        if node.left.overall_count != node.right.overall_count:
            count += 1
    elif node.left or node.right:
        count += 1

    return node.overall_count


def select_node_for_deletion(node):
    global count
    if node is None:
        return

    select_node_for_deletion(node.left)

    if node.left and node.right:
        if node.left.overall_count != node.right.overall_count:
            count -= 1
            if count == 0:

                # Генерируем искусственную ошибку, чтобы выйти из функции
                raise FoundNode(node)
            
    elif node.left or node.right:
        count -= 1
        if count == 0:

            # Генерируем искусственную ошибку, чтобы выйти из функции
            raise FoundNode(node)

    select_node_for_deletion(node.right)


def delete_median_node(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete_median_node(root.left, key)
    elif key > root.key:
        root.right = delete_median_node(root.right, key)
    else:

        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = root.right
        while temp.left is not None:
            temp = temp.left
        root.key = temp.key
        root.right = delete_median_node(root.right, temp.key)
    return root

def pre_order_traversal(node):
    if node is None:
        return []
    result = [node.key]
    result += pre_order_traversal(node.left)
    result += pre_order_traversal(node.right)
    return result

# ---------------------------------
with open("in.txt", "r") as file:
    nodes = [int(line.strip()) for line in file if line.strip().isdigit()]

# Построение дерева
root = Tree(nodes[0])
for key in nodes[1:]:
    root.insert(key)

count = 0
compute_counts(root)

if count % 2 != 0:
    count = (count + 1) // 2
    node_for_delete = None

    try:
        select_node_for_deletion(root)
    except FoundNode as fn:
        node_for_delete = fn.node

    if node_for_delete is not None:
        root = delete_median_node(root, node_for_delete.key)

traversal_list = pre_order_traversal(root)
with open("out.txt", "w") as file:
    for key in traversal_list:
        file.write(str(key) + "\n")
