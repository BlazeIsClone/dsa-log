class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0

    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.length -= 1
        return True
        

    def getValues(self) -> List[int]:
        result = []
        current = self.head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result
        
