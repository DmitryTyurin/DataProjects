# Одной из базовых банковских услуг является обмен валют.
#
# Написать функцию convert, которая умеет конвертировать доллар в другую валюту и наоборот. Для конвертации используются текущие курсы валют, которые хранятся в глобальном словаре exchange_rates.
#
# Результат округлите до двух знаков после запятой при помощи функции round


def convert(from_currency: str, to_currency: str, amount: [int | float]):
    global exchange_rates

    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        return "Invalid currency"

    from_rate = exchange_rates[from_currency]
    to_rate = exchange_rates[to_currency]

    converted_amount = round(amount * (to_rate / from_rate), 2)

    return converted_amount


exchange_rates = {
    "USD": 1.0,
    "EUR": 0.861775,
    "GBP": 0.726763,
    "INR": 75.054725,
    "AUD": 1.333679,
    "CAD": 1.237816,
    "SGD": 1.346851,
}