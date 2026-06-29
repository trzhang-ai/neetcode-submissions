class ListNode:

  def __init__(self, val=None, prev=None, next=None):
    self.val = val
    self.prev = prev
    self.next = next


class MyLinkedList:


    def __init__(self):
      self.head = None
      self.tail = None
      self.size = 0


    def get(self, index: int) -> int:
      if self.size == 0:
        return -1
      if 0 <= index <= self.size - 1:
        if index < self.size // 2:
          head = self.head
          idx = 0
          while head:
            if idx == index:
              break
            else:
              head = head.next
              idx += 1
          return head.val
        else:
          tail = self.tail
          idx = self.size - 1
          while tail:
            if idx == index:
              break
            else:
              tail = tail.prev
              idx -= 1
          return tail.val
      else:
        return -1
      

    def addAtHead(self, val: int) -> None:
      node = ListNode(val=val)
      if self.size == 0:
        self.head = node
        self.tail = node
      else:
        head = self.head
        node.next = head
        head.prev = node
        self.head = node
      self.size += 1


    def addAtTail(self, val: int) -> None:
      node = ListNode(val)
      if self.size == 0:
        self.head = node
        self.tail = node
      else:
        tail = self.tail
        node.prev = tail
        tail.next = node
        self.tail = node
      self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
      if index == 0:
        self.addAtHead(val)
      elif index == self.size:
        self.addAtTail(val)
      elif index > self.size:
        return
      else:
        node = ListNode(val)
        if index < self.size // 2: 
          head = self.head
          idx = 0
          while head:
            idx += 1
            head = head.next
            if idx == index:
              break
          prev = head.prev
          next = head
          node.prev = prev
          node.next = next
          prev.next = node
          next.prev = node
        else:                          
          tail = self.tail # [0, 1, 2, 3, 4, 5]
          idx = self.size
          while tail:
            idx -= 1
            tail = tail.prev
            if idx == index:
              break
          next = tail.next
          prev = tail
          node.prev = prev
          node.next = next
          next.prev = node
          prev.next = node
        self.size += 1

      
    def deleteAtIndex(self, index: int) -> None:
      if self.size == 0:
        return
      if index == 0:
        head = self.head
        next = head.next
        next.prev = None
        self.head = next
      elif index == self.size - 1:
        tail = self.tail
        prev = tail.prev
        prev.next = None
        self.tail = prev
      elif 0 < index < self.size - 1:
        if index < self.size // 2:
          head = self.head
          idx = 0
          while head:
            idx += 1
            head = head.next
            if idx == index:
              break
          prev = head.prev
          next = head.next
          prev.next = next
          next.prev = prev
        else:
          tail = self.tail
          idx = self.size - 1
          while tail:
            idx -= 1
            tail = tail.prev
            if idx == index:
              break
          prev = tail.prev
          next = tail.next
          prev.next = next
          next.prev = prev
      else:
        return
      self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)