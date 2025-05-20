my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
uni=[]
for i in my_list:
    if i not in uni:
        uni.append(i)
my_list=uni[:]
    
#
print("The list with unique elements only:")
print(my_list)
