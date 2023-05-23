import base64
import os
from config import key
# Flag et message chiffré
flag = "01253{X0R_3nc0d1ng_1s_aw3s0me}"

# Fonction pour encoder un message en base64 plusieurs fois
def encode_repeatedly(message, num_repetitions):
    encoded_message = message.encode('utf-8')
    for i in range(num_repetitions):
        encoded_message = base64.b64encode(encoded_message)
    return encoded_message


# Fonction pour encoder un message avec XOR
def xor_encode(message, key):
    return "".join(chr(ord(c) ^ key) for c in message)

# Générer une clé le XOR
key = key

# Encode le message chiffré avec XOR
xor_encoded_message = xor_encode(flag, key)

N = 35
# Encode le message en base64 N fois
encoded_message = encode_repeatedly(xor_encoded_message, N)

with open('cipher.txt', 'wb') as f:
    f.write(encoded_message)
    f.close()