import random
import os 
import time

passwords = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]

buyuk = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

spec = ["!", "#", "$", "%", "&", "*", "(", ")", "-", "+", "=", "[", "]", "{", "}", "|", "/", ":", ";"]

os.system("cls")
os.system("color 4a")
os.system("title Password Generator!")

print("Hmmm...")
time.sleep(3)
print("Tamam Şifren Oluşturuluyor....")
time.sleep(5)
os.system("cls")
time.sleep(2)

print("İşte Şifren;")
print(" ")
print(random.choice(passwords) + random.choice(buyuk) + random.choice(spec) + random.choice(passwords) + random.choice(buyuk) + random.choice(spec) + random.choice(passwords) + random.choice(buyuk) + random.choice(spec) + random.choice(passwords) + random.choice(buyuk) + random.choice(spec) + random.choice(passwords) + random.choice(buyuk) + random.choice(spec) + random.choice(passwords) + random.choice(buyuk) + random.choice(spec) + random.choice(passwords) + random.choice(buyuk) + random.choice(spec) + random.choice(passwords) + random.choice(buyuk) + random.choice(spec) + random.choice(passwords) + random.choice(buyuk) + random.choice(spec))

print(" ")

print("Çıkmak İçin Herhangi Bir Tuşa Basınız")
os.system("pause > null")
