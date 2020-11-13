import os
import time

#este .py debe estar acompaño del ejecutable de hashcat, los archvios a crackear y sus diccionarios.
print('writing on console using py')
time1 = time.time()
os.system('hashcat.exe -m 0 -a 0 --outfile-format=2 -o textoplano1.txt archivo_1 diccionario_1.dict diccionario_2.dict -d 2 --potfile-disable > ch-archv1.txt')
time2 = time.time()
os.system('hashcat.exe -m 10 -a 0 --outfile-format=2 -o textoplano2.txt archivo_2 diccionario_1.dict diccionario_2.dict -d 2 --potfile-disable > ch-archv2.txt')
time3 = time.time()
os.system('hashcat.exe -m 10 -a 0 --outfile-format=2 -o textoplano3.txt archivo_3 diccionario_1.dict diccionario_2.dict -d 2 --potfile-disable > ch-archv3.txt')
time4 = time.time()
os.system('hashcat.exe -m 1000 -a 0 --outfile-format=2 -o textoplano4.txt archivo_4 diccionario_1.dict diccionario_2.dict -d 2 --potfile-disable > ch-archv4.txt')
time5 = time.time()
os.system('hashcat.exe -m 1800 -a 0 --outfile-format=2 -o textoplano5.txt archivo_5 diccionario_1.dict diccionario_2.dict -d 2 --potfile-disable > ch-archv5.txt')
time6 = time.time()

tarchivo1 = time2 - time1 
tarchivo2 = time3 - time2 
tarchivo3 = time4 - time3 
tarchivo4 = time5 - time4 
tarchivo5 = time6 - time5 


f = open("times.txt", "w")
f.write('tiempo archivo1 = '+ str(tarchivo1) + '\n' + 'tiempo archivo2 = '+ str(tarchivo2) + '\ntiempo archivo3 = '+ str(tarchivo3) + '\ntiempo archivo4 = '+ str(tarchivo4) + '\ntiempo archivo5 = '+ str(tarchivo5))
f.close()




