number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1>number2:
    if number1>number3:
        if number2>number3:#n1,n2,n3
            print(number1,number2,number3)
        else:#n1,n3,n2
            print(number1,number3,number2)
    else:#n3,n1,n2
        print(number3,number1,number2)
else:
    if number2>number3:#n2 mayor
        if number1>number3:#n2,n1,n3
            print(number2,number1,number3)
        else:#n2,n3,n1
            print(number2,number3,number1)
    else:#n3,n2,n1
        print(number3,number2,number1)
        
    