class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

    def __str__(self) -> str:
        current = self 
        output = []

        while current:
            output.append(f" {current.val} ->")
            current = current.next
            

        return "".join(output).strip("->")

def get_merged(list1, list2):    
    output = ListNode(list1.val)
    head = output    
    list1 = list1.next

    while (list1 and list2):

        if list1.val < list2.val:
            output.next = ListNode(list1.val)
            output = output.next
            list1 = list1.next
            continue
        
        output.next = ListNode(list2.val)
        output = output.next
        list2 = list2.next

        
    if list1:
        output.next = list1
    else:
        output.next = list2   

    return head 


"""
list1 = [1] -> [2] -> [3] -> null
list2 = [3] -> [4] -> null

output = [1]
"""



def main():
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(3)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)

    output = get_merged(list1, list2)
    print(output)

main()