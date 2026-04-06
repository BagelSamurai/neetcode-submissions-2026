class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Start both at the head
        slow = head
        fast = head
        
        # Ensure fast and fast.next exist so we can move 2 steps
        while fast and fast.next:
            slow = slow.next          # moves 1 step
            fast = fast.next.next     # moves 2 steps
            
            # Check if the objects are the same node
            if slow == fast:
                return True
                
        return False