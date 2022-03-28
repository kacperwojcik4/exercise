if __name__ == "__main__":
    net_price = int(input("podaj cene netto: "))
    vat_rate = int(input("podaj wartosc vat: "))
    gross_price = net_price + (net_price * vat_rate / 100)
    print(f"cena brutto wynosi {gross_price}")

