from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')



shared_secret = "2249074055540051940156177263468474344647546579317702092844048968446717298994613396737978462662731404077067345274555420714130131090761293338229924235385671986847515917714142759600816218454676717542318831707101175186158225150598214867479752906948385533024631468423223903150936486422361591719430377545087236663777550332323867814492392464947095767614053782711308234398883017981877166973749207095314193854674886145380435021853882067931068240852009264789978430690285207"
iv =  "7460b5a275ff946ccacbde509a848f95"
encrypted = "d7bb4d71f17265ed1e55ece2a1c5ec5f34809867bdab8888478d87470b356ce9572eb5836d23fccb92f19a3446163a3b"

print(decrypt_flag(shared_secret, iv, encrypted))
