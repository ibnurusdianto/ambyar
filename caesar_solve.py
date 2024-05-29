import os
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
def encrypt_file(filename, shift):
    with open(filename, 'r') as f:
        text = f.read()
    encrypted = caesar_encrypt(text, shift)
    with open(filename + '.enc', 'w') as f:
        f.write(encrypted)
def decrypt_file(filename, shift):
    with open(filename, 'r') as f:
        text = f.read()
    decrypted = caesar_decrypt(text, shift)
    with open(filename[:-4], 'w') as f:  # Remove '.enc' extension
        f.write(decrypted)

while True:
    print("\n===== Caesar Tools =====")
    print("1. Enkripsi Pesan (Encrypt Message)")
    print("2. Dekripsi Pesan (Decrypt Message)")
    print("3. Enkripsi File (Encrypt File)")
    print("4. Dekripsi File (Decrypt File)")
    print("0. Keluar (quit?)")

    choice = input("Pilihan Anda: (Your choice : ) ")

    if choice == '1':
        text = input("Masukkan pesan: (Enter message : )")
        shift = int(input("Masukkan pergeseran: (Enter shift : ) "))
        print("Hasil enkripsi:", caesar_encrypt(text, shift))
    elif choice == '2':
        text = input("Masukkan pesan: (Enter message : ) ")
        shift = int(input("Masukkan pergeseran: (Enter shift : ) "))
        print("Hasil dekripsi:", caesar_decrypt(text, shift))
    elif choice == '3':
        filename = input("Masukkan nama file: (Enter filename : ) ")
        if not os.path.exists(filename):
            print("File tidak ditemukan. (File not found.)")
            continue
        shift = int(input("Masukkan pergeseran: (Enter shift : )"))
        encrypt_file(filename, shift)
        print("File berhasil dienkripsi. (File encrypted successfully.)")
    elif choice == '4':
        filename = input("Masukkan nama file: (Enter filename : ) ")
        if not os.path.exists(filename):
            print("File tidak ditemukan. (File not found.)")
            continue
        shift = int(input("Masukkan pergeseran: (Enter shift: ) "))
        decrypt_file(filename, shift)
        print("File berhasil didekripsi. (File decrypted successfully.)")
    elif choice == '0':
        break
    else:
        print("Pilihan tidak valid. (Invalid choice.)")
