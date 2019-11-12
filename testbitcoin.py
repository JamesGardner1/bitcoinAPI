import unittest
for unittest import TestCase
from unittest.mock import patch


import bitcoin

class TestExchangeRates(TestCase):

    @patch('bitcoin.request_rates')
    def test_bitcoin_to_dollars(self, mock_rates)
    mock_rate = 8753.8467
    example_api_response = {'bpi': 'USD', 'rate_float': {'USD': mock_rate}}
    mock_rate.side_effect = [ example_api_response ]
    converted = exchange_rate.convert_bitcoin_to_dollars(4)
    self.assertEqual(35015.39, converted)