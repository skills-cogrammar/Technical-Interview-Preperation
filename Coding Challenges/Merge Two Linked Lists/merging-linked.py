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

    if (not list1):
        return list2
    
    if (not list2):
        return list1


    if (list1.val < list2.val):
        head = list1
        tail = list1
        list1 = list1.next
    else:
        head = list2
        tail = list2
        list2 = list2.next    



    while (list1 and list2):

        if list1.val < list2.val:
            tail.next = list1
            tail = tail.next

            next = tail.next
            tail.next = None
            list1 = next
            continue
        
        tail.next = list2
        tail = tail.next

        next = tail.next
        tail.next = None
        list2 = next

        
    if list1:
        tail.next = list1
    else:
        tail.next = list2   

    return head 


"""
list1 = [1] -> [2] -> [3] -> null
list2 = [3] -> [4] -> null

output = [1]
"""



def main():
    list1 = ListNode(100)
    list1.next = ListNode(102)
    list1.next.next = ListNode(103)

    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(400)

    output = get_merged(list1, list2)
    print(output)

main()