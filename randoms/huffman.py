import sys
from heapq import heapify, heappush, heappop


class Node:
    def __init__(self, char=None, freq=None, left=None, right=None):
        self.char = char
        self.freq = freq

        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq

    def __str__(self):
        return "%s: %s" % (self.char, self.freq)


def get_frequencies(text):
    counts = dict()
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts


def construct_tree(frequencies):
    priority_queue = [Node(char, freq) for char, freq in frequencies.items()]
    heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heappop(priority_queue)
        right = heappop(priority_queue)

        merged = Node(freq=left.freq+right.freq, left=left, right=right)
        heappush(priority_queue, merged)

    return heappop(priority_queue)


def inorder(node, path=""):
    if node.left:
        yield from inorder(node.left, path + "0")
    if node.char:
        yield node.char, path
    if node.right:
        yield from inorder(node.right, path + "1")


def encoding(tree):
    return {char: path for char, path in inorder(tree)}


def encode(text, mapping):
    return "".join([mapping[char] for char in text])


def decode(encrypted, tree):
    result = list()

    current_node = tree

    for char in encrypted:
        if char == "0":
            current_node = current_node.left
        elif char == "1":
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            result.append(current_node.char)
            current_node = tree

    return "".join(result)


if __name__ == "__main__":
    input_text = "".join(line for line in sys.stdin)
    frequencies = get_frequencies(input_text)

    tree = construct_tree(frequencies)
    encode_mapping = encoding(tree)
    encoded = encode(input_text, encode_mapping)
    decoded = decode(encoded, tree)

    print(input_text)
    print(encoded)
    print(decoded)
    print(len(input_text) * 8 - len(encoded))
