import sys
import os
import copy
os.system('cls')


class queueType:
    def __init__(self, data_object):
        self.content = data_object
        self.next = None


counter = 0

tree_object = None


class Queue:
    def __init__(self):
        self.head = None

    def add_first(self, tree_object):
        if not(tree_object):
            return
        tree_root = tree_object.root
        tree_root = queueType(tree_root)
        self.head = tree_root
        current_node = self.head
        if (not(tree_root.content.left)):
            current_node.next = queueType('endLevel')
            return
        current_node.next = queueType(tree_root.content.left)
        if (not(tree_root.content.right)):
            current_node.next.next = queueType('endLevel')
            return
        current_node.next.next = queueType(tree_root.content.right)
        current_node.next.next.next = queueType('endLevel')

    def remove(self):
        global counter

        if counter == 0:
            print(self.head.content.data)
            print()
            if (not (self.head.next)):
                return
            self.head = self.head.next
            counter += 1
            self.remove()
            return
        if self.head.content == 'endLevel':
            print()
            print()
            if not(self.head.next):
                return
            self.add('endLevel')

            self.head = self.head.next

        print(self.head.content.data, end=' ')

        if (self.head.content.left):
            self.add(self.head.content.left)
        if (self.head.content.right):
            self.add(self.head.content.right)
        if not(self.head.next):
            return
        self.head = self.head.next
        self.remove()

    def add(self, data):
        current_node = self.head
        while (current_node.next != None):
            current_node = current_node.next
        current_node.next = queueType(data)


class TreeData:
    def __init__(self, data):
        self.data = int(data)
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data_object):
        if self.root == None:
            self.root = data_object
            return
        current_tree_object = self.root
        while True:
            if (data_object.data == current_tree_object.data):

                return
            if data_object.data > current_tree_object.data:
                if current_tree_object.right == None:
                    current_tree_object.right = data_object

                    return
                else:
                    current_tree_object = current_tree_object.right
            else:
                if current_tree_object.left == None:
                    current_tree_object.left = data_object

                    return
                else:
                    current_tree_object = current_tree_object.left


def printTreeDLR(tree_root_object):
    if not tree_root_object.data:
        return

    print(tree_root_object.data)

    if (tree_root_object.left):
        printTreeDLR(tree_root_object.left)
    if (tree_root_object.right):
        printTreeDLR(tree_root_object.right)


temp = 0
myTree = Tree()
a = TreeData(int(input('Enter Root Value: ')))
b = int(input('Enter Node Value (1): '))
c = int(input('Enter Node Value (2):'))
if (b > c):
    temp = b
    b = c
    c = temp
b = TreeData(b)
c = TreeData(c)

myTree.add(a)
myTree.add(b)
myTree.add(c)


def home():
    global counter
    counter = 0
    os.system('cls')
    print('Current Tree:')
    x = Queue()
    x.add_first(myTree)
    x.remove()
    del x
    counter = 0
    print()
    print('1) Add Data')
    print('2) Traverse Tree (DLR)')

    print()
    choice = input('Enter Controls: ')
    if choice == '1':
        print()
        data_input = input('Enter The Data: ')
        if (data_input != ''):
            data_input = int(data_input)
            tree_data_object = TreeData(data_input)
            myTree.add(tree_data_object)
            q = Queue()
            q.add_first(myTree)
            q.remove()
            del q
    if choice == '2':
        print()
        printTreeDLR(myTree.root)
        print()
        input('Press Enter To Continue')
    home()


home()
