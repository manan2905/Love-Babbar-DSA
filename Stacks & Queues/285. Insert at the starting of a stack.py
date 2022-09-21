def func(s, data):
    # [1,2,3,4,5]
    if len(s) == 0:
        s.append(data)
        return
    d = s.pop()
    func(s, data)
    s.append(d)


s = [int(i) for i in input().split()]
data = int(input("Enter Data: "))
func(s, data)
print(s)
