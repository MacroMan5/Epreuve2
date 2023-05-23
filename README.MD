# CTF Flag et Déchiffrement XOR

Ce CTF (Capture The Flag) présente un défi de déchiffrement utilisant l'opération XOR. Le défi consiste à déchiffrer un message chiffré en base 64 pour obtenir le message ensuite en XOR. Il faudra utilisé la clé obtenu précedement pour déchiffrer le message XOR. 


## Déchiffrement XOR

Pour déchiffrer le message chiffré avec XOR, vous pouvez utiliser la fonction de déchiffrement `xor_decode(message, key)`. Voici un exemple en Python :

```python
# Fonction pour déchiffrer un message avec XOR
def xor_decode(message, key):
    return "".join(chr(ord(c) ^ key) for c in message)

# Supposons que vous ayez le message chiffré et la clé XOR
message_chiffre = "..."
key = ... # Clé sera donné dans le défi

# Déchiffrez le message
message_dechiffre = xor_decode(message_chiffre, key)

print(message_dechiffre)



## Remarque importante
Il est essentiel de comprendre que ce défi de déchiffrement XOR est à des fins éducatives et de divertissement, et il n'est pas recommandé d'utiliser XOR seul comme mécanisme de chiffrement sécurisé dans un contexte réel. XOR simple n'est pas suffisant pour garantir une sécurité adéquate.