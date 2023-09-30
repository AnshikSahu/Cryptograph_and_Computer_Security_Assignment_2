from decrypt import check_padding
from encrypt import main as encrypt

"""
You can implement helper function here if you want
"""

def attack(cipher_text):
    """
    Takes a ciphertext (list of integers from 0 to 255 [byte array]) as input
    TODO: Implement your code below
    """
    l=len(cipher_text)//16-1
    if(l==0):
        return []
    padding=16
    # figure out padding
    while(padding>0):
        cipher_text[padding-1]=255-cipher_text[padding-1]
        valid=check_padding(cipher_text)
        cipher_text[padding-1]=255-cipher_text[padding-1]
        if(valid==2):
            break
        padding-=1
    m=[padding]*padding
    # figure out the message
    temp=padding
    for i in range(0,l):
        new_cypher=cipher_text[i*16:(i+2)*16].copy()
        for j in range(temp,16):
            for k in range(0,j):
                new_cypher[k]=(j+1)^m[i*16+k]^cipher_text[i*16+k]
            for k in range(0,256):
                new_cypher[j]=k^(j+1)^cipher_text[i*16+j]
                valid=check_padding(new_cypher)
                if(valid==0):
                    m.append(k)
                    break
        temp=0
    """
    Return a list of integers representing the original message
    """
    return m[padding:]

# if __name__ == "__main__":
#     print(attack(encrypt()))