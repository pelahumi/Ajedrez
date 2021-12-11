import chess

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
    print("Los movimientos posibles son: ", tablero.legal_moves)#Esto mostrará al usuario los posibles movimientos que puede hacer
    move = input("Introduce tu movimiento: ")

    tablero.push_san(move)
    print(tablero)
    tablero.is_checkmate()
    
    if tablero.is_checkmate() == True:
        print("Jaque mate")