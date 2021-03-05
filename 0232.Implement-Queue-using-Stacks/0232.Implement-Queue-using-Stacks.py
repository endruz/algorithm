class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 初始化两个栈 instack 和 outstack，分别用来处理队列的入队和出队的操作
        self.instack = []
        self.outstack = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # 入队时，将数据入栈 instack
        self.instack.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # 出队时，若 outstack 为空，则将 instack 中的数据依次出栈并入栈 outstack
        # 此时 outstack 的栈尾数据即队列开头数据，pop 栈 outstack 即为 pop 队列
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        # 与 pop 操作同理
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]


    def empty(self) -> bool:
        # 两个栈 instack 和 outstack 同时为空时，队列为空
        """
        Returns whether the queue is empty.
        """
        return (not self.instack) and (not self.outstack)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()