def is_rotation(a1,a2):
    first_ele = 0
    n =len(a1)
    if len(a1) != len(a2):
        return False

    for i in range(0,n):
        if a2[i] == a1[0]:
            first_ele = i
            break

    for i in range(0,n):
        if first_ele+i <n:
            if a1[i] != a2[first_ele+i]:
                return False
        else:
            if a1[i]!=a2[first_ele+i-n]:
                return False
    return True

def main():
    print is_rotation([1,2,3,4,5], [3,4,5,1,2])

if __name__ == "__main__":
    main()
