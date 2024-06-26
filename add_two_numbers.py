class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2: 
        val1  = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10 
        total = total % 10 

        current.next = ListNode(total)
        current = current.next 

        if l1: 
            l1 = l1.next
        if l2: 
            l2 = l2.next
    if carry > 0 :
        current.next = ListNode(carry)
        
    return dummy_head.next 


