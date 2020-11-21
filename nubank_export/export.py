import datetime
import json
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

if __name__ == '__main__':
    log_config_file = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'logging.json')
    setup_logging(log_config_file)

    logging.info('Initializen Nubank export')

    nu = Nubank()
    nu.authenticate_with_refresh_token(NUBANK_TOKEN, NUBANK_CERT)

    #credit_transactions = nu.get_card_feed()
    #logging.info(f'Found {len(credit_transactions)} credit transactions')

    account_transactions = nu.get_account_feed()
    logging.info(f'Found {len(account_transactions)} account transactions')
    logging.info(account_transactions)
