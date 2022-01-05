# given 2 arrays are sorted
def union_intersection(arr1, arr2):
    intersection = []
    union = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if len(union) == 0:
                union.append(arr1[i])
            else:
                if union[-1] != arr1[i]:
                    union.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if len(union) == 0:
                union.append(arr2[j])
            else:
                if union[-1] != arr2[j]:
                    union.append(arr2[j])
            j += 1
        else:
            if len(union) == 0:
                union.append(arr1[i])
            else:
                if union[-1] != arr1[i]:
                    union.append(arr1[i])

            if len(intersection) == 0:
                intersection.append(arr1[i])
            else:
                if intersection[-1] != arr1[i]:
                    intersection.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    while j < len(arr2):
        if union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1

    print("Intersection: ", *intersection)
    print("Union: ", *union)


arr1 = [int(i) for i in input().split()]
arr2 = [int(i) for i in input().split()]
union_intersection(arr1, arr2)
