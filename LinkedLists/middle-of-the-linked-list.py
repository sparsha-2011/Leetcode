from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a given singly linked list.
        If there are two middle nodes (even-length list), returns the second middle node.
        
        :param head: Head of the singly linked list
        :return: The middle node of the linked list
        """
        slow = head
        fast = head
        
        # In an even length linked list with two middle nodes, to print the second middle
        # we just have to add 'and fast.next.next' to the while condition.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

# Example usage
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution = Solution()
    middle = solution.middleNode(head)
    print(middle.val)  # Output: 3
