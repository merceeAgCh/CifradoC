"""
Prcatica 1 de materia Telelmatica
Profesor: Sergio Martinez Chavez
Lenguaje Python Version 3.8
"""


class Cifrado:  # Clase
    def __init__(self):
        pass  # esto se define unicamente cuando se utilizan clases en python

    @staticmethod  # se utiliza este para que el método funcione de forma correcta, lo hace estatico
    def cifrado():  # Definimos el objeto con nombre cifrado

        import random  # se importa la libreria a usar, para hacer la mezcla del abecedario

        n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # Arreglo de numeros
        le = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
              'y', 'z']
        le.extend(n)
        original = le
        f = open("abecedario.txt", "w")
        f.write(" ".join(original))
        f.close()
        """
        Agregamos ambas cadenas en la variable original y esta misma la enviamos al archivo que se crea
        de nombre abecedario.txt
        """
        random.shuffle(le)
        cif = le
        print("Abecedario para cifrar:")
        print(cif)
        """
        Se hace la mezcla (shuffle) de la cadena del abecedrio con numeros para usarlo en el 
        cifrado.
        Imprime en consola el resultado.
        """
        f = open("abecedarioC.txt", "w")
        f.write(" ".join(cif))
        f.close()
        """
        Se usa esta funcion para crear el archivo con el 
        abecedario para cifrar
        """

        # archivo=aco.modificar()
        print("Deseas cifrar: ")  # Preguntamos al usuario si desea hacer el cifrado
        respuesta = input()  # Asignamos a la variable respuesta la respuesta que da el usuario (s/n)
        if respuesta == "s":
            s = ""
            f = open('archivo/archivo.txt', 'r')
            abrir = f.read()
            f.close()
            # print(abrir)
            f = open("abecedario.txt", "r")
            normal = f.read()
            f.close()
            f = open("abecedarioC.txt", "r")
            clave = f.read()
            f.close()
            cifrado_tex = []
            #print(type(abrir))
            #print(len(abrir))

            for palabra in abrir:
                print(palabra)
                nueva = ""
                for letra in normal:
                    try:
                        #print(normal)
                    #print(abrir.index("a"))
                        indice = abrir.index(letra)
                    #print("M _ " + indice)
                        nueva = nueva + clave[indice]
                    except:
                        print("")
                cifrado_tex.append(nueva)
                print("Texto original")
                print(abrir)
                print("Texto cifrado")
                print(cifrado_tex)
                f = open("textoCifrado.txt", "w")
                f.write(" ".join(cifrado_tex))
                f.close()
        else:
            print("Gracias")
    def contadorl(con):  # funcion para realizar el conteo de letras
        from collections import Counter
        f = open('textoCifrado.txt', 'r')
        cuenta = f.read()
        f.close()
        con = Counter(cuenta)
        print(con)
        f = open("Contador.txt", "w")
        f.write("".join(con))
        f.close()

    """
    Se crea el archivo con el resultado del 
    contador y tambien lo imprime en consola
    """


objeto_cifrado = Cifrado()
objeto_cifrado.cifrado()
"""
Se manda a llamar la funcion de cifrado, si esto no 
se pone, el programa no hara lo referente a ello.
"""
