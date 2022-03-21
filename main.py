count = 0
summ = 0
with open("17.txt", "r") as f:
    lines = f.readlines()
for i in range(len(lines) - 1):
    if (int(lines[i]) % 3 == 0) or (int(lines[i+1]) % 3 == 0):
        count += 1
    summ = max(summ, int(lines[i]) + int(lines[i+1]))
print(count, summ)
