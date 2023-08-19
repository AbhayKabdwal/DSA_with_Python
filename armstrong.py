lst = []

for a in range(10,100_000):
    a = str(a)
    arm = 0

    for i in range(0, len(a)):
        arm += int(a[i])**len(a)

    if arm == int(a):
        lst.append(a)

    else:
        pass

print(lst)   