import requests
import sys

if len(sys.argv) > 1:
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line arguement is not a number")
else:
    sys.exit("Missing command-line arguement")

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    request = r.json()
    results = request["bpi"]["USD"]["rate_float"]
    bitcoin_amount = n * results
    print(f"${bitcoin_amount:,.4f}")
except requests.RequestException:
    pass
