
import math

giris = """

	1 : "Toplama İşlemi", 
	2 : "Çıkarma İşlemi", 
	3 : "Çarpma İşlemi",  
	4 : "Bölme İşlemi"
	5 : "Kare Alma"
	6 : "Karekök Alma"
	7 : "Logaritma Alma"
	8 : "Faktöriyel Hesaplama"
"""


print(giris)
i= 1

while i==1:
	islem = input("Yapmak istediğiniz işlemi seçiniz(çıkmak için q) :")
	
	if islem == "q":
		i = 0
		print("Çıkılıyor...")
	
	# Sum	
	elif islem == "1":
		sayi1 = input("Toplamak İstediğiniz İlk Sayı: ")
		sayi2 = input("Toplamak İstediğiniz İkinci Sayı: ")
		print("Sonuç: ", int(sayi1) + int(sayi2))
	
	# Subtraction
	elif islem == "2":
		sayi1 = input("Çıkarmak İstediğiniz İlk Sayı: ")
		sayi2 = input("Çıkarmak İstediğiniz İkinci Sayı: ")
		print("Sonuç: ", int(sayi1) - int(sayi2))
		
	# Multiplication	
	elif islem == "3":
		sayi1 = input("Çarpmak İstediğiniz İlk Sayı: ")
		sayi2 = input("Çarpmak İstediğiniz İkinci Sayı: ")
		print("Sonuç: ", int(sayi1) * int(sayi2))
	
	# Division	
	elif islem == "4":
		sayi1 = input("Bölmek İstediğiniz İlk Sayı: ")
		sayi2 = input("Bölmek İstediğiniz İkinci Sayı: ")
		print("Sonuç: ", int(sayi1) / int(sayi2))
		
	# Square	
	elif islem == "5":
		sayi1 = input("Karesini Almak İstediğiniz Sayıyı Giriniz: ")
		print("Sonuç:" , int(sayi1)**2)
		
	# Square Root	
	elif islem == "6":
		sayi1 = input("Karekökünü Almak İstediğiniz Sayıyı Giriniz: ")
		print("Sonuç: ", int(sayi1)** 0.5)
		
	# Logarithm	
	elif islem == "7":
		sayi1 = input("Logaritması alınacak sayı giriniz: ")
		if sayi1 == "0":
			print("Lütfen 0'dan büyük bir sayı giriniz.")
		else:
			print("Sonuç: ", math.log10(int(sayi1)))
			
	# Factorial		
	elif islem == "8":
		sayi1 = int(input("Faktöriyeli alınacak sayı giriniz: "))
		if sayi1 < 0:
			print("Negatif sayıların faktöriyeli hesaplanamaz.")
		elif sayi1 == 0:
			print("0! = 1")
		else:
			for b in range(1, sayi1+1):
				i = i*b
				print("Sonuç: ", str(i))

	else:
		print(f"Yanlış sayı girdiniz, lütfen aşağıdaki işlemlerden birini seçiniz: {giris}")
