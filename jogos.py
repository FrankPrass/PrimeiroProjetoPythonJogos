import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo*******!")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo? \n"))

    if(jogo == 1):
        print("Jogo da Forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo da Adivinhação")
        adivinhacao.jogar()
    else:
        print("Escolha uma opção válida.")
        escolhe_jogo()

if(__name__ == "__main__"):
    escolhe_jogo()
