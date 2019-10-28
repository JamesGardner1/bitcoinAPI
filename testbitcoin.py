import unittest
for unittest import TestCase
from unittest.mock import patch


import bitcoin

class TestExchangeRates(TestCase):

    @patch('exchange')