import requests
import json
from urllib.parse import urlencode
from shrimpy.auth_provider import AuthProvider


class ShrimpyApiClient():
    """Authenticated access to the Shrimpy Developer API"""

    def __init__(self, key, secret, timeout=300):
        self.url = 'https://api.shrimpy.io/v1/'
        self.auth_provider = None
        self.timeout = timeout
        if (key and secret):
            self.auth_provider = AuthProvider(key, secret)
        self.session = requests.Session()

    ###############
    # Market Data #
    ###############

    def get_ticker(self, exchange):
        endpoint = '{}/ticker'.format(exchange)
        return self._call_endpoint('GET', endpoint)

    ############
    # Accounts #
    ############

    def list_accounts(self):
        endpoint = 'accounts'
        return self._call_endpoint('GET', endpoint)

    def get_account(self, exchange_account_id):
        endpoint = 'accounts/{}'.format(exchange_account_id)
        return self._call_endpoint('GET', endpoint)

    ###########
    # Trading #
    ###########

    ## Balances

    def get_balance(self, exchange_account_id):
        endpoint = 'accounts/{}/balance'.format(exchange_account_id)
        return self._call_endpoint('GET', endpoint)

    ## Asset Management

    def rebalance(self, exchange_account_id):
        endpoint = 'accounts/{}/rebalance'.format(exchange_account_id)
        return self._call_endpoint('POST', endpoint)

    ## Strategies 

    def get_portfolios(self, exchange_account_id):
        endpoint = 'accounts/{}/portfolios'.format(exchange_account_id)
        return self._call_endpoint('GET', endpoint)

    def create_portfolio(self, exchange_account_id, porfolio_name, allocations, rebalance_period=0, is_dynamic=False,
                         strategy_trigger='interval', rebalance_threshold='1', max_spread='10', max_slippage='10'):
        endpoint = 'accounts/{}/portfolios/create'.format(exchange_account_id)
        data = {
            'name': porfolio_name,
            'rebalancePeriod': rebalance_period,  # integer in hours, must be zero to use threshold trigger
            'strategy': {
                'isDynamic': is_dynamic,
                'allocations': allocations,  # must be a list of dictionaries
            },
            'strategyTrigger': strategy_trigger,  # either "interval" or "threshold"
            'rebalanceThreshold': rebalance_threshold,  # percent deviation for rebalance operation
            'maxSpread': max_spread,
            'maxSlippage': max_slippage
        }
        return self._call_endpoint('POST', endpoint, data=data)

    def update_portfolio(self, exchange_account_id, portfolio_id, porfolio_name, allocations, rebalance_period=0,
                         is_dynamic=False, strategy_trigger='interval', rebalance_threshold='1', max_spread='10',
                         max_slippage='10'):
        endpoint = 'accounts/{}/portfolios/{}/update'.format(exchange_account_id, portfolio_id)
        data = {
            'name': porfolio_name,
            'rebalancePeriod': rebalance_period,  # integer in hours, must be zero to use threshold trigger
            'strategy': {
                'isDynamic': is_dynamic,
                'allocations': allocations,  # must be a list of dictionaries
            },
            'strategyTrigger': strategy_trigger,  # either "interval" or "threshold"
            'rebalanceThreshold': rebalance_threshold,  # percent deviation for rebalance operation
            'maxSpread': max_spread,
            'maxSlippage': max_slippage
        }
        return self._call_endpoint('POST', endpoint, data=data)

    def activate_portfolio(self, exchange_account_id, portfolio_id):
        endpoint = 'accounts/{}/portfolios/{}/activate'.format(exchange_account_id, portfolio_id)
        return self._call_endpoint('POST', endpoint)

    ###########
    # Helpers #
    ###########

    def _call_endpoint(self, method, endpoint, params=None, data=None):
        url = self.url + endpoint
        if data is not None:
            data = json.dumps(data)

        api_request = self.session.request(
            method,
            url,
            params=params,
            data=data,
            auth=self.auth_provider,
            timeout=self.timeout
        )

        return api_request.json()

    def _create_query_string(self, endpoint, params):
        return endpoint + '?' + urlencode(params)

    def _add_param_or_ignore(self, params, key, value):
        if value is not None:
            params[key] = value
