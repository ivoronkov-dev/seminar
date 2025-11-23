class Node:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None


# {'item': data, nref: None, pref: None}


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = Node(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_node.pref = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def delete_element_by_value(self, x):
        # check empty list
        if self.start_node is None:
            print("The list has no element to delete")
            return
            # check if list is a single element
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
                return

        # folllowing the delete_at_start() method
        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return
            # list is nonsingle-element and desirable elem is not the first
        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p

    def push(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = Node(data)
        n.nref = new_node
        new_node.pref = n

    def pop(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            print(self.start_node.item)
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        print(n.item)
        n.pref.nref = None

    def top(self):
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        print(n.item)

    def size(self):
        k = 1
        n = self.start_node
        while n.nref is not None:
            n = n.nref
            k += 1
        print(k)

    def isempty(self, data):
        if self.start_node is None:
            return True
        else:
            return False

    def printstack(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref


new_linked_list = DoublyLinkedList()
new_linked_list.insert_in_emptylist(50)
new_linked_list.insert_at_start(10)
new_linked_list.insert_at_start(5)
new_linked_list.insert_at_start(18)

print("task 1")

a = [1, 2, 3, 4, 5, 6, 10, 22, 14, 2, 53, 4, 13, "tail"]
x = int(input("Какой элемент нужно найти:"))
t = 0
if a[0] == x:
    t = 1
k = 0
while True:
    k += 1
    if a[k] == x:
        t = 1
    if a[k] == "tail":
        break
if t == 1:
    print("True")
else:
    print("False")

print("task 2")
new_linked_list.reverse_linked_list()
new_linked_list.traverse_list()

print("task 3")
a = [1, 2, 3, 4, 5, 6, 10, 22, 14, 2, 53, 4, 13, "tail"]

n = 0
k = 0
while True:
    k += 1
    if a[k] == "tail":
        n = a[k - 1]
        break
k = 0
while True:
    print(a[k] - n)
    k += 1
    if a[k] == "tail":
        break

print("task 4")
new_linked_list.traverse_list()
print()
new_linked_list.delete_element_by_value(10)
print()
new_linked_list.traverse_list()

print("task 5")
a = ["head", 1, 2, 3, 4, 5, 6, 10, 1, 1, 22, 14, 2, 53, 4, 13, 47, "tail"]

p = 1
k = 2

while a[p + k - 2] != "tail":
    print(a[p] - a[-k])
    p += 1
    k += 1

print("task 6")

new_linked_list.push(25)
new_linked_list.pop()
new_linked_list.top()
new_linked_list.size()
print(new_linked_list.isempty())
new_linked_list.printstack()

# C деревьями подсказал deepseek

print("task 7")

a = eval(input())


def check(i, j):
    if i >= len(a) and j >= len(a):
        return True
    if i >= len(a) or j >= len(a):
        return False
    if a[i] != a[j]:
        return False
    return check(2 * i + 1, 2 * j + 2) and check(2 * i + 2, 2 * j + 1)


print(check(1, 2))

print("task 8")

print("Исходный список: [1, 2, 3, 4, 5, 6, 7]")
a = [1, 2, 3, 4, 5, 6, 7]
m_a = []
p = 0
f = 0

while f < len(a):
    k = f + (2 ** p)
    p_nodes = a[f:k]
    m_a.extend(p_nodes[::-1])
    f = k
    p += 1

print(m_a)

print("task 9")

a = eval(input())  # [1, 2, 3, 4, 5, 6, 7]
n = int(input())  # 5
gde = a.index(n)

ans = []

i = gde
while i > 0:
    tyt = (i - 1) // 2
    ans.append(a[tyt])
    i = tyt

print(ans)  # [2, 1]
