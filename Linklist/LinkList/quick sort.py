from LinkedList import LinkList, Node #imported from LinkList.py module file

class Quicksort:
    def sortList(self, head: Node) -> Node:
            def partition(start, end):
                node = start.next.next
                pivotPrev = start.next
                pivotPrev.next = end
                pivotPost = pivotPrev
                while node != end:
                    temp = node.next
                    if node.data > pivotPrev.data:
                        node.next = pivotPost.next
                        pivotPost.next = node
                    elif node.data < pivotPrev.data:
                        node.next = start.next
                        start.next = node
                    else:
                        node.next = pivotPost.next
                        pivotPost.next = node
                        pivotPost = pivotPost.next
                    node = temp
                return [pivotPrev, pivotPost]
            
            def quicksort(start, end):
                if start.next != end:
                    prev, post = partition(start, end)
                    quicksort(start, prev)
                    quicksort(post, end)

            newHead = Node(0)
            newHead.next = head
            quicksort(newHead, None)
            return newHead.next
            
first = Node(4)
sec = Node(2)
third = Node(5)
fourth = Node(1)

first.next = sec
sec.next = third
third.next = fourth


obj = LinkList()
obj.head = first

llist = Quicksort()
obj.head = llist.sortList(obj.head)
obj.printlist()