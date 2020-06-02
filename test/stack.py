
class OpStack(object):

    def __init__(self):
        self._data = []

    def push(self, op, val):
        obj = {'type': op,
               'val': val}
        self._data.append(obj)

    def pop(self):
        return self._data.pop()

    def empty(self):
        return len(self._data) == 0


stack = OpStack()

stack.push('a', 1)
stack.push('b', 2)

print(stack.pop())
print(stack.pop())
print(stack.empty())