class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        lst = []
        current = self.head
        while current:
            lst.append(current.data)
            current = current.next
        print(lst)

    def fill_with(self, lst_):
        self.head = None
        for v in lst_:
            self.insert_at_end(v)

    def reverse(self):
        cur = self.head
        next2 = None
        while cur:
            next = cur.next
            cur.next = next2
            next2 = cur
            cur = next
        self.head = next2

    def insertion_sort(self):
        cur = self.head
        unsorted = cur.next
        sorted_head = cur
        sorted_head.next = None
        prev = cur
        while unsorted:
            if unsorted.data >= cur.data:
                if cur.next:
                    prev = cur
                    cur = cur.next
                else:
                    cur.next = unsorted
                    unsorted = unsorted.next
                    cur.next.next = None
                    cur = sorted_head
            else:
                if cur == sorted_head:
                    sorted_head = unsorted
                    unsorted_new = unsorted.next
                    sorted_head.next = prev
                else:
                    unsorted_new = unsorted.next
                    next_new = prev.next
                    prev.next = unsorted
                    unsorted.next = next_new
                cur = sorted_head
                unsorted = unsorted_new

        self.head = sorted_head

    def merge_sorted(self, second_llist):
        cur1 = self.head
        cur2 = second_llist.head
        self.head = None

        while cur1 and cur2:
            if cur1.data > cur2.data:
                self.insert_at_end(cur2.data)
                cur2 = cur2.next
            else:
                self.insert_at_end(cur1.data)
                cur1 = cur1.next
        while cur1:
            self.insert_at_end(cur1.data)
            cur1 = cur1.next
        while cur2:
            self.insert_at_end(cur2.data)
            cur1 = cur2.next


llist = LinkedList()
llist2 = LinkedList()

llist.fill_with([3, 5, 7, 1, 5])
print("Зв'язний список:")
llist.print_list()

llist.reverse()
print("Реверсний список:")
llist.print_list()

llist.insertion_sort()
print("Відсортований список:")
llist.print_list()


llist.fill_with([1, 5, 7, 10, 15])
llist2.fill_with([3, 5, 6, 7, 8, 11, 13])
print("Два відсортовані списки:")
llist.print_list()
llist2.print_list()

llist.merge_sorted(llist2)
print("Об'єднані списки:")
llist.print_list()
