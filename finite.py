from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count = 0
    node = lst.head
    while node is not None:
        count = count + 1
        node = node.next  
    return(count)    


def llprint(lst):
    """print a finite linked list"""
    node = lst.head
    while node is not None:
        print(node.val)
        node = node.next
        

if __name__ == "__main__":

    llist = LList()
    append(llist, Node(1))
    append(llist, Node(2))
    append(llist, Node(4))
    append(llist, Node(8))
    append(llist, Node(16))
    append(llist, Node(32))
    append(llist, Node(64))
    append(llist, Node(128))
    append(llist, Node(256))
    append(llist, Node(512))
    
    length(llist)
    print("The Length of the llist is:" ,length(llist))
    llprint(llist)
    from genfinite import lst
    print("The Length of lst is: ",length(lst))