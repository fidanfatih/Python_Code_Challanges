with open("istiklal.txt", "r", encoding="utf-8") as f:
    lines=f.readlines()

with open("istiklal.txt", "w", encoding="utf-8") as f:
    i=0
    for line in lines:
        if i%4==0:
            f.write("\n"+line)
        else:
            f.write(line)
        i+=1