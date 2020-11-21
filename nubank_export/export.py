import datetime
import json
import csv
import logging.config
import os
import base64

from pynubank import Nubank, MockHttpClient
from dotenv import load_dotenv
load_dotenv()


def setup_logging(filename):
    try:
        with open(filename) as f:
            config = json.loads(f.read())
            logging.config.dictConfig(config)
        return True
    except FileNotFoundError:
        print('Missing logging.json, logging not configured.')
        return False


NUBANK_TOKEN = os.getenv('NUBANK_TOKEN')
NUBANK_CERT = os.getenv('NUBANK_CERT')


def clean(transaction):
    print(transaction)
    transaction["detail"] = transaction['detail'].split(' - ')[0]
    if "amount" in transaction:
        transaction["amount"] = '{:.2f}'.format(
            transaction['amount']).replace('.', ',')
    return transaction.values()


if __name__ == '__main__':
    log_config_file = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'logging.json')
    setup_logging(log_config_file)

    logging.info('Initializen Nubank export')

    nu = Nubank()
    nu.authenticate_with_refresh_token(NUBANK_TOKEN, NUBANK_CERT)

    account_transactions = nu.get_account_feed()
    logging.info(f'Found {len(account_transactions)} account transactions')

    with open('export.csv', mode='w', encoding='utf-8') as tfile:
        fieldnames = ['id', '__typename', 'title',
                      'detail', 'postDate', 'amount', 'originAccount', 'destinationAccount']
        writer = csv.DictWriter(tfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)

        data = list(map(lambda t: clean(t), account_transactions))
        writer.writeheader()
        writer.writerows(account_transactions)
