import crypto
import sys
from Crypto.Cipher import DES

sys.modules['Crypto'] = crypto
key = b'absdefgh'


def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text


des = DES.new(key, DES.MODE_ECB)
text = b'Python rocks!'
padded_text = pad(text)

encrypted_text = des.encrypt(padded_text)
print(encrypted_text)

# import hashlib
# import binascii
#
#
# dk = hashlib.pbkdf2_hmac(
#     hash_name='sha256',
#     password=b'bad_password34',
#     salt=b'bad_salt',
#     iterations=100000
# )
# result = binascii.hexlify(dk)
# print(result)

# result = hashlib.md5(b'Python rocks!').hexdigest()
# result2 = hashlib.md5(b'Python rocks!').digest()
# sha = hashlib.sha1(b'Hello Python').hexdigest()
#
# print(result)
# print(result2)
# print(sha)
