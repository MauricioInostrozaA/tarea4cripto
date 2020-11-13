# Tarea 4 Criptología 
Este repositorio contiene la siguientes carpetas:

## hcrack

Esta carpeta contiene:

* hcrack.py - Este .py debe estar acompaño del ejecutable de hashcat, los archvios a crackear y sus diccionarios.
* ch-archv(n).txt - El output por consola al crackear los archivos.
* outlife(n).txt - Los Hashes y su valor al crackearlos.
* times.txt - El tiempo que tomó crackear cada archivo

## rehash

Esta carpeta contiene:

* rehashing.py - Este .py debe estar acompañado de los textoplanos obtenidos despues de ser crackeados para rehashearlos con sha3_224
* textoplano(n).txt - Los valores obtenidos al crackear los hashes (con hcrack.py)
* rehash(n).txt - El valor al rehashear con sha3_224.
* rehashtimes.txt - El tiempo que tomó hashear cada archivo.

## server

Esta carpeta contiene:

* server.py - Crea la connección por parte de servidor, decifra y guarda los datos en la base de datos.
* Rabin.py - Este .py contiene el algoritmo de cifrado y decifrado Rabin.
* decryptfile(n).txt - Los valores obtenidos al desencriptar los datos entregados.
* database_t4.sqlite - Los valores entregados, guardados en la base de datos.

## client

Esta carpeta contiene:

* client.py - Crea la connección por parte de cliente, cifra y manda los datos al servidor.
* Rabin.py - Este .py contiene el algoritmo de cifrado y decifrado Rabin.
* rehash(n).txt - Los valores obtenidos al rehashear (con rehashing.py)
