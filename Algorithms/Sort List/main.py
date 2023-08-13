class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sort_list(head):
    if not head or not head.next:
        return head

    prev, slow, fast = None, head, head

    while fast and fast.next:
        prev, slow, fast = slow, slow.next, fast.next.next

    prev.next = None
    left = sort_list(head)
    right = sort_list(slow)

    return merge(left, right)

def merge(left, right):
    dummy = ListNode()
    current = dummy

    while left and right:
        if left.val < right.val:
            current.next, left = left, left.next
        else:
            current.next, right = right, right.next
        current = current.next

    if left:
        current.next = left
    if right:
        current.next = right

    return dummy.next
