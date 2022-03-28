def get_value_from_user(prompt):
    try:
        value = int(input(prompt))
    except ValueError:
        print("nieprawidlowa wartosc, podaj jeszcze raz")
        value = get_value_from_user(prompt)
    return value


def calculate_gross_price(net_value, vat_value):
    return net_value + (net_value * vat_value / 100)


if __name__ == "__main__":
    net_price = get_value_from_user("podaj cene netto: ")
    vat_rate = get_value_from_user("podaj wartosc vat: ")
    gross_price = calculate_gross_price(net_price, vat_rate)
    print(f"cena brutto wynosi {gross_price}")
