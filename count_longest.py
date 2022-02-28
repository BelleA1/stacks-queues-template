# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Elizabeth Ager
# ASSIGNMENT:   Project 2: Stacks & Queues
from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty

def count_longest(queue):
    countMax = 0
    countCurrent = 1

    while(not queue.is_empty()):
        elementNext = queue.deq()
        elementCurrent = queue.front()

        if elementNext == elementCurrent:
            countCurrent += 1
        elif elementNext != elementCurrent:
            countCurrent = 1
        if countCurrent > countMax:
            countMax = countCurrent
    return countMax

def main():
    print(count_longest(Queue([l for l in "weeeeeeewooooooo"])))
    print(count_longest(Queue([l for l in "goodbye"])))
    print(count_longest(Queue([l for l in "z" * 17])))
    print(count_longest(Queue([l for l in "scoop"])))
    print(count_longest(Queue([l for l in "shoooooop"])))
    print(count_longest(Queue([l for l in "shoooopeeeeee"])))
    print(count_longest(Queue([l for l in "shooooooopeeeeee"])))
    print(count_longest(Queue([ ])))
    print(count_longest(Queue([l for l in "z"])))
    print(count_longest(Queue([l for l in "+__--___----__--_+"])))


if __name__ == "__main__":
    main()
