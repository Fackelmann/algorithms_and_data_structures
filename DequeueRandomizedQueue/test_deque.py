import pytest
import random
import os
from deque import *

def test_add_first_empty():
    deque = Deque()
    deque.addFirst(1)
    assert deque._size == 1 and \
        deque._head._data == 1 and \
        deque._head._next == None and \
        deque._head._prev == None and \
        deque._tail == deque._head


def test_add_last_empty():
    deque = Deque()
    deque.addLast(1)
    assert deque._size == 1 and \
        deque._tail._data == 1 and \
        deque._tail._next == None and \
        deque._tail._prev == None and \
        deque._tail == deque._head

def test_is_empty():
    deque = Deque()
    assert deque.isEmpty()

def test_remove_first():
    deque = Deque()
    deque.addFirst(1)
    deque.addLast(2)
    first = deque.removeFirst()
    assert first == 1 and \
        deque.size() == 1

def test_remove_last():
    deque = Deque()
    deque.addFirst(1)
    deque.addLast(2)
    last = deque.removeLast()
    assert last == 2 and \
        deque.size() == 1

def test_removeFirstException():
    deque = Deque()
    deque.addFirst(1)
    print(deque.removeLast())
    with pytest.raises(Exception) as e_info:
        deque.removeFirst()
    assert str(e_info.value) == 'Deque is empty'

def test_removeLastException():
    deque = Deque()
    deque.addLast(1)
    print(deque.removeFirst())
    with pytest.raises(Exception) as e_info:
        deque.removeLast()
    assert str(e_info.value) == 'Deque is empty'

def test_iterator():
    deque = Deque()
    deque.addFirst(1)
    deque.addFirst(2)
    deque.addFirst(3)
    deque.addLast(4)
    #[3 2 1 4]
    l = []
    for i in deque:
        l.append(i)
    #[3, 2, 1, 4]
    assert l == [3, 2, 1, 4] and deque.size() == 0


    
