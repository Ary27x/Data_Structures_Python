import os
import copy
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
        return


class Controller:
    def atl(self, data):
        new_node = Node(data)
        mainList.add(new_node)

    def llen(self):
        print(list_length)

    def display(self):
        mainList.printList()

    def atlh(self, data):
        new_node = Node(data)
        mainList.add_new_head(new_node)

    def atlb(self, data, pos):
        global list_length
        if (pos <= 0 or pos > list_length + 1):
            print("Invalid Position: List Out Of Bounds: llen({}),pos({})".format(
                list_length, pos))
            input("Press Enter To Continue \n")
            return
        new_node = Node(data)
        mainList.add_between(new_node, pos)

    def dn(self, pos):
        if (pos < 1 or pos > list_length):
            print("Invalid Position: List Out Of Bounds: llen({}),pos({})".format(
                list_length, pos))
            input("Press Enter To Continue \n")
            return
        mainList.delete_node(pos)

    def gd(self, pos):
        if (list_length == 0):
            print("Error: The list is empty")
            input("Press enter to continue")
            return
        if (pos < 1 or pos > list_length):
            print("Error: List Index Out Of Range: ({})".format(pos))
            input("Press Enter To Continue")
            return
        mainList.getData(pos)

    def cd(self, data, pos):
        if (list_length == 0):
            print("Error: The list is empty")
            input("Press enter to continue")
            return
        if (pos < 1 or pos > list_length):
            print("Error: List Index Out Of Range: ({})".format(pos))
            input("Press Enter To Continue")
            return
        mainList.changeData(data, pos)

    def dh(self):
        mainList.delete_header()


mainList = List()
nc = Controller()


def main_controller():
    os.system('cls')
    nc.display()
    print()
    print("List Length: {}".format(list_length))
    print()
    print("1) Add Element (Tail Position)")
    print("2) Add Element (Positioned)")
    print("3) Add Header")
    print("4) Delete Header")
    print("5) Delete Element (Positioned)")
    print("6) Get Data (Positioned)")
    print("7) Change Data (Positioned)")

    print()
    choice = input()
    if choice == "1":
        data = input("Enter Data: ")
        nc.atl(data)
        main_controller()
    if choice == "2":
        pos = int(input("Enter Position: "))
        data = input("Enter Data: ")

        nc.atlb(data, pos)
        main_controller()
    if choice == "3":
        data = input("Enter Data: ")
        nc.atlh(data)
        main_controller()
    if choice == "4":
        nc.dh()
        main_controller()
    if choice == "5":
        pos = int(input("Enter Position: "))
        nc.dn(pos)
        main_controller()
    if choice == "6":
        pos = int(input("Enter Position: "))
        nc.gd(pos)
        main_controller()
    if choice == "7":
        pos = input("Enter Position: ")
        pos = int(pos)
        data = input("Enter The New Data: ")
        nc.cd(data, pos)
        main_controller()


main_controller()
