'''
A linked list is collection of nodes , each of which contains nodes and at least one reference or link to another node.
'''
class _ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self._size = 0

    def __len__(self):
        return self._size

    def insert_head(self, head, data):
        new_node = _ListNode(data)
        if head is None:
            head = new_node
            self._size += 1
        else:
            new_node.next = head
            head = new_node
            self._size += 1
        return head


    def insert_tail(self, head, data):
        new_node = _ListNode(data)
        if head is None:
            head = new_node
            self._size += 1
        elif head.next == None:
            head.next = new_node
            self._size += 1
        else:
            current_node = head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            self._size += 1
        return head


    def walk(self, head):
        if head==None:
            print("head is none")
            return None
        else:
            current_node = head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next

    def remove(self, head, target):
        prev_node = None
        cur_node = head

        while cur_node is not None and cur_node.data != target:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is not None:
            if cur_node is head:
                head = cur_node.next
                self._size -= 1
            else:
                prev_node.next = cur_node.next
                self._size -= 1
            return head

if __name__=="__main__":
    ll = LinkedList()
    head = None
    for i in range(5):
        data = i
        head = ll.insert_tail(head, data)
    ll.walk(head)
    print()
    print(len(ll))

    for i in range(10, 14):
        data = i
        head = ll.insert_head(head, data)

    ll.walk(head)
    print()
    print(len(ll))
    head = ll.remove(head, 13)
    head = ll.remove(head, 4)
    head = ll.remove(head, 10)
    print()
    ll.walk(head)
    print()
    print(len(ll))
    