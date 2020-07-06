class CodigoCesarArchivos:

    def __init__(self):
        pass

    @staticmethod
    def cifradoDesifrado():
        respuesta = "s"
        while respuesta == "s":
            cifrar = ""
            descifrar = ""
            archivo = "archivo/data_file.csv"
            abrir = open(archivo, "r")
            leer = abrir.read()
            print(leer)
            pregunta = input("¿Desea cifrar o descifrar? ")
            if pregunta == "cifrar":
                abrir = open(archivo, "w")
                for scannear in leer:
                    alfabeto = ord(scannear)
                    cifrar += chr(alfabeto - 7)
                abrir.write(cifrar)
                print(cifrar)
                abrir.close()
            if pregunta == pregunta == "descifrar":
                abrir = open(archivo, "w")
                for scannear in leer:
                    alfabeto = ord(scannear)
                    descifrar += chr(alfabeto + 7)
                abrir.write(descifrar)
                abrir.close()
                print(descifrar)
            respuesta = input("Desea cifrar o desifrar otro archivo de texto? ")
            if respuesta == "n":
                break


objeto_cifrado = CodigoCesarArchivos()
objeto_cifrado.cifradoDesifrado()
