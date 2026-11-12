# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #create a varaiable called dummy that is assigned the throw away node at the start 
        tail = dummy #tail vaiable that also starts where dummy is, but will move to keep track of end of LL

        while list1 and list2: #keeps looping as long as both linked lists have a node in them 
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        
        return dummy.next







    
    
        