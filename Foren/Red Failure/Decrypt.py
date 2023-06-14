from Cryptodome.Cipher import AES
import hashlib
from Cryptodome.Util.Padding import pad, unpad
f = open('9tVI0','rb')
full_9t = f.read()
f.close()

key = "z64&Rx27Z$B%73up"
print('isi key')
print(key)
iv = full_9t[:16]
ciphertext = full_9t[16:]

hashed_str = bytearray(hashlib.sha256(key.encode('utf-8')).digest())

g = open('keyNew99','wb')
g.write(hashed_str)
g.close()

cipher = AES.new(hashed_str, AES.MODE_CBC, iv=iv)
plaintext = unpad(cipher.decrypt(ciphertext), 16)

print('isi plaintext')
# print(plaintext)

f = open('resultPycryptoWithPadding','wb')
f.write(plaintext)
f.close()