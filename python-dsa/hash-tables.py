# implementation of hash tables using Seperate Chaining


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity  # the hash table array

    # returns an index for the key passed
    def _hash(self, key):
        return (
            hash(key) % self.capacity
        )  # python inbuilt hash function, modulo with the hash capacity

    def insert(self, key, value):
        index = self._hash(key)
        new_node = Node(key, value)
        if self.table[index]: 
            current_node = self.table[index]
            while current_node:
                pass
            self.table[index].next = new_node
        else:
            self.table[index] = new_node
            self.size += 1
