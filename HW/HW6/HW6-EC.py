import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def seperate(self, head, k):
    count, node = 0, head
    while node and count < k:
        node = node.next
        count += 1
    if count < k: return head
    new_head, prev = reverse(head, head, count)
    head.next = seperate(new_head, new_head, k)
    return prev

def reverse(self, head, count):
    prev, curr, nxt = None, head, head
    while count > 0:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        count -= 1
    return (curr, prev)

def main(argv):
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(244)
    head.next.next.next = ListNode(7)
    head.next.next.next.next = ListNode(93)
    head.next.next.next.next.next = ListNode(105)
    k = int(argv[1])
    node = seperate(head, head, k)
    while (node != None):
        print('%d' % node.val, ' ', end = '')
        node = node.next
    print(' ')

if __name__ == '__main__':
    main(sys.argv)
