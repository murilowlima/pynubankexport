Exporte os lançamentos da Nuconta com este script Python. ([Utilizando a biblioteca pynubank](https://github.com/andreroggeri/pynubank))


## Utilização

A autenticação é feita utilizando certificado (a mesma utilizada pelo app). [Mais informações](https://github.com/andreroggeri/pynubank/blob/master/examples/login-certificate.md)

1. Primeiro devemos utilizar o script cli.py [(acessar aqui)](https://github.com/andreroggeri/pynubank/blob/master/pynubank/cli.py) para gerar o certificado. Atenção: não compartilhe este arquivo de certiticado com ningúem.

2. Com o aqruivo de certificado devemos obter o **refresh token**. Este token nos permitirá fazer várias requisições ao Nubank, sem que nossa conta seja bloqueada. Para isto executar o script [get_token.py](https://github.com/murilowlima/pynubankexport/blob/main/nubank_export/get_token.py).

3. Com o **refresh token** podemos, então, executar o script [export.py](https://github.com/murilowlima/pynubankexport/blob/main/nubank_export/export.py). Os dados, atualmente, estão indo para a tel e para o arquivo de log (export.log).    


## Contribuindo

Me envie uma mensagem ou PR!