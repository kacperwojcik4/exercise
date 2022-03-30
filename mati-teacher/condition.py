age = int(input("wpisz swoj wiek: "))

if age < 18:
    print("nie sprzedam ci harnasia")
if age == 18:
    print("no moze ci sprzedam taterke")
if age > 18:
    print("gosciu ty to walisz wode")

if age < 18:
    print("znowu tu jestes nie sprzedam ci taterki")
else:
    print("4.50 za taterke pls")


if age < 15:
    print("dzieciaku tobie to nawet picolo nawet nie sprzedam")
elif 15 < age < 18:
    print("znowu ty nie ma taterki")
elif age == 23:
    print("takim nie sprzedaje")
else:
    print("taterka here ")
