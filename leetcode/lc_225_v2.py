class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q=collections.deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q =collections.deque([x])+self.q

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q
