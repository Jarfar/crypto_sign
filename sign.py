from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5


key = RSA.generate(1024)

kf = open('closed.pem', 'wb')
kf.write(key.exportKey('PEM'))
kf.close()

with open('message.txt', 'rb') as f:
    message = f.read()
    h = SHA.new(message)

signature = PKCS1_v1_5.new(key).sign(h)
with open('signature.pem', 'wb') as f:
    f.write(signature)


pubkey = key.publickey()

with open('pubkey.pem', 'wb') as f:
    f.write(pubkey.exportKey('PEM'))

print(PKCS1_v1_5.new(pubkey).verify(h, signature))
