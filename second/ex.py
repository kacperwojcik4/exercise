if __name__ == "__main__":
    pln_price = float(input("podaj wartosc w zlotych: "))
    currency = input("podaj walute e/d: ")
    if currency == "e":
        calculated_value = pln_price * 0.22
        print(f"wartosc w euro wynosi {calculated_value}")

    if currency == "d":
        calculated_value = pln_price * 0.25
        print(f"watosc w dolarach wynosi {calculated_value}")
