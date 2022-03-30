first_name = "kacper"
last_name = "wojcik"

mom_name = "kasia"
dad_name = "radek"

first_name_from_user = input("podaj imie: ")
last_name_from_user = input("podaj nazwisko: ")

if first_name_from_user == first_name and last_name_from_user == last_name:
    print('mozesz wejsc')

if last_name_from_user == last_name:
    if first_name_from_user == mom_name or first_name_from_user == dad_name:
        print("mama tata weee")

if not  last_name_from_user == last_name:
    print("gajewski daj se luz")

if (
    last_name_from_user == "gajewska"
    or last_name_from_user == "ignaczewska"
    and first_name_from_user == "bozena"
):
    print("bozena co tu robi")

