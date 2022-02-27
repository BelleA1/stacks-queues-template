i# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Elizabeth Ager
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
from Stack import Stack

 def reverse(q_orig):
        q_new = Queue()
    stack_new = Stack()
    print("orig", orig)
    while (not orig.is_empty()):
        stack_new.push(orig.deq())
    while (not stack_new.is_empty()):
        q_new.enq(stack_new.pop())
    return (q_new)
# Return a new queue in reverse order
# Hint: can use a stack to help
def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()

