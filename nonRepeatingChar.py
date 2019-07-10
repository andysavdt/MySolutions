def non_repeating_char(string):
    count = {}

    for char in string:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1

    for element in count:
        if count[element] ==1:
            return element
    return None

def main():
    print non_repeating_char("saasmmpplle")

if __name__ == "__main__":
    main()
