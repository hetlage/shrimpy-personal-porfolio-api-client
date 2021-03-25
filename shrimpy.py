# sample script for 
# import required libraries
import shrimpy
import time

# assign your Shrimpy API keys for later use
shrimpy_public_key = 'your_public_key'
shrimpy_secret_key = 'your_secret_key'

# create the Shrimpy client
client = shrimpy.ShrimpyApiClient(shrimpy_public_key, shrimpy_secret_key)

""" Test API methods """
# print(client.get_ticker('binance')) # Must be one of the following: "binance", "bittrex", "coinbasepro", "kraken", "kucoin", or "poloniex"
# print(client.list_accounts(exchange_acct_id)) #integer
# print(client.get_account(exchange_acct_id))
# print(client.get_balance(exchange_acct_id)
# print(client.rebalance(exchange_acct_id))
# print(client.get_portfolios(exchange_acct_id))
# allocations = [{"symbol":"USDT", "percent":"100"}]
# print(client.create_portfolio(exchange_acct_id, "Api Test", allocations))
# print(client.update_portfolio(exchange_acct_id, portfolio_id, "API Test Change", allocations)) # portfolio_id is also an integer
# print(client.activate_portfolio(exchange_acct_id, portfolio_id))
