from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


with open('message.txt', 'rb') as f:
    message = f.read()
    h = SHA.new(message)

with open('signature.pem', 'rb') as f:
    signature=f.read()

with open('pubkey.pem', 'rb') as f:
    pubkey = RSA.importKey(f.read())

if PKCS1_v1_5.new(pubkey).verify(h, signature):
    print('проверка пройдена')
else: print('ты че дядя')