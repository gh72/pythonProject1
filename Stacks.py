# LIFO : Last item we insert is the first item we take out


class Stack:

    def __init__(self):
        self.stack = []

    # insert item into the stack
    def push(self, data):
        self.stack.append(data)

    # remove and return the last item inserted (LIFO) // O(1)
    def pop(self):

        if self.stack_size() < 1:
            return -1

        data = self.stack[-1]
        del self.stack[-1]
        return data

    # peek:  it returns the last item without removing it // O(1)
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Size: %d" % stack.stack_size())
    print("Popped item: %d" % stack.pop())
    print("Size: %d" %stack.stack_size())
    print("Peek: %d" % stack.peek())
    print("Popped item: %d" % stack.pop())
    print("Popped item: %d" % stack.pop())
    print("Popped item: %d" % stack.pop())


