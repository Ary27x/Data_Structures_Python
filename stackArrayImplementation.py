import os
os.system('cls')


class Stack():
    def __init__(self, limit):

        self.stack = []
        self.limit = limit

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def info(self):
        print()
        print('Stack Capacity: {}'.format(self.limit))
        print('Stack Current Size: {}'.format(len(self.stack)))
        print('Stack Empty: {}'.format(self.isEmpty()))
        print()
        input('Press Enter To Continue')

    def baseValue(self):
        if (len(self.stack) == 0):
            return False
        return self.stack[0]

    def topValue(self):
        if len(self.stack) == 0:
            return False
        return (self.stack[len(self.stack) - 1])

    def push(self):
        if len(self.stack) == self.limit:
            return False
        data = input('Enter Data: ')
        if data == '':
            self.stack.append('_Blank_')
            return (True)
        self.stack.append(data)
        return (True)

    def pop(self):
        if len(self.stack) == 0:
            return False
        self.stack = self.stack[:-1]
        return True

    def length(self):
        return (len(self.stack))

    def display(self):
        i = self.limit - 1
        while (i >= 0):
            if i > len(self.stack) - 1:
                print('_Empty_')
                i -= 1
            else:
                print(self.stack[i])
                i -= 1


size = input('Enter Stack Size: ')
if (size == '' or size == '0'):
    size = 5
else:
    size = int(size)

myStack = Stack(size)


def home():
    os.system('cls')
    print('Current Stack:')
    myStack.display()
    print()
    print('1) Push Data')
    print('2) Pop Data')
    print('3) Stack Current Size')
    print('4) Stack Top Value')
    print('5) Stack Base Value')
    print('6) Stack Memory Information')
    print()
    choice = input('Enter Control: ')
    if choice == '1':
        print()
        if myStack.push():
            print('Data SuccessFully Pushed Into The Stack')
        else:
            print('Error: Stack Overflow')
        print()
        input('Press Enter To Continue')
    if choice == '2':
        print()
        if myStack.pop():
            print('Data SuccessFully Popped Out Of The Stack')
        else:
            print('Error: Stack Underflow')
        print()
        input('Press Enter To Continue')
    if choice == '3':
        print()
        print('Size Of The Stack: {}'.format(myStack.length()))
        input('Press Enter To Continue')

    if choice == '4':
        print()
        returned = myStack.topValue()
        if returned:
            print('Top Value Of Stack: {}'.format(returned))
        else:
            print('Error: Stack Is Empty')
        print()
        input('Press Enter To Continue')
    if choice == '5':
        print()
        returned = myStack.baseValue()
        if returned:
            print('Base Value Of Stack: {}'.format(returned))
        else:
            print('Error: Stack Is Empty')
        print()
        input('Press Enter To Continue')
    if choice == '6':
        myStack.info()
    home()


home()
