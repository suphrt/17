f = open('17_3.txt')
a = [int(i) for i in f]
maxim = 0
cnt = 0

for i in range(len(a) - 1):
    for j in range (i + 1, len(a) - 1):
        if ((a[i] - a[j]) % 2 == 0) and (a[i] % 31 == 0 or a[j] % 31 == 0):
            cnt += 1
            maxim = max(maxim, a[i] + a[j])

print(cnt, maxim)