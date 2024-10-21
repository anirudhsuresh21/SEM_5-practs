
def generate_matrix(key):
    prep =  ""
    key = key.replace("j","i")
    key = "".join(set(key))
    prep = key
    alpha = "abcdefghiklmnopqrstuvwxyz"

    for i in alpha:
        if i not in prep:
            prep += i

    matrix = [["" for _ in range(5)] for _ in range(5)]
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = prep[index]
            index += 1

    return matrix

def find_position(matrix,letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row,col

def encrypt(text):
    global excess
    encrypted = ""
    matrix = generate_matrix("monarchy")
    text = text.replace("j", "i")
    if len(text) % 2 != 0:
        excess = True
        text += 'x' 

    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            enc_char1 = matrix[row1][(col1 + 1) % 5]
            enc_char2 = matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            enc_char1 = matrix[(row1 + 1) % 5][col1]
            enc_char2 = matrix[(row2 + 1) % 5][col2]
        else:
            enc_char1 = matrix[row1][col2]
            enc_char2 = matrix[row2][col1]

        encrypted += enc_char1 + enc_char2

    return encrypted

def decrypt(text):
    decrypted = ""
    matrix = generate_matrix("monarchy")
    text = text.replace("j", "i")
    # if len(text) % 2 != 0:
    #     text += 'x'

    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1]
        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            enc_char1 = matrix[row1][(col1 - 1) % 5]
            enc_char2 = matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            enc_char1 = matrix[(row1 - 1) % 5][col1]
            enc_char2 = matrix[(row2 - 1) % 5][col2]
        else:
            enc_char1 = matrix[row1][col2]
            enc_char2 = matrix[row2][col1]

        decrypted += enc_char1 + enc_char2

    return decrypted[0:-1] if excess else decrypted

encrypted_msg = encrypt("hello")
decrypted_msg = decrypt(encrypted_msg)
print(encrypted_msg)
print(decrypted_msg)



