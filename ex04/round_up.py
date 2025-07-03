
num1=input("Give me a number: ")  # input kullanicidan veri lir ama bu veri her zaman string yani metin olarak gelir.

num1 = float(num1)  # Convert the input string to a float
rounded_num1 = round(num1)  # Round the number to the nearest integer
print(f"{rounded_num1}")

