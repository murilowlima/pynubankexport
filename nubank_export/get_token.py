from pynubank import Nubank
import os

from dotenv import load_dotenv
load_dotenv()

NUBANK_CERT = os.getenv('NUBANK_CERT')

WARN = "Atenção: Utilizar apenas para obter o refresh token. Não utilizar com frequência, pois o Nubank pode bloquear sua conta."

if __name__ == '__main__':
    print(WARN)
    username = input('[>] Type your CPF: ')
    password = input('[>] Type your password: ')

    nu = Nubank()
    refresh_token = nu.authenticate_with_cert(username, password, NUBANK_CERT)
    print(refresh_token)
