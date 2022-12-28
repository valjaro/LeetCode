# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):  
        self.head = None
    
    # insertion method for the linked list
    def insert(self, val):
        newNode = ListNode(val)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
                current.next = newNode
        else:
            self.head = newNode
    
    # print method for the linked list
    def printLL(self):
        current = self.head
        while(current):
            # print(current.val)
            current = current.next
        
    def reverseList(self):
        # initialize variables
        previous = None         # `previous` initially points to None
        current = self.head     # `current` points at the first element
        following = current.next    # `following` points at the second element

        # go till the last element of the list
        while current:
            current.next = previous # reverse the link
            previous = current      # move `previous` one step ahead
            current = following         # move `current` one step ahead
            if following:               # if this was not the last element
                following = following.next    # move `following` one step ahead

        list.head = previous

class Solution(object):
    
    # def reverse(self, list, len):
    #     for i in range(int(len / 2)):
    #         n = list[i]
    #         list[i] = list[len - i - 1]
    #         list[len - i - 1] = n
    #     return list
    
    # def len(self, list):
    #     i = 0
    #     for item in list.val:
    #         i+=1
    #     return i
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1.reverseList()
        n1 = int(''.join(map(str, l1)))
        n1 += int(''.join(map(str, l2)))
        r = [int(x) for x in str(n1)]
        return self.reverse(r, len(r))
        

if __name__ == "__main__":
    s = Solution()
    l1 = LinkedList()
    l2 = LinkedList()
    l1.insert(2)
    l1.insert(4)
    l1.insert(3)
    l2.insert(5)
    l2.insert(6)
    l2.insert(7)
    r = s.addTwoNumbers(l1,l2)
   
    print(r)