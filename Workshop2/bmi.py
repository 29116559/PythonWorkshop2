weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

result = None

def bmi(weight, height) -> float:
    heightInM = height / 100
    return weight / (heightInM ** 2)

if weight and height: result = bmi(weight, height)

print(result)