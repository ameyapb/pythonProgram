num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
print("Operator cloices can be \n 1.Add  \n 2.Subtract  \n 3.Multiply \n 4.Division /")
op =input("Enter operator: ")

if op == "1":
    print(num1 + num2)
elif op == "2":
    print(num1 - num2)
elif op == "3":
    print(num1 * num2)
elif op == "4":
    print(num1 / num2)
else:
    print("Please enter the provided choices!")
