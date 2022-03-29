def get_price_from_user():
    try:
        value = float(input("podaj wartosc w zlotych: "))
    except ValueError:
        print("nieprawidlowa wartosc, podaj jeszcze raz")
        value = get_price_from_user()
    return value


def get_currency_from_user():
    value = input("podaj walute e/d: ")
    if value == "e" or value == "d":
        return value
    print("nieprawidlowa wartosc, podaj e/d: ")
    return get_currency_from_user()


def calculate_price(currency, pln_price):
    if currency == "e":
        return pln_price * 0.22
    if currency == "d":
        return pln_price * 0.25


if __name__ == "__main__":
    pln_price = get_price_from_user()
    currency = get_currency_from_user()
    calculated_value = calculate_price(currency, pln_price)
    print(f"obliczona wartosc wynosi {calculated_value}")
