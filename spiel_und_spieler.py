l = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']

for i in l:
    for j in l:
        
        if j == i:
            pass
        else:
            t = open("Spielstände/%s-%s.txt"%(i,j),"w")
            t.write("0:0")
            t.close()
            """

text_dokument = open("Spielstände/%s-%s.txt"%("0000", "0011"), "r")
alter_stand = text_dokument.read()
print(alter_stand)
text_dokument.close()
text_dokument = open("Spielstände/%s-%s.txt"%("0011", "0000"), "r")
alter_stand = text_dokument.read()
print(alter_stand)
text_dokument.close()"""
