fin = open("./Databases/TRwordlist_bundle.txt", 'r')
fout = open("./Databases/TRwordlist_bundle_cleared.txt", 'w')
fin.seek(0)
lines = fin.readlines()

for line in lines:
    line = line.replace(",", "\n")
    fout.write(line.replace("\"",""))

fout.close()
fin.close()