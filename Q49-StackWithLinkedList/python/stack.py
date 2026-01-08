from link import Link


class Stack:
    def __init__(self):
        self.root = Link(None)

    def Pop(self):
        if self.root.Next == None:
            raise ValueError("Stack is empty, nothing to retrieve")

        v = self.root.Next.Value
        self.root.Next = self.root.Next.Next
        return v

    def Push(self, value):
        link = Link(value)
        link.Next = self.root.Next
        self.root.Next = link

    def IsEmpty(self):
        return self.root.Next is None


if __name__ == "__main__":
    stack = Stack()
    stack.Push(1)
    stack.Push(2)
    stack.Push(3)
    while not stack.IsEmpty():
        print(stack.Pop())
