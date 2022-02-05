from pickle import TRUE
import binascii 

BITS = ('0', '1')
ASCII_BITS = 7

def display_bits(b):
    """converts list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

def pad_bits(bits, pad):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits
        
def convert_to_bits(n):
    """converts an integer `n` to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = int(n / 2)
    return result

def string_to_bits(s):
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in 
            map(chr_to_bit, s)
            for b in group]

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
                    for i in range(0, len(b), ASCII_BITS)])

def otp(m, k):
    assert len(m) == len(k)
    return [(mm + kk) % 2 for mm, kk in zip(m, k)]

def bin2hex(str1):
    bytes_str = bytes(str1, 'utf-8')
    return binascii.hexlify(bytes_str)

def XOR(A, B):
    return ''.join([chr(x ^ y) for x, y in zip(bytes(A, 'ascii'), bytes(B, 'ascii'))])

def crib_drag(text, c):
    for i in range(0, len(text) - len(c) + 1):
        pt = text[i:(i + len(c))]
        print("\t{0}:{1}".format(i,XOR(pt,c)))


# 1 - Set your own plain text M1, M2, and k

k= "FOOD"

M1 = "KARI"
print("\n" + M1 + " in binary python list is \n" + str(string_to_bits(M1))+ "\n same with 0b" + display_bits(string_to_bits(M1)))


M2 = "AYAM"
print("\n" + M2 + " in binary python list is \n" + str(string_to_bits(M2))+ "\n same with 0b" + display_bits(string_to_bits(M2)))

print ("\nKEY\t: " + k )
print ("M1\t: " + M1 )
print ("M2\t: " + M2 )


#ENCODE

print ( "\nENCRYPTION : \n" )

C1 = otp(string_to_bits(M1), string_to_bits(k))           
C2 = otp(string_to_bits(M2), string_to_bits(k))           
C1hexadecimal= bin2hex(bits_to_string(C1))                              # convert C1 in binary to hexadecimal
C2hexadecimal= bin2hex(bits_to_string(C2))                              # convert C2 in binary to hexadecimal

OTPc = otp ( C1 , C2 )                                        

print ("Key\t: " + display_bits(string_to_bits(k)))             
print ("M1 is\t: " + display_bits(string_to_bits(M1)))    
print ("C1 is\t: " + display_bits((C1)))                       
print ("C1 in hex\t: " + C1hexadecimal.decode('utf-8'))                 

print ("\nKey\t: " + display_bits(string_to_bits(k)))           
print ("M2 is\t: " + display_bits(string_to_bits(M2)))    
print ("C2 is\t: " + display_bits((C2)))                        
print ("C2 in hex\t: " + C2hexadecimal.decode('utf-8'))                 

print ("\notp(C1,C2) : " + display_bits(OTPc))                  

#DECODE

print("***DECRYPTION***")

C1 = XOR("KARI", "AYAM")
C2 = XOR("KARI", "AYAM")
C1C2 = XOR("KARI", "AYAM")

while(TRUE):
    print("Try some letters that may be in your messages (Hint: maggie flavour with letter A)")
    guess = input()
    crib_drag(C1C2, guess)