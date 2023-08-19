a = input("Enter a number : ")
arm = 0

for i in range(0, len(a)):
    arm += int(a[i])**len(a)

if arm == int(a):
    print("Is an armstrong number")

else:
    print("Is not an armstrong number")