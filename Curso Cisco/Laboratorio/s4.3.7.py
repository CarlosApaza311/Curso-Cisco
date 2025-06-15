def is_prime(num):
    if num==2: return True
    max = round(num**.5)
    a= num%2 != 0
    i=3
    while a == True and i <= max:
        a = num%i != 0
        i += 2
    return a    

for i in range(1, 50):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
