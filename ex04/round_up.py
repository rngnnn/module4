import math
num1=float(input("Give me a number: "))  # input kullanicidan veri lir ama bu veri her zaman string yani metin olarak gelir.

#num1 = float(num1)  # Convert the input string to a float
rounded_num1 = math.ceil(num1)  # Round the number to the nearest integer
print(f"{rounded_num1}")

# math.ceil fonksiyonu, verilen sayıyı en yakın üst tam sayıya yuvarlar.
# Örneğin, 3.2 sayısını 4'e, 5.8 sayısını ise 6'ya yuvarlar.
# Bu, sayının ondalık kısmını dikkate alarak, sayıyı bir üst tam sayıya yuvarlamak için kullanılır
# . Bu, genellikle sayısal hesaplamalarda veya kullanıcı girdilerinin tam say