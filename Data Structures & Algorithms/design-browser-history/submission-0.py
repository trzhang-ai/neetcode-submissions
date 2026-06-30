class ListNode:

  def __init__(self, val=None, prev=None, next=None):
    self.val = val
    self.prev = prev
    self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        node = ListNode(homepage)
        self.head = node
        self.tail = node
        self.history = [node]
        self.pointer = 0

    def visit(self, url: str) -> None:
        node = ListNode(url)
        tail = self.tail
        tail.next = node
        node.prev = tail
        self.tail = node
        self.history = self.history[: self.pointer + 1]
        self.history.append(node)
        self.pointer += 1

    def back(self, steps: int) -> str:
        idx = 0
        tail = self.tail
        steps = min(self.pointer, steps)
        while idx < steps:
          tail = tail.prev
          tail.next = None
          idx += 1
          self.pointer -= 1
        self.tail = tail
        return self.tail.val

    def forward(self, steps: int) -> str:
        nodes = self.history[self.pointer + 1: self.pointer + steps + 1]
        tail = self.tail
        for node in nodes:
           tail.next = node
           node.prev = tail
           tail = tail.next
           self.pointer += 1
        self.tail = tail
        return self.tail.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)