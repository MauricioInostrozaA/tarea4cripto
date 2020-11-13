import socket, pickle
import random
import Rabin
from Crypto.Util.number import *
import codecs
import Crypto
from Crypto import Random
import sqlite3

################## DB STUFF ############################
cdb = sqlite3.connect('database_t4.sqlite')
cur = cdb.cursor()

# Crear Tabla (Ejecutar solo la primera vez) ###########
#cur.execute('CREATE TABLE SavedHashes (hash VARCHAR)')
#cdb.commit()
#-------------------------------------------------------

def Decryption(data, p, q):
    plaintext = Rabin.decryption(data, p, q)
    st=format(plaintext, 'x')
    return(st)

########################################################
bits=512
msg="hello"
#################### ALGORITHM #########################
if (len(sys.argv)>1):
    msg=str(sys.argv[1])
if (len(sys.argv)>2):
    bits=int(sys.argv[2])

while True:
    p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    if ((p % 4)==3): break

while True:
    q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    if ((p % 4)==3): break
 
n = p*q
p = int(p)
q = int(q)

print(("\n=== TEMPORAL OUTPUT OF Private key (%d bit prime numbers) ===") % bits)
print(("p = %d, q = %d") % (p,q))

print("\n=== Public key For Encyption ===")

print("n = %d" %  n)
################## FILENAME ############################
filename = "decryptfile5.txt"
f = open(filename, "w+")
########################################################
print("Server is Listening.....")
HOST = 'localhost'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)
conn, addr = s.accept()
print('Connected by', addr)
conn.send(b"Public key: " + str(n).encode())
#conn.send(str(n).encode())
while True:
    decoded_data = b''
    data = conn.recv(4096)
    if data == b'':
        print('Confirm -Finished- from Client' )
        break

    else:
        data_len = int(data[:10])
        decoded_data += data


        if len(decoded_data) - 10  == data_len:
            ciphertext = str(pickle.loads(decoded_data[10:]))
            plaintext = Decryption(int(ciphertext), p, q)
            str_plaintext = bytes.fromhex(plaintext).decode()
            print(str_plaintext)
            
            ######################## DB STUFF ######################
            cur.execute('INSERT INTO SavedHashes (hash) VALUES (?)', (str_plaintext,))
            cdb.commit()
            ########################################################

            f.write(str_plaintext + '\n')

print('Data received from client')