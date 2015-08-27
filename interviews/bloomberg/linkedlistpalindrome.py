class Node:
    def __init__(self, val=0, head=None):
        self.val = val
        self.head = head

    def __str__(self):
        if self.head:
            return "Val: " + str(self.val) + " Head: " + str(self.head.val)
        else:
            return "Val: " + str(self.val) + " Head: NULL"


def is_palindrome(r):
    def backwards(n):
        if n:
            for y in backwards(n.head):
                yield y
            yield n.val

    def forwards(n):
        if n:
            yield n.val
            for y in forwards(n.head):
                yield y

    for x, y in zip(backwards(r), forwards(r)):
        if x != y:
            return False

    return True

if __name__ == "__main__":
    r = Node(1, Node(2, Node(3, Node(2, Node(1)))))
    print(is_palindrome(r))
