import hashlib

class HASH:
    def generarHash(h):
        digest=h.hexdigest()
        return digest

x=0

while x!=3:
    print("Elige la opción a usar:")
    print("1.SHA256")
    print("2.SHA512")
    print("3. Salir")
    opcion=int(input())

    if opcion == 3:
        break

    if opcion == 1 or opcion == 2:
        print("Introducir la información a la que se le hará Hash:")
        data=input()
        print()

        method = ""
        if opcion == 1:
            method = "sha256"
            print ("SHA256:")
        if opcion == 2:
            method = "sha512"
            print ("SHA512:")
    
        databytes = bytes(data,'utf-8')
        h = hashlib.new(method,databytes)
        result=HASH.generarHash(h)
        print(result)
        print()
        opcion = 0

print("saliendo...")
