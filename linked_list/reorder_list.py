from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the list
        def findMiddle(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        middle = findMiddle(head)
        
        # Step 2: Reverse the second half of the list
        def reverseList(head):
            prev, current = None, head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        
        second_half = reverseList(middle.next)
        middle.next = None  # Split the list into two halves
        
        # Step 3: Merge the two halves
        def mergeLists(l1, l2):
            while l1 and l2:
                l1_next = l1.next
                l2_next = l2.next
                
                l1.next = l2
                if not l1_next:
                    break
                l2.next = l1_next
                
                l1 = l1_next
                l2 = l2_next
        
        mergeLists(head, second_half)

# Example usage
# Create a sample linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
solution = Solution()
solution.reorderList(head)
# The output list should be 1 -> 4 -> 2 -> 3

        