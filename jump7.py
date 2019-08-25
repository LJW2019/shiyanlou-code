a = 0
for a in range(1,101):
    if a % 7 == 0:
        continue
    if a % 10 == 7:
        continue
    if int(a/10) == 7:
        continue
    print(a)
a = a+1

