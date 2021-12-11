import chess
tablero = chess.Board()
print(tablero)

while tablero.is_checkmate() == False:
    print(tablero.legal_moves)#Esto mostrará al usuario los posibles movimientos que puede hacer
    move = input("Introduce tu movimiento: ")
    tablero.push_san(move)
    print(tablero)
    tablero.is_checkmate()
    