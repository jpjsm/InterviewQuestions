#!/usr/bin/env python3

class Queue(object):
    def __init__(self):
        self.q = []

    def enqueue(self,v):
        self.q.append(v)

    def dequeue(self):
        if not self.q:
            raise Exception("Empty queue, nothing to dequeue")

        return self.q.pop(0)

    def size(self):
        return len(self.q)

    def isempty(self):
        return len(self.q) == 0

class Stack(object):
    def __init__(self):
        self.current = Queue()
        self.next = Queue()

    def push(self, v):
        self.current.enqueue(v)

    def pop(self):
        if not self.current:
            raise Exception("Empty stack, nothing to pop")

        while self.current.size() > 1:
            self.next.enqueue(self.current.dequeue())

        tmp = self.current
        self.current = self.next
        self.next = tmp

        return self.next.dequeue()

    def size(self):
        return self.current.size()

    def isempty(self):
        return self.current.size() == 0


if __name__ == "__main__":
    print("... starting ...")
    s = Stack()
    try:
        s.pop()
        print("Ooops, something went wrong here")
    except Exception as ex:
        print(ex)
    finally:
        pass

    for i in range(1,5):
        s.push(i)

    while not s.isempty():
        print(s.pop())
