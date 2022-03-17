fin = open("./Databases/ENGwordlist_nytimes.txt", 'r')
fout = open("./Databases/ENGwordlist_nytimes_cleared.txt", 'w')
fin.seek(0)
lines = fin.readlines()

for line in lines:
    line = line.replace(",", "\n")
    fout.write(line.replace("\"",""))

fout.close()
fin.close()