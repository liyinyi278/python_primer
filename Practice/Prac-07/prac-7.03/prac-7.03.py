# 练习 7.3：10 的整数倍 
#   让用户输入一个数，并指出这个数是否是10 的整数倍。

number = int(input("Enter a number: "))

if number % 10 == 0:
    print("The last digit is 0")
else:
    print("The last digit is not 0")