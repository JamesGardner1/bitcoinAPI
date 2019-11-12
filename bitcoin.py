import requests


def main():
    bitcoin = get_bitcoin_amount()
    converted = convert_bitcoin_to_dollars(bitcoin)
    display_results(bitcoin, converted)

def get_bitcoin_amount():
    ''' Get Bitcoin Value '''
    return int(input('How much bitcoin do you possess?'))


def convert_bitcoin_to_dollars(bitcoin):
    exchange_rate = get_exchange_rate()
    converted = convert(bitcoin, exchange_rate)
    return converted

def get_exchange_rate():
    response = request_rates()
    rate = extract_rate(response)
    return rate

def request_rates():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    return requests.get(url).json()

def extract_rate(rates):
    print(rates)
    return rates['bpi']['USD']['rate_float']

def convert(bitcoin, exchange_rate):
    ''' Convert bitcoin to USD '''
    return bitcoin * exchange_rate

def display_results(bitcoin, converted):
    ''' Format and Display results. '''
    print(f'{bitcoin} bitcoin is equal to {converted:.2f} USD!')

main()