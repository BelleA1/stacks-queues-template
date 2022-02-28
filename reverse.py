# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Elizabeth Ager
# ASSIGNMENT:   Project 2: Stacks & Queues
from Queue import Queue
from Stack import Stack

def reverse(q_orig):

    q_new = Queue()
    stack_new = Stack()
    print("original queue", q_orig)
    while (not q_orig.is_empty()):
        stack_new.push(q_orig.deq())
    while (not stack_new.is_empty()):
        q_new.enq(stack_new.pop())
    return q_new

def main():
    reverse(Queue([l for l in "Welcome to Drew University"])).print()
    reverse(Queue([l for l in "Goodbye!"])).print()
    reverse(Queue(list(range(1, 10)))).print()
    reverse(Queue([])).print()
    reverse(Queue([0])).print()
    reverse(Queue(list(range(0, 150, 8)))).print()
    reverse(Queue(list(range(1, -15, -5)))).print()
    reverse(Queue([int(i) for i in "2146574i879976"])).print()
    reverse(Queue(["b"])).print()
    reverse(Queue([-7])).print()
    reverse(Queue(list(range(-7, 8)))).print()

# Don't run main on import
if __name__ == "__main__":
    main()
