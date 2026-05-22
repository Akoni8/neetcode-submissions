class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while (current != None):
            if i == index:
                return current.value
            current = current.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        current = self.head
        i = 0
        while i < index and current:
            current = current.next
            i += 1
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        results = []
        current = self.head.next
        while(current != None):
            results.append(current.value)
            current = current.next

        return results

class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
