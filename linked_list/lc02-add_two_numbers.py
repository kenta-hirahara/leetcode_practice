# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    curr1, curr2 = l1, l2
    q = 0
    mod_list=[]
    while curr1 or curr2 or q:
        sum_nodes = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + q
        q, mod = divmod(sum_nodes, 10)
        mod_list.append(mod)
        curr1 = curr1.next if curr1 else None
        curr2 = curr2.next if curr2 else None
    head = None
    for mod_rev in reversed(mod_list):
        head = ListNode(mod_rev, head)
    return head

def list2LinkedList(l: list[int]) -> ListNode:
    head = None
    for node_val in reversed(l):
        head = ListNode(node_val, head)
    return head

def linkedList2List(head: ListNode) -> list:
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l

def main():
    l1 = list2LinkedList([2,4,3])
    l2 = list2LinkedList([5,6,4])
    head = addTwoNumbers(l1, l2)
    print(linkedList2List(head))

if __name__ == "__main__":
    main()