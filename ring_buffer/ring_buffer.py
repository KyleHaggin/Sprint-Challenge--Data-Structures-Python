from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # Find/create the node
        node = self.storage

        if self.storage.length < self.capacity:
            # Add value to queue from tail
            node.add_to_tail(item)
            self.current = node.head
            return

        if self.storage.head == self.current:
            node.remove_from_head()
            node.add_to_tail(item)
            self.current = self.storage.tail
        else:
            node.remove_from_head()
            node.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # Initialize node as self.storage for easy reading
        node = self.current

        # If empty buffer, return empty list
        if self.storage.length == 0:
            return list_buffer_contents

        x = 0
        while x < self.storage.length:
            list_buffer_contents.append(node.value)
            node = node.next
            if node is None:
                node = self.storage.head
            x += 1
        # Remove None values form list
        list_buffer_contents = [i for i in list_buffer_contents if i]
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.initialize()

    def initialize(self):
        while self.storage.length < self.capacity:
            self.append(None)

    def append(self, item):
        # Find/create the node
        node = self.storage

        if self.storage.length < self.capacity:
            # Add value to queue from tail
            node.add_to_tail(item)
            # Init rest of list as None
            self.current = node.head
            return

        if self.storage.head == self.current:
            node.remove_from_head()
            node.add_to_tail(item)
            self.current = self.storage.tail
        else:
            node.remove_from_head()
            node.add_to_tail(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # Initialize node as self.storage for easy reading
        node = self.current

        x = 0
        while x < self.storage.length:
            if node.value is not None:
                list_buffer_contents.append(node.value)
            node = node.next
            if node is None:
                node = self.storage.head
            x += 1
        # Remove None values form list
        list_buffer_contents = [i for i in list_buffer_contents if i]
        return list_buffer_contents
