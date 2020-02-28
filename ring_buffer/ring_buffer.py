from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Find/create the node
        node = self.storage

        # Check if at max capacity, if true pop value from head
        if node.length == self.capacity:
            node.remove_from_head()

        # Add value to queue from tail
        node.add_to_tail(item)

        self.current = node.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # Initialize node as self.storage for easy reading
        node = self.storage

        # If empty buffer, return empty list
        if self.storage.length == 0:
            return list_buffer_contents

        # Run through entire buffer and add values to the list
        x = 0
        while x < self.storage.length:
            hldr_value = node.remove_from_head()
            list_buffer_contents.append(hldr_value)
            node.add_to_tail(hldr_value)
            x += 1

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
