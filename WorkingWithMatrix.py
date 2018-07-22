M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]

print(M)
Set1 = {sum(row) for row in M}
print(Set1)
Dict1 = {i : sum(M[i]) for i in range(3)}
print(Dict1)

diag = [M[i][i] for i in [0, 1, 2]]
print("The diagonal of my matrix is: ",diag)

col2 = [row[0] for row in M]
print(col2)
col1 = [row[1] + 1 for row in M]
print(col1)
col3 = [row[1] for row in M if row[1] % 2 == 0] # Filter out odd items
print(col3)
M = [[x ** 2, x ** 3] for x in range(4)]
print(M)
M = [[x, x / 2, x * 2] for x in range(-6,7,2) if x > 0]
print(M)
M = list(map(sum, M))
print(M)




