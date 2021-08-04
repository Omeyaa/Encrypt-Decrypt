from cryptography import fernet
from cryptography.fernet import Fernet
import os


def load_file(filename):
    # loads a key
    return open(filename, 'rb').read()


# encrypt file
def encrypt_file(filename, key):
    f = Fernet(key)

    with open(filename, 'rb') as file:
        # read all file data
        file_data = file.read()

    # encrypt data
    encrypted_data = f.encrypt(file_data)

    # write the encrypted file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)

# decrypt file


def decrypt_file(filename, key):
    f = Fernet(key)

    with open(filename, 'rb') as file:
        # read the encrypted data
        encrypted_data = file.read()

    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)

    # write the original file
    with open(filename, 'wb') as file:
        # write data
        file.write(decrypted_data)


while(True):
    os.system('cls')
    print("""-----------Encrypt/Decrypt-----------
[ 1 ] Encrypt File
[ 2 ] Decrypt File
[ 3 ] Exit   
    """)
    q = input("Enter Number : ")
    if q == '1':
        filename = input("Enter Filename : ")
        keyfile = input("Enter Key File : ")
        load_key_file = load_file(keyfile)
        encrypt_file(filename, load_key_file)
        print("Successfully Encrypt the File")
        break
    elif q == '2':
        filename = input("Enter Filename : ")
        keyfile = input("Enter Key File : ")
        load_key_file = load_file(keyfile)
        decrypt_file(filename, load_key_file)
        print("Successfully Decrypt the File")
        break
    elif q == '3':
        break
