# User function Template for python3

# Function to push an element in queue by using 2 stacks.
def Push(x, stack1, stack2):
    # O(1)
    stack1.append(x)

    # O(n)
    # while len(stack1) != 0:
    #     stack2.append(stack1.pop())
    # stack1.append(x)
    # while len(stack2) != 0:
    #     stack1.append(stack2.pop())


# Function to pop an element from queue by using 2 stacks.
def Pop(stack1, stack2):
    # O(1)
    #     if len(stack1) == 0:
    #         return -1
    #     return stack1.pop()

    # O(n)
    if len(stack1) == 0:
        return -1
    while len(stack1) != 1:
        stack2.append(stack1.pop())
    d = stack1.pop()
    while len(stack2) != 0:
        stack1.append(stack2.pop())
    return d


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry = int(input())
        qtyp_qry = list(map(int, input().strip().split()))

        i = 0
        stack1 = []
        stack2 = []
        while i < len(qtyp_qry):
            # print(i)
            if qtyp_qry[i] == 1:
                Push(qtyp_qry[i + 1], stack1, stack2)
                # print(i)
                i += 2
            else:
                print(Pop(stack1, stack2), end=' ')
                i += 1

        print()
# } Driver Code Ends
