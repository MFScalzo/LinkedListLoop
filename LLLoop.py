# Node Class Implementation
class Node:
    data = None
    nextNode = None

    def __init__(self, d: int):
        data = d

# The solution function
def findLoop(head: Node):
    nodesSeen = set()

    while (head != None):
        if head in nodesSeen:
            return head

        nodesSeen.add(head)
        head = head.nextNode

    return None

# BELOW IS ALL TESTING
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

A.nextNode = B
B.nextNode = C
C.nextNode = D
D.nextNode = E
E.nextNode = C

result = findLoop(A)

if id(result) == id(C):
    print("Loop found at Node: " + str(C))

else:
    print("No loop found.")