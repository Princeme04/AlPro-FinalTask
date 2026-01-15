class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        cur = self.root
        while True:
            if value < cur.value:
                if cur.left is None:
                    cur.left = Node(value)
                    return
                cur = cur.left
            elif value > cur.value:
                if cur.right is None:
                    cur.right = Node(value)
                    return
                cur = cur.right
            else:
                return  # ignore duplicates


# ---- pretty print like the picture ----
# Adapted from common StackOverflow "print tree" answers. [web:94][web:105]
def _display_aux(node):
    if node.right is None and node.left is None:
        line = str(node.value)
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = str(node.value)
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = str(node.value)
        u = len(s)
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = str(node.value)
    u = len(s)
    first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
    if p < q:
        left += [" " * n] * (q - p)
    elif q < p:
        right += [" " * m] * (p - q)
    zipped_lines = zip(left, right)
    lines = [a + u * " " + b for a, b in zipped_lines]
    return [first_line, second_line] + lines, n + m + u, max(p, q) + 2, n + u // 2


def print_tree(node):
    if node is None:
        print("(empty)")
        return
    lines, *_ = _display_aux(node)
    for line in lines:
        print(line)
if __name__ == "__main__":
    bst = BST()
    values = [10, 5, 15, 2, 7, 12, 18, 1, 3, 6, 8, 11, 13, 16, 19, 4, 9, 17, 20]
    for v in values:
        bst.insert(v)

    print_tree(bst.root)
