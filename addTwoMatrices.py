# Matrix 1
x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
# Matrix 2
y = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]]
# Matrix 3
z = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

# iterate through row
for i in range(len(x)):  # loop to access row
    # iterate through column
    for j in range(len(x[0])):  # loop to access column
        result[i][j] = x[i][j] + y[i][j] + z[i][j] # adding elements of three matrices and storing results

for r in result:
    print(r)
