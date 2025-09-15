# calculator using if elif

num1 = float(input("Enter 1st number:  "))
num2 = float(input("Enter 2nd number:  "))
choose = input("What would you like to choose(+,-,*,/):")

if choose == "+":
        output = num1+num2
        print(output)
elif choose =="-":
        output = num1-num2
        print(output)
elif choose =="*":        
        output = num1*num2
        print(output)
elif choose =="/":        
        output = num1/num2
        print(round(output, 2))
else:
        print("Enter a valid choice")        