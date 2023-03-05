
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        h1, h2 = list1, list2
        merged_head  = ListNode(None)
        current = merged_head
        while h1 is not None and h2 is not None:
            if h1.val < h2.val:
                current.next = h1
                h1 = h1.next
            else:
                current.next = h2
                h2 = h2.next
            current = current.next
        if h1 is not None:
            current.next = h1
            
        if h2 is not None:
            current.next = h2

        current = current.next
        return current

        
if __name__ == "__main__":
    s = Solution()
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)   
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)   
    r = s.mergeTwoLists(list1, list2)
    current = r
    while current is not None:
        print(current.data)
    print(r)