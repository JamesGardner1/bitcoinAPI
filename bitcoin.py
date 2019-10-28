import requests


def main():
    bitcoin = get_bitcoin_amount()
    converted = convert_bitcoin_to_dollars

def get_bitcoin_amount():
    ''' Get Bitcoin Value '''
    return int(input('How much bitcoin do you possess?'))

def request_rates():
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    return data

def bitcoin_dollar_amount():
    

def main():
    data = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
    bitValue = data['bpi']['USD']['rate_float']


    print(bitValue)

    bitcoinAmount = input('How much bitcoin do you possess?')

    bitcoin = int(bitcoinAmount)

    rate = float(bitValue)

    usConvert = bitcoin * rate

    print('That is ' + str(usConvert) + ' dollars!')



main()