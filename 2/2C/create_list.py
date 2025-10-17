mylist = []
print("Type 5 different integers:")
for _ in range(5) :
    mylist.append(int(input()))
length_list = len(mylist)
print("Length of the list is: " + str(length_list))
print("Last element is: " + str(mylist[length_list - 1]))