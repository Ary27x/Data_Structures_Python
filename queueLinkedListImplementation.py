import os
os.system('cls')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


q_length = 0


class Queue:
    def __init__(self):
        self.head = None

    def enQue(self, data_object):
        global q_length
        q_length += 1
        if self.head == None:
            self.head = data_object
            return
        current_data_object = self.head
        while (current_data_object.next != None):
            current_data_object = current_data_object.next
        current_data_object.next = data_object
        return

    def deQue(self):
        global q_length
        if (q_length == 0):
            print('Error: Queue Is Empty')
            input('Press Enter To Continue')
            return
        self.head = self.head.next
        q_length -= 1
        return

    def printQueue(self):
        if q_length == 0:
            print('The Queue Is Empty')
            return
        current_data_object = self.head
        print(current_data_object.data, end=' ')
        while (current_data_object.next != None):
            print('--', end=' ')
            current_data_object = current_data_object.next
            print(current_data_object.data, end=' ')
        print()


myQueue = Queue()


def home():
    os.system('cls')
    print('Current Queue:')
    myQueue.printQueue()
    print()
    print('Queue Lenght:')
    print(q_length)
    print()
    print('1) EnQue')
    print('2) DeQue')
    print()
    choice = input('Enter Controls: ')
    if choice == '1':
        data = input('Enter Queue Data: ')
        if data == '':
            data = '_Blank_'
        data = Node(data)
        myQueue.enQue(data)
    if choice == '2':
        myQueue.deQue()
    print()
    home()


home()
