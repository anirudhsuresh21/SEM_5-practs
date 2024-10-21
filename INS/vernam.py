def encrypt(key,string):
    encrypted =""
    for i in range(len(string)):
        print(key[i %len(key)])
        encrypted += chr(ord(string[i]) ^ (ord(key[i %len(key)])))
    return encrypted

def decrypt(key,string):
    decrypted = ""
    for i in range(len(string)):
        decrypted += chr(ord(string[i]) ^ (ord(key[i %len(key)])))
    return decrypted

string = input("Enter the String :")
key = input("Enter the key :")
encrypt_msg=encrypt(key,string)
print(encrypt_msg)
print(decrypt(key,encrypt_msg))
