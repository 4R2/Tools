#!/usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input("[*] Enter Sha1 Hash Value: ")

passlist = str(urlopen('https://raw.githubusercontent.com/iryndin/10K-Most-Popular-Passwords/refs/heads>

for password in passlist.split('\n'):
        hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
        if hashguess == sha1hash:
                print (colored("[+] Yay, Found ---> " + str(password),'green'))
                quit()
        else:
                print (colored("[-] Password guess ---> " +str(password) + " ---- does not match, tryin>

print ("Password not in passwordlist")
