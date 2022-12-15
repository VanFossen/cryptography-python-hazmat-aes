import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

p_flag = False

# setup
key = os.urandom(32)
iv = os.urandom(16)
print(f"key: \n  {key}")
print(f"key length: \n  {len(key)}")
print(f"iv: \n  {iv}")
print(f"iv length: \n  {len(iv)}")
print()


plaintext = b"Hello, World!"
print(f"plaintext: \n  {plaintext}")
print(f"plaintext length: \n  {len(plaintext)}")
print()


if len(plaintext) < 16:
    # add padding
    p_flag = True
    padder = padding.ANSIX923(128).padder()
    plaintext = padder.update(plaintext)
    plaintext += padder.finalize()
    print(f"padded message: \n  {plaintext}")
    print(f"planned message length: \n  {len(plaintext)}")
    print()


# encryption
enc_cypher = Cipher(algorithms.AES256(key), modes.CBC(iv))
encryptor = enc_cypher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
print(f"ciphertext: \n  {ciphertext}")
print(f"ciphertext length: \n  {len(ciphertext)}")
print()


# decryption
dec_cypher = Cipher(algorithms.AES(key), modes.CBC(iv))
decryptor = dec_cypher.decryptor()
cleartext = decryptor.update(ciphertext) + decryptor.finalize()
print(f"cleartext: \n  {cleartext}")
print(f"cleartext length: \n  {len(cleartext)}")
print()

if p_flag:
    # remove padding
    unpadder = padding.ANSIX923(128).unpadder()
    cleartext = unpadder.update(cleartext)
    cleartext = cleartext + unpadder.finalize()
    print(f"unpadded message: \n  {cleartext}")
    print(f"unplanned message length: \n  {len(cleartext)}")
    print()
