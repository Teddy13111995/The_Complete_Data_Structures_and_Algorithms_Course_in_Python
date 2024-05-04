class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def isFULL(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False

    def push(self, target):
        if not self.isFULL():
            self.list.append(target)
        else:
            return "Stack is full"

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None
