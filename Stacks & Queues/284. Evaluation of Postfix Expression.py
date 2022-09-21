# User function Template for python3

class Solution:

    # Function to evaluate a postfix expression.
    def evaluatePostfix(self, string):
        # code here
        s = []
        for char in string:
            if char in "*/+-":
                s1, s2 = int(s.pop()), int(s.pop())
                if char == "+":
                    s.append(s1 + s2)
                elif char == "-":
                    s.append(s2 - s1)
                elif char == "*":
                    s.append(s1 * s2)
                else:
                    s.append(s2 // s1)
            else:
                s.append(char)
        return s[0]


# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        S = input()
        obj = Solution()
        print('{0:g}'.format(float(obj.evaluatePostfix(S))))
# } Driver Code Ends
