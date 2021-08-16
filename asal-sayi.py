
sayi = int(input("Sayı giriniz: "))
asalmi = True

if sayi == 1:
	asalmi = False
	

for i in range(2, sayi):
	if sayi % i == 0:
		asalmi = False
		break
		
if asalmi:
	print("Sayı Asaldır")
else:
	print("Sayı asal değildir.")