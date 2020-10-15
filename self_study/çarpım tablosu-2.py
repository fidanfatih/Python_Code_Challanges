str,row="ÇARPIM TABLOSU",list()
print(f"{str:^77}\n")
for _ in range(22): row.append([])
for j in range(1,11):
    for i in range(1,11):
        if j<6: row[i-1].append(f"{j:^2} x {i:^2} = {i*j:^3}  ")
        else: row[i+10].append(f"{j:^2} x {i:^2} = {i*j:^3}  ")
for line in row: print(*line)