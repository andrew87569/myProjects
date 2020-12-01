string = '''Dl'yl uv zayhunlyz av svcl
Fvb ruvd aol ybslz huk zv kv P
H mbss jvttpatlua'z doha P't aopurpun vm
Fvb dvbsku'a nla aopz myvt huf vaoly nbf
P qbza dhuuh alss fvb ovd P't mllspun
Nvaah thrl fvb buklyzahuk
Ulcly nvuuh npcl fvb bw
Ulcly nvuuh sla fvb kvdu
Ulcly nvuuh ybu hyvbuk huk klzlya fvb
Ulcly nvuuh thrl fvb jyf
Ulcly nvuuh zhf nvvkifl
Ulcly nvuuh alss h spl huk obya fvb'''

string = string.lower()

a = list(string)
displacement = 0
for i in range(26):
    displacement += 1
    for index in range(0,len(a)):
        if a[index] == '\n' or a[index] == '\'' or a[index] == ' ':
            continue
        elif a[index] == 'z':
            a[index] = 'a'
        else:
            char = chr(ord(a[index]) + 1)
            a[index] = char
    
    b = ''.join(a)
    print(b)
    ask = input("Is this correct? y/N: ")
    if ask == 'y':
        print('\nIt was a displacement of ' + str(displacement) + ' letters!')
        break
    elif ask == 'N':
        continue