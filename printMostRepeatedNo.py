import operator

'''def most_frequent(given_list):
    max_item = None
    n = len(given_list)
    counter = 0
    if n == 0:
        return max_item
    else : max_item = 0
    for i in range (0,n-1):
        num_count = given_list.count(given_list[i])
        if  counter < given_list.count(given_list[i]):
            counter = num_count
            max_item = given_list[i]
    return max_item'''

def most_frequent(given_list):
    max_item = None
    max_count = 0
    n = len(given_list)
    if n == -1 or n == 0 :
        return None

    count = {}

    for i in range(0,n):
        if given_list[i] not in count:
            count[given_list[i]] = 1
        else:
            count[given_list[i]] += 1

        if count[given_list[i]] > max_count:
            max_count = count[given_list[i]]
            max_item = given_list[i]
    return max_item

def common_elements(list1, list2):
    p1 = 0
    p2 = 0
    result = []
    while p1< len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append
            p1 += 1
            p2 += 1
        elif list1[p1]> list2[p2]:
            p1 += 1
        else:
            p2 += 1

def is_rotation(list1, list2):
    first_elem_loc = -1
    n = len(list1)

    if len(list1) != len(list2):
        print "false1"
        return False

    for i in range(0,n):
        if list1[0] == list2[i]:
            first_elem_loc = i
            print "first_elem_loc %d", first_elem_loc
            break
    if first_elem_loc == -1:
        return False

    for i in range(0,n):
        j = (first_elem_loc+i)%n
        if list1[i]!=list2[j]:
            return False
    return True

def non_repeating(given_string):
    n = len(given_string)
    if n ==0:
        return None
    if n ==1:
        return given_string[0]
    count = 0
    dict1 = {}
    for c in given_string:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1

    for c in given_string:
        if dict1[c] == 1:
            return c
    return None

def is_one_away(s1, s2):
    operation = 0
    len_diff = len(s1) - len(s2)
    if len_diff == 0:
        return is_one_away_same_len(s1,s2)
    elif len_diff == 1:
        return is_one_away_diff_len(s2,s1)
    elif len_diff == -1:
        return is_one_away_diff_len(s1,s2)
    else: return False

def is_one_away_same_len(s1,s2):
    count_diff = 0
    for i in range(0,len(s1)):
        if s1[i] != s2[i]:
            count_diff += 1
    if count_diff <= 1:
        return True
    return False

def is_one_away_diff_len(s1,s2):
    count_diff = 0
    i = 0
    while i < len(s1):
        if s1[i+count_diff] != s2[i]:
            count_diff += 1
        i +=1
    if count_diff <=1:
        return True
    return False

def main():
    print is_one_away("abefd", "abefdee")

if __name__ == "__main__":
    main()
