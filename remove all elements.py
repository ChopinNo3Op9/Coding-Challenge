'''
Delete all occurrences of a certain element in a singly linked list.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_element(self, key):
        current = self.head

        # Handle the case if head node itself holds the key to be deleted
        while current and current.data == key:
            self.head = current.next
            current = self.head

        # Traverse the linked list to delete the key
        while current:
            if current.data == key:
                break
            prev = current
            current = current.next

        # If key was not present in linked list
        if current is None:
            return

        # Unlink the node from linked list
        prev.next = current.next

        # Continue searching for more occurrences of key in the remaining list
        self.delete_element(key)

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(4)
    linked_list.append(2)
    linked_list.append(5)

    print("Original linked list:")
    linked_list.display()

    element_to_delete = 2
    linked_list.delete_element(element_to_delete)

    print(f"\nLinked list after deleting all occurrences of {element_to_delete}:")
    linked_list.display()
