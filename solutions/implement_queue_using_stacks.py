# https://leetcode.com/problems/implement-queue-using-stacks/description/


class MyQueue:
    def __init__(self):
        self.back = []
        self.front = []

    def push(self, x: int) -> None:
        self.back.append(x)

    def pop(self) -> int:
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
        return self.front.pop()

    def peek(self) -> int:
        if not self.front:
            while self.back:
                self.front.append(self.back.pop())
        return self.front[-1]

    def empty(self) -> bool:
        return not self.back and not self.front


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
