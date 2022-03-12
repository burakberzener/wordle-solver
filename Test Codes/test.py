fin = open("wordlist2.txt", 'a+')
fout = open("wordlist3.txt", 'w')
fin.seek(0)
lines = fin.readlines()

for line in lines:
    fout.write(line[-6:-1])
    fout.write("\n")

fout.close()
fin.close()