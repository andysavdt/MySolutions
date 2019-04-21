#!/usr/bin/env python

def repeatedString(s, n):
    string = s
    str_len = len(s)
    counter =0
    unit_count = string.count('a')
    multiple_factor = int(n/str_len)
    multiple_remainder = n%str_len
    remainder_string =""

    counter = multiple_factor * unit_count
    if multiple_remainder !=0:
        remainder_string = string[0:multiple_remainder]
    print remainder_string
    counter = counter + remainder_string.count('a')

    return counter



def main():
    print (repeatedString("aba",10))

if __name__ == "__main__":
    main()

# abaabaabaa
