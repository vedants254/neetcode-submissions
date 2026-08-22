# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # no way to traverse from list end so lets find its index from root 
        N=0
        curr=head
        while curr:
            N+=1
            curr=curr.next
        #(N-n) is the index to be removed, N-n+1 th number from start
        curr=head
        removeIndex=N-n
        if removeIndex==0:
            return head.next
        for i in range(N-1):
            if (i+1)==removeIndex:
                curr.next=curr.next.next
                break
            curr=curr.next
        return head
        
        

