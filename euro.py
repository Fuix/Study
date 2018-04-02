
def cur(money):
    usd = 57
    euro = 60

    currency = int(input('Укажите код валюты(Доллары-400, Евро-401):'))

    if currency == 400:
        cache = round(money / usd, 2)
        print('Валюта: Доллары США')
    elif currency == 401:
        cache = round(money / euro, 2)
        print('Валюта: Евро')
    else:
        cache = 0
        print('Неизвестная валюта')
    return cache