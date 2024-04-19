
import requests

def convert_currency(amount, from_currency, to_currency):
    api_key = "API_KEY_HERE" # ENTER YOUR API KEY HERE
    url = f"https://api.currencyscoop.com/v1/convert?api_key={api_key}&from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    data = response.json()
    if 'response' in data and 'value' in data['response']:
        converted_amount = data['response']['value']
        return converted_amount
    else:
        print("Error: Failed to retrieve conversion data")
        return None

def main():
    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the currency to convert from (e.g. USD): ")
    to_currency = input("Enter the currency to convert to (e.g. EUR): ")
    converted_amount = convert_currency(amount, from_currency, to_currency)
    if converted_amount is not None:
        print(f"{amount:.2f} {from_currency} to {to_currency}: {converted_amount:.2f}")

if __name__ == "__main__":
    main()
