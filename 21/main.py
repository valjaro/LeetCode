# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
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
        dummy = cur = ListNode(0)
        while list1 and list2:
            print(list1)
            print(list2)
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            print("current:")
            print(cur)
            print("dummy:")
            print(dummy)
            print("/////////////////")
            cur = cur.next
        cur.next = list1 or list2
        return dummy.next 

if __name__ == "__main__":
    s = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]
    r = s.mergeTwoLists(list1, list2)
    print(r)