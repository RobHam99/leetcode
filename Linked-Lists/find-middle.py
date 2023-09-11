def get_middle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow.val

# by the time fast pointer has reached the end of the list, slow is in the middle