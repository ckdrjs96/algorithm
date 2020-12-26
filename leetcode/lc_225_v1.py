class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q=[]
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q =[x]+self.q

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        a=self.q[0]
        del self.q[0]
        return a

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
