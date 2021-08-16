
import random


giris = (

	"***Number Guessing***\n1 ile 100 Arasında Sayı Giriniz\nÇıkmak için 0 giriniz."

)

x = random.randint(1,100)
puan = 100
sayac = 0

print(giris)

hak= int(input("Kaç Hak İstiyorsunuz: "))
sayi = input("Tahmin ettiğiniz sayı:")

while x != int(sayi):
	hak -=1
	sayac +=1
	puan -=10
	if int(sayi) not in range(0,101):
		print("Yanlış sayı! 1 ile 100 arasında tahmin yapınız.")
		sayi = int(input("Tahmin ettiğiniz sayı:"))
	
	elif hak == 0:
		print(f"Hakkınız bitti! Sayı {x} idi. Yeniden Deneyin.")
		break
		
	elif int(sayi)==0:
		print("Uygulamadan Çıkılıyor.")
		break
	
	elif int(sayi)>x:
		print("Aşağı")
		sayi = int(input(f"{hak} hakkınız kaldı. Tahmin ettiğiniz sayı:"))
		
	elif int(sayi)<x:
		print("Yukarı")
		sayi = int(input(f"{hak} hakkınız kaldı. Tahmin ettiğiniz sayı:"))

else: 
	int(sayi)==x
	print(f"Tebrikler {sayac} denemede bildiniz! Puanınız: {puan}")





