a = input("Enter a number :")
b = 0
for i in range(len(a)):
    b+=int(a[i])*(10**i)

print(b)