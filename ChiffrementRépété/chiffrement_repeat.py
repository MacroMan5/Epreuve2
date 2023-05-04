#!/usr/bin/env python3
import base64

message_clair = "01253{b@se64_l00ps_4re_fun} Félicitations ! Vous avez déchiffré le message. La prochaine étape consiste à vous connecter à cette page web ..........  Une fois sur cette page, votre mission sera de vous connecter en tant qu'administrateur et de trouver un fichier contenant les informations sur un serveur. Ensuite, accédez à ce serveur et trouvez les fichiers top secrets. Bonne chance !"

# Fonction pour encoder un message en base64 plusieurs fois
def encode_repeatedly(message, num_repetitions):
    encoded_message = message.encode('utf-8')
    for i in range(num_repetitions):
        encoded_message = base64.b64encode(encoded_message)
    return encoded_message

N = 35
# Encodez le message en base64 N fois
encoded_message = encode_repeatedly(message_clair, N)

with open ('cipher.txt', 'wb') as f:
    f.write(encoded_message)
    f.close()
