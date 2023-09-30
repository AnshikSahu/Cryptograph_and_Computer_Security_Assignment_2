"""
You can implement helper function here if you want
"""
# from decrypt import decryption_oracle
def attack(ciphertext, decrypt):
    """
    You are given a ciphertext(byte array) of size 48 on some random message of size 48 bytes. 
    You are also given access to the decryption function which takes a ciphertext of size 48 and outputs 48 bytes message corresponding to the ciphertext
    Example Use: decrypt(ciphertext)

    NOTE: 
        1. Ensure that ciphertext send as input to decrypt function is byte array of size 48
        2. Only one query can be made to decrypt function

    TODO: Implement your code below
    """
    n=ciphertext[:16]*2+ciphertext[16:32]
    m=decrypt(n)
    """
    Return the key in byte format
    Example of key: b'\xb8\x15\xd4\xeeUO\xdf\xa3\x02\xe9\x8d.\xb2\x10\xfa\x0c'
    """
    key=bytes([m[i]^m[i+16]^n[i] for i in range(16)])
    return key

# if __name__ == "__main__":
#     message = b'Hello World!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!wefgerfref3feewf4e'
#     decrypt = decryption_oracle()
#     ciphertext = decrypt.encrypt(message[:48])
#     key = attack(ciphertext, decrypt.decrypt)
#     print(key)
#     assert key == b'\xb8\x15\xd4\xeeUO\xdf\xa3\x02\xe9\x8d.\xb2\x10\xfa\x0c'