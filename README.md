# cryptography-python-hazmat-aes

The following program implements the [`pyca/cryptography`](https://cryptography.io/) library to do the following:

1. Generate a symmetric key and iv for AES-256-CBC.
2. (optional) Add padding if message is less than 128-bits.
3. Encrypt plaintext message.
4. Decrypt ciphertext message.
5. (optional) Remove padding if message was less than 128-bits.

---

This small examples shows how to:

- generate an AES key
- perform symmetric encryption and decryption

---

## Virtual Environment Setup:

```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
pip3 install cryptography
```
