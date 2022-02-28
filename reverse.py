# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Elizabeth Ager
# ASSIGNMENT:   Project 2: Stacks & Queues

import reverse_test
from Queue import Queue
from Stack import Stack

# Return a new queue in reverse order
# Hint: can use a stack to help


def reverse(og):
    q_new = Queue()
    stack_new = Stack()
    print("og", og)
    while (not og.is_empty()):
        stack_new.push(og.deq())
    while (not stack_new.is_empty()):
        q_new.enq(stack_new.pop())
    return q_new

def main():
    reverse(Queue([l for l in "Drew University"])).print()


# Don't run main on import
if name == "main":
    main()
