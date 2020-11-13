import hashlib
import time
#este .py debe estar acompañado de los textoplanos obtenidos despues de ser crackeados para rehashearlos con sha3_224
m = hashlib.sha3_224()
time1 = time.time()
with open("textoplano1.txt") as fp: 
    f = open("rehash1.txt", "w")
    for line in fp: 

        text = line.strip()
        m.update(text.encode('utf8'))
        f.write(m.hexdigest() + "\n")
    
    f.close()
time2 = time.time()
with open("textoplano2.txt") as fp: 
    f = open("rehash2.txt", "w")
    for line in fp: 

        text = line.strip()
        m.update(text.encode('utf8'))
        f.write(m.hexdigest() + "\n")
    
    f.close()
time3 = time.time()
with open("textoplano3.txt") as fp: 
    f = open("rehash3.txt", "w")
    for line in fp: 

        text = line.strip()
        m.update(text.encode('utf8'))
        f.write(m.hexdigest() + "\n")
    
    f.close()
time4 = time.time()
with open("textoplano4.txt") as fp: 
    f = open("rehash4.txt", "w")
    for line in fp: 

        text = line.strip()
        m.update(text.encode('utf8'))
        f.write(m.hexdigest() + "\n")
    
    f.close()
time5 = time.time()
with open("textoplano5.txt") as fp: 
    f = open("rehash5.txt", "w")
    for line in fp: 

        text = line.strip()
        m.update(text.encode('utf8'))
        f.write(m.hexdigest() + "\n")
    
    f.close()
time6 = time.time()

tarchivo1 = time2 - time1 
tarchivo2 = time3 - time2 
tarchivo3 = time4 - time3 
tarchivo4 = time5 - time4 
tarchivo5 = time6 - time5 


f = open("rehashtimes.txt", "w")
f.write('tiempo archivo1 = '+ str(tarchivo1) + '\n' + 'tiempo archivo2 = '+ str(tarchivo2) + '\ntiempo archivo3 = '+ str(tarchivo3) + '\ntiempo archivo4 = '+ str(tarchivo4) + '\ntiempo archivo5 = '+ str(tarchivo5))
f.close()