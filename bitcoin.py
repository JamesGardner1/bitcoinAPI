import requests


def main():
    bitcoin = get_bitcoin_amount()
    converted = convert_bitcoin_to_dollars()
    display_results(bitcoin, converted)

def get_bitcoin_amount():
    ''' Get Bitcoin Value '''
    return int(input('How much bitcoin do you possess?'))

def request_rates():
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    return data

def bitcoin_dollar_amount():
    response = request_rates()
    rate = extract_rate()
    return rate

def convert_bitcoin_to_dollars(bitcoin):
    rate = extract_rate()
    converted = convert(bitcoin, rate)
    return converted

def extract_rate():
    return data['bpi']['USD']['rate_float']

def convert(bitcoin, rate):
    ''' Convert bitcoin to USD '''
    return bitcoin * rate

def display_results(bitcoin, converted):
    ''' Format and Display results. '''
    print(f'{bitcoin} bitcoin is equal to {converted:.2f} USD!')

main()