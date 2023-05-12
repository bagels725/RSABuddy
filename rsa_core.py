# Copied from section.io/engineering-education/rsa-encryption-and-decryption-in-python/
# Most of this code likely won't be implemented in the real RSABuddy program. This is just for reference.

import rsa

def generateKeys():
  (publicKey, privateKey) = rsa.newkeys(1024)
  with open('keys/publicKey.pem', 'wb') as p:
    p.write(publicKey.save_pkcs1('PEM'))
  with open('keys/privateKey.pem', 'wb') as p:
    p.write(privateKey.savepkcs1('PEM'))
    
# Opens key files from keys folder, then returns them both.
def loadKeys():
  with open('keys/publicKey.pem', 'rb') as p:
    publicKey = rsa.PublicKey.loads_pksc1(p.read())
  with open('keys/privateKey.pem', 'rb') as p:
    privateKey = rsa.PrivateKey.loads_pksc1(p.read())
  return privateKey, publicKey

def encrypt(message, key):
  return rsa.encrypt(message.encode('ascii'), key)

def decrypt(ciphertext, key):
  try:
    return rsa.decrypt(ciphertext, key).decode('ascii')
  except:
    return False
  
def sign(message, key):
  return rsa.sign(message.encode('ascii'), key, 'SHA-1')

def verify(message, signature, key):
  try:
    return rsa.verify(message.encode('ascii'), signature, key) == 'SHA-1'
  except:
    return False

generateKeys()
publicKey, privateKey = load_keys()

message = input('Write your message here:')
ciphertext = encrypt(message, publicKey)

signature = sign(message, privateKey)

text = decrypt(ciphertext, privateKey)

print(f'Ciphertext: {Ciphertext}')
print(f'Signature: {signature}')

if text:
  print(f'Message text: {text}')
else:
  print(f'OOPS! Unable to decrypt!')

if verify(text, signature, publicKey):
  print('Signature verified!')
else:
  print ('OOPS! Unable to verify!')
