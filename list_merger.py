import os
import copy
os.system("cls")
os.system("cls")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


list_length = 0


class List:
    def __init__(self):
        self.head = None

    def add_new_head(self, new_node):
        global list_length
        current_head = self.head
        self.head = new_node
        self.head.next = current_head
        del current_head
        list_length += 1

    def add(self, new_node):
        global list_length
        if self.head == None:
            self.head = new_node
            list_length += 1
            return
        current_node = self.head
        while True:
            if current_node.next == None:
                break
            current_node = current_node.next
        current_node.next = new_node
        list_length += 1

    def add_between(self, new_node, pos):
        global list_length
        if pos == 1:
            self.add_new_head(new_node)
            return
        if pos == list_length + 1:
            self.add(new_node)
            return
        current_node = self.head
        i = 1
        while i < pos-1:
            i += 1
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node
        del current_node
        list_length += 1

    def changeData(self, data, pos):
        current_node = self.head
        i = 1
        while i != pos:
            current_node = current_node.next
            i += 1
        current_node.data = data
        print("Data Successfully Changed At {} To {}".format(pos, data))
        input("Press Enter To Conntinue")

    def getData(self, pos):
        current_head = self.head
        i = 1
        while i != pos:
            current_head = current_head.next
            i += 1
        print("Data Retrieved: {}".format(current_head.data))
        input("Press Enter To Continue")

    def delete_header(self):
        global list_length
        if list_length == 0:
            print("Error: List Is Empty, Cannot delete Header")
            input("Press Enter To Continue \n")
            return
        elif list_length == 1:
            self.head = None
            list_length -= 1
            return
        else:
            self.head = self.head.next
            list_length -= 1
            return

    def delete_node(self, pos):
        global list_length
        if pos == 1:
            self.delete_header()
            return
        else:
            i = 1
            current_node = self.head
            while (i < pos - 1):
                current_node = current_node.next
                i += 1
            if (pos == list_length):
                current_node.next = None
            else:
                current_node.next = current_node.next.next
            list_length -= 1

    def printList(self):
        current_node = self.head
        if current_node == None:
            print("The list is empty")

            return

        print("<Head>", end=' ')
        while True:
            print(current_node.data, end=' ')
            if current_node.next == None:
                print("<Tail>")
                break
            current_node = current_node.next
            print("->", end=' ')
        print ()
        return


def min_returner(list_obj):
    list_obj = list_obj.head
    if list_obj == None:
        return None, None
    min_data = int(list_obj.data)
    i = 1
    while True:
        temp = int(list_obj.data)
        if temp <= int(min_data):
            min_pos = i
            min_data = int(temp)
        i += 1
        if list_obj.next == None:
            break
        else:
            list_obj = list_obj.next
    return min_data, min_pos


def mergeList(fl, sl):
    firstList = copy.deepcopy(fl)
    secondList = copy.deepcopy(sl)

    mergedList = List()
    while True:
        list_one_min, fpos = min_returner(firstList)
        list_two_min, spos = min_returner(secondList)
        if (list_one_min == None and list_two_min == None):
            break
        if (list_one_min == None and list_two_min != None):
            mergedList.add(Node(list_two_min))
            secondList.delete_node(spos)
        elif (list_one_min != None and list_two_min == None):
            mergedList.add(Node(list_one_min))
            firstList.delete_node(fpos)
        elif (list_one_min < list_two_min):
            mergedList.add(Node(list_one_min))
            firstList.delete_node(fpos)
        else:
            mergedList.add(Node(list_two_min))
            secondList.delete_node(spos)
    return mergedList


# Some Dummy Data
list1 = List()
obj01 = Node(1)
obj02 = Node(3)
obj03 = Node(5)
list1.add(obj01)
list1.add(obj02)
list1.add(obj03)
list2 = List()
obj11 = Node(2)
obj12 = Node(4)
obj13 = Node(6)
obj14 = Node(8)
list2.add(obj11)
list2.add(obj12)
list2.add(obj13)
list2.add(obj14)

# Create A Merged List For The Dummy Data
list_merged = mergeList(list1, list2)


def display_lists():
    print("List 1:")
    list1.printList()
    print()
    print("List 2:")
    list2.printList()
    print()
    list_merged = mergeList(list1, list2)
    print("Merged List:")
    list_merged.printList()


display_lists()
print()


def continue_f():
    print("1) Add To List 1 ")
    print("2) Add To List 2 ")
    print ()
    choice = input('Enter Controls: ')
    if choice == "1":
        data = input("Enter The Number: ")
        list1.add(Node(int(data)))
        os.system('cls')

        display_lists()
    if choice == "2":
        data = input("Enter The Number: ")
        list2.add(Node(int(data)))
        os.system('cls')

        display_lists()
    continue_f()


continue_f()
