import chess

fichas_negras = {
    chr(0x265f): "p",
    chr(0x265c): "r",
    chr(0x265e): "n",
    chr(0x256d): "b",
    chr(0x265b): "q",
    chr(0x265a): "k"  
}



tablero = chess.Board()
print(tablero)

while tablero.is_checkmate() == False:
    print(tablero.legal_moves)#Esto mostrará al usuario los posibles movimientos que puede hacer
    move = input("Introduce tu movimiento: ")
    tablero.push_san(move)
    print(tablero)
    tablero.is_checkmate()
    