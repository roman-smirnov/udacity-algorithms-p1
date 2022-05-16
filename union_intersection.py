""" Union and Intersection """


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def __iter__(self):
        return LinkedListIterator(self)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def extend(self, other_list):
        if self.head is None:
            self.head = other_list.head
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = other_list.head

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


class LinkedListIterator:
    def __init__(self, linked_list):
        self.linked_list = linked_list
        self.current = linked_list.head

    def __next__(self):
        """'Returns the next value of the list """
        if not self.current:
            raise StopIteration
        node = self.current
        self.current = node.next
        return node.value


def union(llist_1, llist_2):
    # NOTE: problem definition doesn't require the union list elements to have unique values
    union_list = LinkedList()
    for v1 in llist_1:
        union_list.append(v1)
    for v2 in llist_2:
        union_list.append(v2)
    return union_list


def intersection(llist_1, llist_2):
    # NOTE: problem definition doesn't require the intersection list elements to have unique values
    intersection_list = LinkedList()
    for v1 in llist_1:
        for v2 in llist_2:
            if v1 == v2:
                intersection_list.append(v1)
    return intersection_list


def test1():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


def test2():
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
    element_2 = [1, 7, 8, 9, 11, 21, 1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print(union(linked_list_3, linked_list_4))
    print(intersection(linked_list_3, linked_list_4))


def test3():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


def test4():
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in range(1000):
        linked_list_1.append(i)
        linked_list_2.append(i)

    print(union(linked_list_1, linked_list_2))
    print(intersection(linked_list_1, linked_list_2))


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
