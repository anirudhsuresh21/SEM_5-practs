prep =  ""
key = "hellj"
key = key.replace("j","i")
print(key)
key = "".join(set(key))
print(key)
prep = key

alpha = "abcdefghiklmnopqrstuvwxyz"

for i in alpha:
    if i not in prep:
        prep += i

print(prep)


matrix = [["" for _ in range(5)] for _ in range(5)]
index = 0
for i in range(5):
    for j in range(5):
        matrix[i][j] = prep[index]
        index += 1

print(matrix)


