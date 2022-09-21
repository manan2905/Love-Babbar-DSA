def reverse(s):
    # given s is a list of strings
    # inplace reverse
    for i in range(len(s) // 2):
        # swapping the first and last characters
        temp = s[i]
        s[i] = s[len(s) - i - 1]
        s[len(s) - i - 1] = temp
    return s


s = input()
li = [chr for chr in s]
print(reverse(li))
