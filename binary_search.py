lst = []
i = 0
check = 0

while True:
    i += 1
    element = input("Enter "+"element "+str(i)+": ")
    if element in ["exit","EXIT","Exit"] :
        break
    lst.append(element)

print(f"The given list is :{lst}")

m = len(lst)
lst.sort()

to_check_element = input(f"Enter the element to be searched : ")

while m > 0:
    if lst[int(m/2)] == to_check_element:
        print(f"Element found")
        check = 1
        break
    elif lst[int(m/2)] < to_check_element:
        lst = lst[int(m/2)::]
    else:
        lst = lst[:int(m/2):]
    m = len(lst)
        
if check == 0:
    print(f"Element not found")