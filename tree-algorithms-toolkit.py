### Project: Tree Algorithms Toolkit
# File: tree_algorithms_toolkit/main.py

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, l, r):
        if l == r:
            self.tree[node] = arr[l]
        else:
            mid = (l + r) // 2
            self.build(arr, 2 * node + 1, l, mid)
            self.build(arr, 2 * node + 2, mid + 1, r)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, l, r, ql, qr):
        if ql > r or qr < l:
            return 0
        if ql <= l and qr >= r:
            return self.tree[node]
        mid = (l + r) // 2
        left = self.query(2 * node + 1, l, mid, ql, qr)
        right = self.query(2 * node + 2, mid + 1, r, ql, qr)
        return left + right

    def update(self, node, l, r, idx, val):
        if l == r:
            self.tree[node] = val
        else:
            mid = (l + r) // 2
            if idx <= mid:
                self.update(2 * node + 1, l, mid, idx, val)
            else:
                self.update(2 * node + 2, mid + 1, r, idx, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


# Example usage
if __name__ == "__main__":
    print("Segment Tree Example:")
    arr = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(arr)
    print("Sum from index 1 to 3:", seg_tree.query(0, 0, len(arr)-1, 1, 3))
    seg_tree.update(0, 0, len(arr)-1, 1, 10)
    print("Sum after update (index 1 set to 10):", seg_tree.query(0, 0, len(arr)-1, 1, 3))

    print("\nTrie Example:")
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    print("Search 'apple':", trie.search("apple"))
    print("Search 'app':", trie.search("app"))
    print("Starts with 'ap':", trie.starts_with("ap"))
