def jumpingOnClouds(c):
    count_steps = 0
    i = 0
    while i<len(c):
        if c[i] == 0:
            count_steps += 1
            if i<(len(c)) and c[i+1] == 1:
                count_steps += 1
            elif i == (len(c)-1) and c[i]== 0 :
                count_steps += 1


        i += 2
    return count_steps

    return valley

def caller():
    print jumpingOnClouds([0,0,1,0,0,1,0,0])

if __name__ == "__main__":
    caller()
