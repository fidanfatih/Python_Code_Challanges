with open("istiklal.txt", "r", encoding="utf-8") as f:
    lines=f.readlines()

with open("istiklal.txt", "w", encoding="utf-8") as f:
    for line in lines:
        if line=="\n":
            f.write(line.replace("\n",""))
        else:
            f.write(line)