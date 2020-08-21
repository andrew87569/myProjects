# http://www.pythonchallenge.com/pc/def/map.html
# everybody thinks twice before solving this.

string = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr\'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

def decipher(a):
    b = ''
    for char in a:
        if char == 'y':
            b += 'a'
        elif char == 'z':
            b += 'b'
        elif ord(char) >= 97 and ord(char) <= 120:
            b += chr(ord(char)+2)
        else:
            b += char
    return b

def decipher2(string):
    table = str.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
    return(string.translate(table))

print(decipher(string) + '\n' + decipher2('map'))