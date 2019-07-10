def most_frequent(arr):
    max_count = -1
    max_item = None
    count = {}
    for item in arr:
        if item not in count:
            count[item] = 1
        else:
            count[item] += 1
        if count[item] > max_count:
            max_item = item
            max_count = count[item]
    #print ("count(item) , max item "+str(count[item])+", "+ str(max_item))
    return max_item

def main():
    array = [1,4,5,1,2,1,3,3]
    print most_frequent(array)

if __name__ == "__main__":
    main()
