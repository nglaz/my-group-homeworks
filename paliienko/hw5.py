def encrypt():
    while True:
        try:
           key = int(input("pls input key from 1 to 25"))
        except ValueError:
           print("try number pls")
        else:
            break
    while True:
        file = input("input your file")
        try:
            with open(file, "r", encoding="utf-8") as crypto:
               crypto.seek(0)
               crp = crypto.read()
               encrypted = ''.join(chr(ord(ceaser) + key) for ceaser in crp)
        except FileNotFoundError:
            print("There is no such file in directory")
        else:
            break
    with open(file, "r", encoding="utf-8") as crypto:
        crypto.seek(0)
        crp=crypto.read()
        encrypted = ''.join(chr(ord(ceaser) + key) for ceaser in crp)
    fileen = input("input name encp file")
    with open (fileen, "w+", encoding="utf-8") as crypted:
        crypted.write(encrypted)
    print("encrypted result in encp file")


def decrypt():
    while True:
        try:
            key = int(input("pls input key from 1 to 25"))
        except ValueError:
            print("try number pls")
        else:
            break
    while True:
        filede = input("input your file")
        try:
            with open(filede, "r", encoding="utf-8") as decrypto:
                decrypto.seek(0)
                decrp = decrypto.read()
                deencrypted = ''.join(chr(ord(ceaser) - key) for ceaser in decrp)
        except FileNotFoundError:
            print("There is no such file in directory")
        else:
            break
    with open(filede, "r", encoding="utf-8") as decrypto:
        decrypto.seek(0)
        decrp=decrypto.read()
        deencrypted = ''.join(chr(ord(ceaser) - key) for ceaser in decrp)
    filedecr = input("input name decp file")
    with open (filedecr, "w+", encoding="utf-8") as decrypted:
        decrypted.write(deencrypted)
    print("decryption result in inputed decp file")


main = input("encrypt or decrypt? e = encrypt, d = decrypt")
if main == "e":
    encrypt()
elif main == "d":
    decrypt()