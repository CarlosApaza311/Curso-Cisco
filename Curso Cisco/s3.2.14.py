blocks = int(input("Enter the number of blocks: "))
i=0
height = 0

while i <= blocks:
    height += 1
    i = (height**2+height)/2

height = height-1

print("The height of the pyramid:", height)