import socket, pickle
import random
import Rabin
from Crypto.Util.number import *
import codecs
import Crypto
from Crypto import Random
import time
#Este .py debe estar acompañado de los archivos que se desean encriptar.
def Encryption(data, n):
    plaintext =  bytes_to_long(data.encode('utf-8'))
    ciphertext = Rabin.encryption(plaintext, n)
    return(ciphertext)

HOST = 'localhost'
PORT = 50007
# Create a socket connection.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
########################################################
hashfile = "rehash5.txt"
########################################################
publickey = s.recv(2024)
n = int(publickey.decode()[12:])
############ ENCRYPT FILE ##############################
with open(hashfile) as f:
    for lines in f:
        line = lines.strip()
        if line!= '' and line != '\n':
            data = line
            print('----------------------------------------------------------------------------------')
            cipher = Encryption(data, n)
            print(cipher)

            data_to_send = pickle.dumps(cipher)
            #adding header
            data_2 = bytes(f'{len(data_to_send):<{10}}', 'utf-8') + data_to_send
            s.send(data_2)
            time.sleep(0.5)
        else:
            break


#######
opt = input("Enter a [0] to finish: ")
if (opt == 0):
    s.send('-------------------------end------------------------')
    print('Data Sent to Server')
    s.close()
#######

print('Data Sent to Server')