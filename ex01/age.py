#!/usr/bin/env python3

age = input("Please tell me your age: ")#kullanicidan veri ister input)(input() asks the user for data)
age2 = int(age) #daha sonra kullanicidan veri yani data yni soru istedikten snra 

#input() kullanıcıdan veri ister
#"Please tell me your age: " mesajını gösterir
#Kullanıcı bir şey yazar (örnek: "25")
#Bu değer age değişkenine string olarak kaydedilir
#age = "25" (sayı değil, metin!)
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#input() kullanıcıdan veri ister
#"Please tell me your age: " mesajını gösterir
#Kullanıcı bir şey yazar (örnek: "25")
#Bu değer age değişkenine string olarak kaydedilir
#age = "25" (sayı değil, metin!)

#eng:
#input() prompts for user input
#Shows "Please tell me your age: " message
#User types something (example: "25")
#This value is stored in the age variable as a string
#age = "25" (text, not a number!)
#;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#input() prompts for user input
#Shows "Please tell me your age: " message
#User types something (example: "25")
#This value is stored in the age variable as a string
#age = "25" (text, not a number!)


print(f"You are currently {age2} years old")
print(f"In 10 years, you will be {age2 + 10} years old")
print(f"In 20 years, you will be {age2 + 20} years old")
print(f"In 30 years, you will be {age2 + 30} years old")
