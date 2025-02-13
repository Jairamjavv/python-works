"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by 
continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
Note that pos is not passed as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x: Optional[int]):
        self.val = x
        self.next = None


class CreateLinkedList:
    def createLinkedList(self, values, cycle_pos):
        if not values:
            return None

        # Create nodes
        nodes = [ListNode(val) for val in values]

        # Connect nodes
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        # Create a cycle if cycle_pos is valid
        if cycle_pos != -1 and cycle_pos < len(nodes):
            nodes[-1].next = nodes[cycle_pos]

        return nodes[0]

    # Helper function to print the linked list (for debugging)
    def printLinkedList(self, head, limit=10):
        current = head
        count = 0
        while current and count < limit:
            print(current.val, end=" -> ")
            current = current.next
            count += 1
        print("None" if not current else "... (cycle detected)")


class Solution:
    def hasCycleApproach1(self, head: Optional[ListNode]) -> bool:
        start_node = head
        visited_nodes = []

        while start_node != None:
            if start_node.val in visited_nodes:
                return True
            else:
                visited_nodes.append(start_node.val)
                start_node = start_node.next

        return False

    # Floyd's Algorithm (Tortoise and Hare)
    def hasCycleApproach2(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Test cases
def test_hasCycle(list_node: CreateLinkedList, solution: Solution):
    # Test case 1: No cycle
    head1 = list_node.createLinkedList([1, 2, 3, 4, 5], -1)
    print("Linked List 1:")
    list_node.printLinkedList(head1)
    print("Has cycle:", solution.hasCycleApproach2(head1))  # Expected: False
    print()

    # Test case 2: Cycle at position 2 (0-based index)
    head2 = list_node.createLinkedList([1, 2, 3, 4, 5], 2)
    print("Linked List 2:")
    list_node.printLinkedList(head2)
    print("Has cycle:", solution.hasCycleApproach1(head2))  # Expected: True
    print()

    # Test case 3: Single node, no cycle
    head3 = list_node.createLinkedList([1], -1)
    print("Linked List 3:")
    list_node.printLinkedList(head3)
    print("Has cycle:", solution.hasCycleApproach2(head3))  # Expected: False
    print()

    # Test case 4: Single node with cycle (points to itself)
    head4 = list_node.createLinkedList([1], 0)
    print("Linked List 4:")
    list_node.printLinkedList(head4)
    print("Has cycle:", solution.hasCycleApproach2(head4))  # Expected: True
    print()

    # Test case 5: Empty list
    head5 = list_node.createLinkedList([], -1)
    print("Linked List 5:")
    list_node.printLinkedList(head5)
    print("Has cycle:", solution.hasCycleApproach1(head5))  # Expected: False
    print()


# Run tests
s = Solution()
l = CreateLinkedList()
test_hasCycle(l, s)
