#print (ord('A'),ord('Z')) 65 90
#print (ord('0'),ord('9')) 48 57
s = input().upper()
for i in s:
    o = ord(i)
    if 65<=o<=90:
        if o+4>90: print(chr(o-26),end='')
        else: print(chr(o+4),end='')
    elif 48<=o<=57:
        if o-2<48: print(chr(o+8),end='')
        else: print(chr(o-2),end='')
    else:
        print(i,end='')