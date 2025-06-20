# Node class for singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Add a node at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    # Convert linked list to Python list (for easy display)
    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    # Insertion sort for the linked list
    def insertion_sort(self):
        sorted_head = None
        current = self.head
        while current:
            next_node = current.next
            if not sorted_head or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node
        self.head = sorted_head

    # Merge two sorted linked lists
    def merge_sorted(self, other):
        dummy = Node(0)
        tail = dummy
        a = self.head
        b = other.head

        while a and b:
            if a.data <= b.data:
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next

        tail.next = a if a else b

        merged = SinglyLinkedList()
        merged.head = dummy.next
        return merged

# Example usage
list1 = SinglyLinkedList()
list2 = SinglyLinkedList()

for value in [3, 1, 4]:
    list1.append(value)
for value in [2, 5, 0]:
    list2.append(value)

list1.insertion_sort()
list2.insertion_sort()
merged = list1.merge_sorted(list2)
merged.reverse()

print("Reversed merged sorted list:", merged.to_list())
# Reversed merged sorted list: [5, 4, 3, 2, 1, 0]
