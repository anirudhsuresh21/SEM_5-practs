import math
text = "mynameisy"
key = [2,4,1,3]
key1 = sorted(key)
print(key1)
nocol = math.ceil(len(text) / len(key))
print(nocol)
index = 0
matrix = [["" for _ in range(len(key))] for _ in range(nocol)]

for i in range(nocol):
    for j in range(len(key)):
        matrix[i][j] = text[index]
        index += 1

encrypted =""
for i in range(len(key1)):
    col = key.index(key1[i])
    for i in range(nocol):
        encrypted += matrix[i][col]

decrypted = ""
for i in range(nocol):
    for j in range(len(key)):
        decrypted += matrix[i][j]

print(decrypted)
print(encrypted)
print(matrix)