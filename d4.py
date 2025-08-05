
l1 = (1,2,3)  l2 = (7,8,9)
output -> 1->2->3->7->8->9

def mergeTwoLists(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
    
    
    dummy = Node(0)
    tail = dummy
    while l1 < l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
    
    
    def reverseList(head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    
    
    
    1->2->3->4->None
    
    def reverseList(head):
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
    4->3->2->1->None
    
    
    
    def _init_(left, val=0, right, self):
        self.left = left
        self.right = right
        self.val = val
        
        def isBalanced(root):
            def check(node):
                if not node:
                    return 0 # height = 0 for null nodes
                    
                left = check(node.left)
                if left == -1:
                    return -1
                
                right = check(node.right)
                if right == -1:
                    return -1
                    
                if abs(left - right) > 1:
                    return -1
                
                return max(left, right) + 1
                
        return check(root) != -1
            
    
    
    
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
