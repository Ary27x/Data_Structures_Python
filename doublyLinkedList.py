import os
import copy
os.system('cls')
list_length = 0


class Node():
    def __init__(self, inp_data):
        self.data = inp_data
        self.next = None
        self.prev = None


class List():
    def __init__(self):
        self.head = None

    def atl(self, new_node):
        global list_length
        list_length += 1
        if self.head == None:
            self.head = new_node
            return
        else:
            current_node = self.head
            while (current_node.next != None):
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def getData(self, pos):
        pos = int(pos)
        if (pos > list_length or pos < 1):
            print("Index Out Of Range")
            return
        i = 1
        current_node = self.head
        while (i != pos):
            i += 1
            current_node = current_node.next
        return (current_node.data)

    def traverseList(self):
        global list_length
        if (list_length == 0):
            print('List Is Empty')
            input('Press Enter To Continue')
            return
        i = 1
        current_node = self.head
        while True:
            os.system('cls')
            print("Controls: 'a' -> Left ; 'd' -> Right ; 'p' -> Exit")
            print()
            self.printList()
            print("List Length: {}".format(list_length))
            print()
            print("Current Node: {}".format(current_node.data))
            print("Current Node Number: {}".format(i))
            ic = input("\nEnter Controls: ")
            if ic == 'a':
                if i == 1:
                    print('Cannot Go More Left!')
                    input('Press Enter To continue')
                else:
                    current_node = current_node.prev
                    i -= 1
            if ic == 'd':
                if i == list_length:
                    print('Cannot go more right')
                    input('press enter to continue')
                else:
                    current_node = current_node.next
                    i += 1
            if ic == 'p':
                return

    def printList(self):
        if (list_length == 0):
            print("The List Is Empty.")
            return
        else:
            print("<Head>", end=' ')
            current_node = self.head
            print(current_node.data, end=' ')
            while (current_node.next != None):
                current_node = current_node.next
                print("<-->", end=' ')
                print(current_node.data, end=' ')
            print("<Tail>")


mylist = List()


class Controller():
    def add(self, data):
        temp_obj = Node(data)
        mylist.atl(temp_obj)

    def printl(self):
        mylist.printList()

    def gd(self, pos):
        return mylist.getData(pos)

    def traverse(self):
        mylist.traverseList()


nc = Controller()


def home():
    os.system('cls')
    print("Current List: ")
    nc.printl()
    print()
    print("List Length: {}".format(list_length))
    print()
    print("1) Add Element (Tail Position)")
    print("2) Get Data")
    print("3) Left Right Traverse Through List")
    choice = input()
    if choice == "1":
        data_input = input("Enter Data To List: ")
        nc.add(data_input)
    if choice == "2":
        data_input = input("Enter The Position: ")
        x = nc.gd(data_input)
        print("Data Retrieved: {}".format(x))
        input("Press Enter to continue")
    if choice == "3":
        nc.traverse()
    home()


home()
