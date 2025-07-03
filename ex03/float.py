

num1=input("Give me a number: ")  # input kullanicidan veri lir ama bu veri her zaman string yani metin olarak gelir.
num1 = float(num1)  # Convert the input string to a float
if num1.is_integer():
    # If the number is an integer, convert it to int
    
  print(f"The number is an integer: {int(num1)}")
else:
  
    print(f"The number is a decimal: {num1}")  # If it's not an integer, print it as a float9