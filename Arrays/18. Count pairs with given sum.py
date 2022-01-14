def find_number_of_pairs(arr, k):
    # naive approach is to use 2 loops : O(n2)
    count = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                count += 1
    return count


def small_func(n):
    c = 0
    for i in range(1, n):
        c += i
    return c


def find_number_of_pairs_hashmap(arr, k):
    d = {}
    count = 0
    for ele in arr:
        d[ele] = d.get(ele, 0) + 1

    # we can either loop through the array or the dictionary to find the relevant pairs
    for key in d:
        comp = k - key
        if key == comp:
            count += small_func(d[key])
        elif comp in d:
            count += d[comp] * d[key]
            d[comp] = 0
            d[key] = 0
    return count


arr = [int(i) for i in input().split()]
k = int(input())
print(find_number_of_pairs_hashmap(arr, k))
