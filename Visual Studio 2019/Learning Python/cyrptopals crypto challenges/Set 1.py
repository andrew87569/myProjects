# 1 - Convert hex to base64

import base64

hex_str1 = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

def hex2base64(hex_str):
    hex_str = bytes.fromhex(hex_str)
    return base64.b64encode(hex_str)

hex2base64(hex_str1)

# 2 - Fixed XOR

def str2hex(a_str):
    hex_str = int(a_str,base=16)
    return hex_str

str1 = '1c0111001f010100061a024b53535009181c'
str2 = '686974207468652062756c6c277320657965'

def xor2str(str1,str2):
    str1 = str2hex(str1)
    str2 = str2hex(str2)
    return hex(str1 ^ str2)

xor2str(str1,str2)

# 3 - Single-byte XOR

hex_str2 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

hex2base64('andrew')