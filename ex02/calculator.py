
#!/usr/bin/env python3
#u satır ************"shebang"********* olarak bilinir.
#Anlamı: Bu dosya çalıştırıldığında, onu çalıştıracak olan program python3 olsun.

#Terminalde ./calculator.py yazdığında sistem bu satırı okuyarak hangi yorumlayıcıyla çalıştıracağını anlar.

num1=input("Give me the first number: ") #input kullanicidan veri lir  ama bu veri her zaman string yani metin olarak gelir.
#input fonksiyonu kullanıcının girdiği veriyi alır ve string olarak döner.
#float ise sayiyi ondalik sayiya cevirir.
#int ise sayiyi tam sayiya cevirir.
#input fonksiyonunun içine yazdığımız metin, kullanıcıya gösterilecek mesajdır.


num2=input("Give me the second number: ")
print("Thank you! ")

num1=int(num1)  # Convert the input to an integer
num2=int(num2)  # Convert the input 7to an integer

print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1//num2}")


#iki slash eklediginde otamatik olarak tam sayi yapar
