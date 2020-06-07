class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None
        self.prev = None


class DoubleList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, node):
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def remove(self, node):
        # can be head node or tail node
        prev_node = node.prev
        next_node = node.next
        if prev_node:
            prev_node.next = next_node
        else:  # head node was removed
            self.head = next_node
        if next_node:
            next_node.prev = prev_node
        else:  # tail node was removed
            self.tail = prev_node

        self.size -= 1

    def remove_last(self):
        removed = self.tail
        prev = self.tail.prev
        if prev:
            prev.next = None
        self.tail = prev
        self.size -= 1
        return removed

    def get_size(self):
        return self.size


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maps = {}  # key: int, val: Node
        self.cap = capacity
        self.cache = DoubleList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.maps:
            return -1
        val = self.maps[key].val
        self.put(key, val)
        return val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        new_node = Node(key, value)
        if key in self.maps:
            self.cache.remove(self.maps[key])
            self.cache.add_first(new_node)
            self.maps[key] = new_node
        else:
            if self.cap == self.cache.size:
                last = self.cache.remove_last()
                self.maps.pop(last.key)
            self.cache.add_first(new_node)
            self.maps[key] = new_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    obj.get(1)
    obj.put(3, 3)
    obj.get(2)
