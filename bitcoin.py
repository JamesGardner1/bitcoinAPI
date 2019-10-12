import requests



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