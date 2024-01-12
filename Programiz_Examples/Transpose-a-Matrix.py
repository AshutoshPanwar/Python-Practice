# Python Program to Transpose a Matrix

X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]
#Iterate through row's
for i in range(len(X)):
    # Iterate through column's
    for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)