#!/usr/bin/python

from termcolor import colored
import hashlib
import sys


def tryOpen(pass_file):

        global file

        if len(sys.argv) != 2:
                print("Usage: python3 md5bryte.py <path_to_passwords_file>")
                sys.exit(1)
        try:
                pass_file = sys.argv[1]
                file = open(pass_file, "r")
                print("Processing file: " + pass_file)
        except:
                print ("[!!] NO such file at PATH: " + pass_file )
                quit()

pass_file = ""
tryOpen(pass_file)

pass_hash = input("[*] Enter MD5 Hash Value: ")

for word in file:
        print (colored("[*] Trying: " + word.strip("\n"), 'red'))
        enc_word = word.encode('utf-8')
        md5_digest = hashlib.md5(enc_word.strip()).hexdigest()

        if md5_digest == pass_hash:
                print(colored("[+] Found: " + word,'green'))
                exit(0)

print ("[!!] Password not in the list!")
