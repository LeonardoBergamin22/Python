tabuleiro =  [
    ['','',''],
    ['','',''],
    ['','','']
]

# 

turno = 'X'

def verificarGanhador():
    # Verifica linhas e colunas para 'X' e 'O'
    for jogador in ['X', 'O']:
        # Verifica linhas
        for linha in tabuleiro:
            if [jogador, jogador, jogador] in linha:
                return True

        # Verifica colunas
        for i in range(0, 3):
            if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
                return True

        # Verifica diagonais
        if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
            return True

        if tabuleiro[2][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[0][2] == jogador:
            return True

    return False

    
    


def imprimirTabuleiro():
    for i in range(0,3):
        print("")
        for j in range(0,3):
            print("[", tabuleiro[i][j], "]", end='')
            
            

turno = input("Quem começa o jogo?")

while True:
    imprimirTabuleiro()
    linha = int(input("\nDigite uma posição para jogar:"))
    coluna = int(input("\nDigite uma posição para jogar:"))
    tabuleiro[linha][coluna] = turno
    
    if verificarGanhador():
        print(turno, " ganhou o jogo")
        break
    
    if turno == 'X':
        turno = 'O'
    elif turno == 'O':
        turno = 'X'