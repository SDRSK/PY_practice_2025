import requests

link = "https://api.monobank.ua/bank/currency"

try:
    response = requests.get(link)

    if response.status_code == 200:
        data = response.json()

        for item in data:
            if item["currencyCodeA"] == 840 and item["currencyCodeB"] == 980:
                rate_buy = item.get("rateBuy", "Немає даних")
                rate_sell = item.get("rateSell", "Немає даних")
                print(f"Курс USD -> UAH:\n Купівля: {rate_buy}\n Продаж: {rate_sell}")
                break
    else:
        print(f"Помилка: статус-код {response.status_code}")

except requests.exceptions.RequestException as e:
    print("Сталася помилка при запиті:", e)
