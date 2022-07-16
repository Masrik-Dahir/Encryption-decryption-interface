import time
from datetime import datetime
import sys
import hashlib
import os
from cryptography.fernet import Fernet
if sys.version_info < (3, 6):
    import sha3

string = ""

def list_format(lis):
    string = ""
    for i in lis:
        string += str(i) + "\n"
    return string

def get_string():
    return string

def no_special_character(password: str):
    if len(password) <= 1:
        return password
    else:
        if (password[0].isdigit() or password[0].isalpha()):
            return password[0] + no_special_character(password[1:])
        else:
            return '/' + no_special_character(password[1:])

def reformat(key: str, password: str):
    password = no_special_character(password)
    key = key[:len(key)-len(password)-1] + password + key[len(key)-1]
    return key

def create_key(name: str):
    # generate the key
    key = Fernet.generate_key()
    # string the key into a file
    with open(name, 'wb') as unlock:
        unlock.write(key)

def encrypt(name: str, key: str):
    try:
        # Start timitng
        start  = time.time()

        # open the key
        with open(key, 'rb') as unlock:
            key = unlock.read()
        # print(key)

        # use the generated key
        f = Fernet(key)
        # open the original file to encrypt
        with open(name, 'rb') as original_file:
            original = original_file.read()
        # encrypt the file
        encrypted = f.encrypt(original)
        # you can write the encrypted data  file into a enc_sample.txt
        with open(name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        # end timing
        # print(name + ", encryption time: " + str(time.time() - start))
        return "Name: " + name + "\nDate: " + str(datetime.now()) + "\nKey: " + key.decode("utf-8")  + "\nencryption time: " + str(time.time() - start)
    except:
        return "Cannot encrypt"

def decrypt(name: str, key: str):
    try:
        # Start timitng
        start = time.time()


        # open the key
        with open(key, 'rb') as unlock:
            key = unlock.read()
        # print(key)

        # first use the key
        f = Fernet(key)
        # open the encrypted file
        with open(name, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        # decrypt the file
        decrypted = f.decrypt(encrypted)
        # finally you can write the decrypted file into a dec_sample.txt
        with open(name, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        # end timing
        # print(name + ", decryption time: " + str(time.time() - start))
        return "Name: " + name + "\nDate: " + str(datetime.now()) + "\nKey: " + key.decode("utf-8")  + "\ndecryption time: " + str(time.time() - start)
    except:
        return "Cannot decrypt"

def hash(name: str):
    # BUF_SIZE is totally arbitrary, change for your app!
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!

    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha224 = hashlib.sha224()
    sha256 = hashlib.sha256()
    sha384 = hashlib.sha384()
    sha512 = hashlib.sha512()


    with open(name, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha224.update(data)
            sha256.update(data)
            sha384.update(data)
            sha512.update(data)

    str = "MD5: {0}".format(md5.hexdigest()) + \
          "\nSHA1: {0}".format(sha1.hexdigest()) + \
          "\nsha224: {0}".format(sha224.hexdigest()) + \
          "\nsha256: {0}".format(sha256.hexdigest()) + \
          "\nSHA384: {0}".format(sha384.hexdigest()) + \
          "\nsha512: {0}".format(sha512.hexdigest())

    return str

def encrypt_by_password(name: str, key: str):
    root_dir = os.getcwd()
    randommm = open(str(root_dir) + '\\secret.txt')
    data1 = randommm.read()
    val = str(data1.split('\n')[1])

    try:
        # Start timitng
        start  = time.time()

        f = Fernet(reformat(val, key))

        with open(name, 'rb') as original_file:
            original = original_file.read()
        # encrypt the file
        encrypted = f.encrypt(original)
        # you can write the encrypted data  file into a enc_sample.txt
        with open(name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        # end timing
        # print(name + ", encryption time: " + str(time.time() - start))
        return "Name: " + name + "\nDate: " + str(datetime.now()) + "\nKey: " + str(reformat(val, key)) + "\nencryption time: " + str(time.time() - start)
    except:
        return "Cannot encrypt"

def decrypt_by_password(name: str, key: str):
    root_dir = os.getcwd()
    randommm = open(str(root_dir) + '\\secret.txt')
    data1 = randommm.read()
    val = str(data1.split('\n')[1])

    try:
        # Start timitng
        start  = time.time()

        f = Fernet(reformat(val, key))

        # open the encrypted file
        with open(name, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        # decrypt the file
        decrypted = f.decrypt(encrypted)
        # finally you can write the decrypted file into a dec_sample.txt
        with open(name, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        # end timing
        # print(name + ", decryption time: " + str(time.time() - start))
        return "Name: " + name + "\nDate: " + str(datetime.now()) + "\nKey: " + str(reformat(val, key)) + "\ndecryption time: " + str(time.time() - start)
    except:
        return "Cannot decrypt"

def token(password: str):
    root_dir = os.getcwd()
    f = open(str(root_dir) + '\\secret.txt')
    data = f.read()
    pasw = data.split('\n')[0]
    a = str(password) + pasw
    key = bytes(a, 'utf-8')
    f = Fernet(key)
    return f

def all_files(directory: str):
    try:
        string = ""
        # create a list of file and sub directories
        # names in the given directory
        listOfFile = os.listdir(directory)
        allFiles = list()
        # Iterate over all the entries
        for entry in listOfFile:
            # Create full path
            fullPath = os.path.join(directory, entry)
            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(fullPath):
                allFiles = allFiles + all_files(fullPath)
            else:
                allFiles.append(fullPath)

        return allFiles
    except:
        return ""

def encrypt_max(directory: str, key: str):
    string = ""
    files = all_files(directory)
    for i in files:
        string += str(encrypt(i, key)) + "\n\n"
    return string

def decrypt_max(directory: str, key: str):
    string = ""
    files = all_files(directory)
    for i in files:
        string += str(decrypt(i, key)) + "\n\n"
    return string

def password_encrypt_max(directory: str, key: str):
    string = ""
    files = all_files(directory)
    for i in files:
        string += str(encrypt_by_password(i, key)) + "\n\n"
    return string

def password_decrypt_max(directory: str, key: str):
    string = ""
    files = all_files(directory)
    for i in files:
        string += str(decrypt_by_password(i, key)) + "\n\n"
    return string
