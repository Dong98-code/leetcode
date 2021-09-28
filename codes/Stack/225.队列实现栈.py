from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = deque()
        self.s2 = deque()



    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.s2.append(x)
        while self.s1:
            self.s2.append(self.s1.popleft())
        self.s1,self.s2 = self.s2,self.s1


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.s1.pop()


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.s1[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.s1) == 0:
            return True
        else:
            return False

s = MyStack()
s.push(1)
s.push(2)
