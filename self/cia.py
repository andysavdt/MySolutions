def common_elements(a1,a2):
    p1 =0
    p2 =0
    result = []
    while p1 <len(a1) and p2<len(a2):
        if a1[p1] == a2[p2]:
            result.append(a1[p1])
            p1 += 1
            p2 += 1
        elif a1[p1]> a2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result

print common_elements([1,2,3,4,5,6,12], [1,2,3,4,6,8,10,12,14])
