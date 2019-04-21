# Implement your function below.
def click(field, num_rows, num_cols, given_i, given_j):
    to_check = []
    if field[given_i][given_j] == 0:
        field[given_i][given_j] = -2
        to_check.insert(0,(given_i,given_j))
    while len(to_check) > 0:
        row = to_check[0][0]
        col = to_check[0][1]
        to_check.pop(0)
        for i in range(row-1, row+2):
            for j in range (col-1,col+2):
                if 0<=i<num_rows and 0<=j<num_cols and field[i][j] == 0:
                    field[i][j] = -2
                    to_check.insert(0,(i,j))
    return field


# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
field1 = [[0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0],
          [0, 1, -1, 1, 0]]
print click(field1, 3, 5, 0 ,0)

# click(field1, 3, 5, 2, 2) should return:
# [[0, 0, 0, 0, 0],
#  [0, 1, 1, 1, 0],
#  [0, 1, -1, 1, 0]]

# click(field1, 3, 5, 1, 4) should return:
# [[-2, -2, -2, -2, -2],
#  [-2, 1, 1, 1, -2],
#  [-2, 1, -1, 1, -2]]


field2 = [[-1, 1, 0, 0],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [0, 0, 1, -1]]

# click(field2, 4, 4, 0, 1) should return:
# [[-1, 1, 0, 0],
#  [1, 1, 0, 0],
#  [0, 0, 1, 1],
#  [0, 0, 1, -1]]

# click(field2, 4, 4, 1, 3) should return:
# [[-1, 1, -2, -2],
#  [1, 1, -2, -2],
#  [-2, -2, 1, 1],
#  [-2, -2, 1, -1]]
