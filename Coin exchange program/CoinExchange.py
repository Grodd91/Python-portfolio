import requests

def swap_on_uniswap(token_in, token_out, amount_in, gas_price, slippage, min_received):
    # Set up the API request to Uniswap
    url = "https://api.uniswap.org/api/v1/exchange"
    payload = {
        "tokenIn": token_in,
        "tokenOut": token_out,
        "amountIn": amount_in,
        "gasPrice": gas_price,
        "slippage": slippage,
        "minimumReceived": min_received
    }

    # Send the request to Uniswap
    response = requests.get(url, params=payload)
    # Process the response
    # ...

def swap_on_1inch(token_in, token_out, amount_in, gas_price, slippage, min_received):
    # Set up the API request to 1inch
    url = "https://api.1inch.exchange/v3.0/swap"
    payload = {
        "fromTokenAddress": token_in,
        "toTokenAddress": token_out,
        "amount": amount_in,
        "gasPrice": gas_price,
        "slippage": slippage,
        "minReturn": min_received
    }

    # Send the request to 1inch
    response = requests.post(url, json=payload)
    # Process the response
    # ...

# Example usage
token_in = "0xTokenIn"
token_out = "0xTokenOut"
amount_in = 1.0
gas_price = 100
slippage = 1.0
min_received = 0.9

# Swap on Uniswap
swap_on_uniswap(token_in, token_out, amount_in, gas_price, slippage, min_received)

# Swap on 1inch
swap_on_1inch(token_in, token_out, amount_in, gas_price, slippage, min_received)

