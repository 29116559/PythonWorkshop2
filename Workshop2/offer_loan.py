# Dependent variables - age, income, not received a loan in the past
age = int(input("How old are you?: "))
income = float(input("What is your income?: "))
received = str(input("Have you received a loan in the past? (True or False): "))

print(received)

if age > 21 and income > 21000 and received == "False":
    print("The loan can be offered")
else:
    print("Nope youre out sucker")