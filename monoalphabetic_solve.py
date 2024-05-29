import os
import string

def generate_key(keyword):
    key = list(keyword) + list(set(string.ascii_lowercase) - set(keyword))
    return dict(zip(string.ascii_lowercase, key))
def monoalphabetic_encrypt(text, key):
    result = ""
    for char in text.lower():
        if char.isalpha():
            result += key[char]
        else:
            result += char
    return result
def monoalphabetic_decrypt(text, key):
    reversed_key = {value: key for key, value in key.items()}
    return monoalphabetic_encrypt(text, reversed_key)
def encrypt_file(filename, key):
    with open(filename, 'r') as f:
        text = f.read()
    encrypted = monoalphabetic_encrypt(text, key)
    with open(filename + '.enc', 'w') as f:
        f.write(encrypted)
def decrypt_file(filename, key):
    with open(filename, 'r') as f:
        text = f.read()
    decrypted = monoalphabetic_decrypt(text, key)
    with open(filename[:-4], 'w') as f:  # Remove '.enc' extension
        f.write(decrypted)
while True:
    print("\n===== Monoalphabetic Cipher =====")
    print("1. Enkripsi Pesan : (Encrypt Message)")
    print("2. Dekripsi Pesan : (Decrypt Message)")
    print("3. Enkripsi File : (Encrypt File)")
    print("4. Dekripsi File : (Decrypt File)")
    print("0. Keluar (Exit / quit!)")

    choice = input("Pilihan Anda : (Your choice: ) : ")

    if choice == '1':
        text = input("Masukan Pesan : (Enter message) : ")
        keyword = input("Masukan Keyword : (Enter keyword) : ").lower()
        key = generate_key(keyword)
        print("Hasil Enkripsi : (Encrypted result)", monoalphabetic_encrypt(text, key))
    elif choice == '2':
        text = input("Masukan Pesan : (Enter message) : ")
        keyword = input("Masukan Keyowrd : (Enter keyword) : ").lower()
        key = generate_key(keyword)
        print("Hasil Dekripsi : (Decrypted result)", monoalphabetic_decrypt(text, key))
    elif choice == '3':
        filename = input("Masukan nama file : (Enter filename) : ")
        if not os.path.exists(filename):
            print("File tidak ditemukan (File not found.)")
            continue
        keyword = input("Masukan Keyword : (Enter keyword) : ").lower()
        key = generate_key(keyword)
        encrypt_file(filename, key)
        print("File Berhasil di enkripsi (File encrypted successfully.)")
    elif choice == '4':
        filename = input("Masukan nama file : (Enter filename) : ")
        if not os.path.exists(filename):
            print("File tidak ditemukan (File not found.)")
            continue
        keyword = input("Masukan Keyword : (Enter keyword) : ").lower()
        key = generate_key(keyword)
        decrypt_file(filename, key)
        print("File berhasil di dekripsi (File decrypted successfully.)")
    elif choice == '0':
        break
    else:
        print("Pilihan tidak valid (Invalid choice.)")
