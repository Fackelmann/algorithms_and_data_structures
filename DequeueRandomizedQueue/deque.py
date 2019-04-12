class Node:
    def __init__(self,data,prev=None,next=None):
        self._data = data
        self._prev = prev
        self._next = next
        
class Deque:

    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def isEmpty(self) -> bool:
        if self._size == 0:
            return True
        else:
            return False
    
    def size(self) -> int:
        return self._size
    
    def addFirst(self, item):
        new_node = Node(item,None,None)
        if self._head == None:
            #New deque, intialize
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next=self._head
            self._head._prev = new_node
            self._head=new_node
        self._size+=1

    def addLast (self, item):
        new_node = Node(item,None,None)
        if self._head == None:
            #New deque, intialize
            self._head = new_node
            self._tail = new_node
        else:
            new_node._prev=self._tail
            self._tail._next = new_node
            self._tail=new_node
        self._size+=1
        

    def removeFirst(self):
        if self._head is None:
            raise IndexError('Deque is empty')
        result = self._head
        self._head = self._head._next
        self._size-=1
        #Set both to None if size is now zero. If not tail pointer is left hanging
        if self._size == 0:
            self._tail=self._head
        return(result._data)
        
    def removeLast(self):
        if self._tail is None:
            raise IndexError('Deque is empty')        
        result = self._tail
        self._tail = self._tail._prev
        self._size-=1
        #Set both to None if size is now zero. If not head pointer is left hanging
        if self._size == 0:
            self._head=self._tail
        return(result._data)

    def __iter__(self):
        return self

    def __next__(self):
        if self._size == 0:
            raise StopIteration
        else:
            next = self.removeFirst()
            return next


    def __str__(self):
        """
        Prints the current list in the form of a Python list
        """
        return str(self._head._data)        

if __name__ == "__main__":
    deque = Deque()
    deque.addFirst("one")
    #[1]
    print(deque.removeFirst())
    #[]
    deque.addFirst("two")
    #[2]
    deque.addFirst("three")
    #[3 2]
    deque.addLast("four")
    #[3 2 4]
    for i in deque:
        print(i)
    # 3 2 4
    #[]
    print(deque.size())
    #0
