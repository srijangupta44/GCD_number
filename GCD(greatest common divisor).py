def gcd_num(num1,num2):
    num1 = int(input("enter the num 1: "))
    num2 = int(input("enter the num 2: "))
    value = []
    max = 0
    for i in range(1,num1):
        if (num1%i==0):
            for j in range(1, num2):
                if (num2%j==0):
                    if (i==j):
                        value.append(i)
                        for values in value:
                            if max<values:
                                max = values
    return max              
result = gcd_num(num1,num2)
print(result) 
