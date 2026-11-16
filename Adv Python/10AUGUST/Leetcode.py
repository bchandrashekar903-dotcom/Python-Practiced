'''876. Middle of the Linked List 
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
def middleNode(head):
        size = 0
        curr = head
        while curr:
            size+=1
            curr = curr.next
        mid = (size)//2
        curr = head
        for i in range(mid):
            curr = curr.next
        return curr
#
'''Booyen Moor Algorithm 
Middle Node Linked list'''
def middleNode(self, head:  Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
middle


'''206 Reverse the linked list '''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        prev = None
        curr = head
        while curr:
            next_node = curr.next   # Store next node before breaking the link
            curr.next = prev        # Reverse current node's pointer
            prev = curr             # Move prev to current node
            curr = next_node        # Move to next node
        return prev.data

# Example setup: Creating Linked List 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s = Solution()
reversed_head = s.reverseList(head)

# Displaying reversed list values
curr = reversed_head
result = []
while curr:
    result.append(curr.val)
    curr = curr.next
print(result)  # Output: [5, 4, 3, 2, 1]