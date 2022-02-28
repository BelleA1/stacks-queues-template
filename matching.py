# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Elizabeth Ager
# ASSIGNMENT:   Project 2: Stacks & Queues
def matcher(expr):
  stack = []
  for c in expr:
    if c in '[({':
      stack.append(c)
    elif c in '])}':
      if len(stack) == 0:
        return False
      if '])}'.index(c) != '[({'.index(stack.pop()):
        return False
  return len(stack) == 0

def main():
    print("matcher: ", matcher("a[b]{"))

# Don't run main on import
if __name__ == "__main__":
    main()
