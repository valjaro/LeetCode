# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # loop = len(head) - n
        # i = 0
        # while i < loop:
        #     if i + 1 == loop:
        #         index = head.index(head[i + 1])
        #         head[index - 1].next = head[index + 1].val
        #         head.pop(index)
        #     i += 1
        last_node = head
        if last_node.next == None: head = None
        l = 1
        while last_node.next is not None:
            last_node = last_node.next
            l += 1
        l, j = l - n, 0
        current_node = head
        if l == 0 and head: return head.next
        while j < l:
            if j + 1 == l:
                aux_node = current_node.next
                next_node = aux_node.next
                current_node.next = next_node
                break
            else:
                current_node = current_node.next
            j += 1    
        return head

if __name__ == "__main__":
    s = Solution()
    head = [1,2,3,4,5]
    n = 2
    l = len(head)
    new_head = []
    for i in range(l - 1):
        node = ListNode(head[i], head[i + 1])
        new_head.append(node)
    new_head.append(ListNode(head[l - 1]))
    r = s.removeNthFromEnd(new_head, n)
    print(r)