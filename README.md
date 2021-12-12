# Ajedrez
Esta tarea consistió en realizar un programa con el que se pueda jugar una partida de ajedrez.
Mi dirección de este repositorio es la siguiente: [GitHub](https://github.com/pelahumi/Ajedrez)
https://github.com/pelahumi/Ajedrez

El diagrama de flujo correspondiente a este código es el siguiente:

![Diagrama de flujo](https://github.com/pelahumi/Ajedrez/blob/main/Captura%20de%20pantalla%202021-12-12%20a%20las%2019.37.14.png)

El código de la tarea es el siguiente:

'''import chess

fichas_negras = {
    chr(0x265f): "p",
    chr(0x265c): "r",
    chr(0x265e): "n",
    chr(0x256d): "b",
    chr(0x265b): "q",
    chr(0x265a): "k"  
}

fichas_blancas = {
    chr(0x2659): "P",
    chr(0x2658): "R",
    chr(0x2657): "N",
    chr(0x2566): "B",
    chr(0x2655): "Q",
    chr(0x2654): "K" 
}

fichas = {**fichas_negras, **fichas_blancas}


for ficha, valor in fichas.items():
    print("Las fichas {} en el tablero son {}".format(ficha,valor))

tablero = chess.Board()
print(tablero)

while tablero.is_checkmate() == False:
    respuesta = input("¿Quieres realizar un movimiento?: ")

    if respuesta == "Si" or respuesta == "Sí":
        print("Los movimientos posibles son: ", tablero.legal_moves)#Esto mostrará al usuario los posibles movimientos que puede hacer
        move = input("Introduce tu movimiento: ")
        tablero.push_san(move)
    
        print(tablero)#Tablero después del movimiento
        tablero.is_checkmate()#Comprueba si hay jaque mate y devuelve un valor boleano
    
    else:
        print("Se ha acabado la partida")
        break
    
    if tablero.is_checkmate() == True:
        print("Jaque mate")
