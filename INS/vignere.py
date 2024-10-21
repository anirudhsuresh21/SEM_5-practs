charset = "abcdefghijklmnopqrstuvwxyz"
def encrypt(text,key):
    encrypted = ""
    for i in range(len(text)):
        encrypted += charset[(charset.index(text[i]) + charset.index(key[i % len(key)])) % 26]
    return encrypted

def decrypt(cipher,key):
    decrypted = ""
    for i in range(len(cipher)):
        decrypted += charset[(charset.index(cipher[i]) - charset.index(key[i % len(key)])) % 26]
    return decrypted

encrypt_msg = encrypt("hello","key")
print(encrypt_msg)
decrypt_msg = decrypt(encrypt_msg,"key")
print(decrypt_msg)
