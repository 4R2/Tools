#!/usr/bin/python
import hashlib

print ("""*** WELCOME TO HASHER ***""")
print ("* Enter a string to hash")

hashvalue = input("* string: ")

hashobj1 = hashlib.md5()
hashobj1.update(hashvalue.encode())
print ("MD5: " + hashobj1.hexdigest())

hashobj2 = hashlib.sha1()
hashobj2.update(hashvalue.encode())
print ("SHA1: " + hashobj2.hexdigest())

hashobj3 = hashlib.sha224()
hashobj3.update(hashvalue.encode())
print ("SHA224: " + hashobj3.hexdigest())

hashobj4 = hashlib.sha256()
hashobj4.update(hashvalue.encode())
print ("SHA256: " + hashobj4.hexdigest())

hashobj5 = hashlib.sha512()
hashobj5.update(hashvalue.encode())
print ("SHA512: " + hashobj5.hexdigest())
