class Stack:
    def __init__(self):
        # creating an empty list
        self.list = []

    # def __str__(self):
    #     values = self.list.reverse()
    #     values = [str(x) for x in self.list]
    #
    #     return '\n'.join(values)

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]

        return '\n'.join(values)

    # isEmpty()
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # push
    def push(self, value):
        self.list.append(value)
        return "the element has been successfully implemented"

    # pop
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.list.pop()

    # peek
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.list[len(self.list) - 1]

    # delete entire stack
    def delete(self):
        self.list = None


custom_stack = Stack()

print(custom_stack.isEmpty())

custom_stack.push(1)
custom_stack.push(2)
custom_stack.push(3)

print(custom_stack)
