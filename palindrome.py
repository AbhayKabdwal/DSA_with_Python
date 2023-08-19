a = input("Enter a string : ")
c = 1
for i in range(0,int(len(a)/2)+1):
    if a[i]!= a[len(a)-i-1]:
        print("Not a palindrome")
        c = 0
        break
    else:
        pass

if c==1:
    print("Palindrome")