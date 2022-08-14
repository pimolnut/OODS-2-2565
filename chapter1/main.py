print("*** multiplication or sum ***")
num = str(input("Enter num1 num2 : ")).split()
num1 = int(num[0])
num2 = int(num[1])
if num1*num2 > 1000:
    result = num1+num2
    print("The result is "+str(result))
elif num1*num2 <= 1000:
    result1 = num1*num2
    print('The result is '+str(result1))