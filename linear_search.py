lst = []
i,j = 0,0
lst_index = []

while True:
    i += 1
    element = input("Enter "+"element "+str(i)+": ")
    if element in ["exit","EXIT","Exit"] :
        break
    lst.append(element)

print("The given list is :",lst)

to_check_element = input("Enter the element to be searched : ")

for lst_element in lst:
    if lst_element == to_check_element:
        print(f"{to_check_element} found at index {j}")
        lst_index.append(j)
        check = 1
    else:
        pass
    j += 1

if not lst_index:
    print("Element not found in the given list")