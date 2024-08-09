from tkinter import *
from tkinter import messagebox
from random import choice
import os

# Função PATH - Obtém o diretório do arquivo Python atual.
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# A variável "endereco_arquivo" irá armazenar o caminho e o nome do arquivo que será usado ou criado.
endereco_arquivo = diretorio_atual+"\\pontuacao.txt"

#listas dos botões
botoes = {}
cobertura = {}

#variáveis iniciais
pontos = 0
perdeu= False

#Função sorteia 
def bombas():
    linha1 = [botoes["botao1"],botoes["botao2"],botoes["botao3"],botoes["botao4"]]
    linha2 = [botoes["botao5"],botoes["botao6"],botoes["botao7"],botoes["botao8"]]
    linha3 = [botoes["botao9"],botoes["botao10"],botoes["botao11"],botoes["botao12"]]
    linha4 = [botoes["botao13"],botoes["botao14"],botoes["botao15"],botoes["botao16"]]
    linha5 = [botoes["botao17"],botoes["botao18"],botoes["botao19"],botoes["botao20"]]
    linhas = [linha1,linha2,linha3,linha4,linha5]

    for linha in linhas:
        bomba = choice(linha)
        bomba["text"] = "💣"
        

            

# Função chamada quando um botão é clicado
def clique(chave):
    global perdeu, pontos
    botoes[chave].lift() #coloca o botão na frente da cobertura
    if botoes[chave]["text"] == "💎":
        pontos+=1
        gameOver()
    elif botoes[chave]['text'] == '💣':
        perdeu = True
        gameOver()

#Função que exibe a mensagem de fim de jogo
def gameOver():
    global perdeu
    if perdeu == True:
        messagebox.showinfo(title="Fim de Jogo", message=f"Bomba!!! Você perdeu!\nSua pontuação foi: {pontos}.")
        reset()
    elif (perdeu==False) and (pontos == 15):
        messagebox.showinfo(title="Fim de Jogo", message=f"Parabéns, você venceu!\nSua pontuação foi: {pontos}.")
        reset()


#Função que reseta as condições do jogo e salva a pontuação do usuário
def reset():
    global perdeu, pontos, endereco_arquivo
    if os.path.exists(endereco_arquivo): #Verifica se o arquivo txt existe
        with open(endereco_arquivo, "r") as arquivo:
            lista = arquivo.readlines()
            if lista: #Verifica se há algo escrito no arquivo
                try:
                    pontos_salvos = int(lista[0].strip())
                    if pontos > pontos_salvos: #Sobrescreve a pontuação salva se a nova pontuação for maior que a anterior
                        with open(endereco_arquivo, "w") as arquivo:
                                arquivo.truncate(0)
                                arquivo.write(f"{pontos}") 
                        maior_pontuacao['text'] = pontos
                except:
                    with open(endereco_arquivo, "w") as arquivo:
                        arquivo.write("0")
                        
            else:
                with open(endereco_arquivo, "w") as arquivo: #Escreve 0 se o arquivo estiver vazio
                    arquivo.write("0")            
    else:
        with open(endereco_arquivo, "w") as arquivo: #Cria um arquivo e escreve nele "0"
            arquivo.write("0")
    for button in botoes:
        cobertura[button].lift() #Coloca a cobertura por cima do botão
        botoes[button]["text"] = '💎'
    pontos = 0
    perdeu = False
    bombas()

#Criando uma janela
janela = Tk()
janela.title("Jogo da Velha")
janela.geometry("410x600+500+100")
janela.configure(background="#a4a4a4")
janela.resizable(False, False)

#Titulo
titulo = Label(janela, text="💎MINES💣", font="Arial 24",foreground="black",background="#c4c4c4" )
titulo.place(x=135, y=10)

#Criando os botoes - Linha 1
botoes["botao1"] = Button(janela,text="💎",font="Arial 20", width=5, height=2,bg='#ccc')
botoes["botao1"].place(x=10, y=60)
botoes["botao2"]= Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao2"].place(x=105, y=60)
botoes["botao3"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao3"].place(x=200, y=60)
botoes["botao4"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao4"].place(x=295, y=60)

#Criando as coberturas - Linha 1
cobertura["botao1"] = Button(janela,text="",font="Arial 20", width=5, height=2,bg='#ccc', command=lambda botao = "botao1":clique(botao))
cobertura["botao1"].place(x=10, y=60)
cobertura["botao2"]= Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao2":clique(botao))
cobertura["botao2"].place(x=105, y=60)
cobertura["botao3"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao3":clique(botao))
cobertura["botao3"].place(x=200, y=60)
cobertura["botao4"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao4":clique(botao))
cobertura["botao4"].place(x=295, y=60)

#Criando os botoes - Linha 2
botoes["botao5"] = Button(janela,text="💎",font="Arial 20", width=5, height=2,bg='#ccc')
botoes["botao5"].place(x=10, y=155)
botoes["botao6"]= Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao6"].place(x=105, y=155)
botoes["botao7"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao7"].place(x=200, y=155)
botoes["botao8"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao8"].place(x=295, y=155)

#Criando as coberturas - Linha 2
cobertura["botao5"] = Button(janela,text="",font="Arial 20", width=5, height=2,bg='#ccc', command=lambda botao = "botao5":clique(botao))
cobertura["botao5"].place(x=10, y=155)
cobertura["botao6"]= Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao6":clique(botao))
cobertura["botao6"].place(x=105, y=155)
cobertura["botao7"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao7":clique(botao))
cobertura["botao7"].place(x=200, y=155)
cobertura["botao8"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao8":clique(botao))
cobertura["botao8"].place(x=295, y=155)

#Criando os botoes - Linha 3
botoes["botao9"] = Button(janela,text="💎",font="Arial 20", width=5, height=2,bg='#ccc')
botoes["botao9"].place(x=10, y=250)
botoes["botao10"]= Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao10"].place(x=105, y=250)
botoes["botao11"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao11"].place(x=200, y=250)
botoes["botao12"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao12"].place(x=295, y=250)

#Criando as coberturas - Linha 3
cobertura["botao9"] = Button(janela,text="",font="Arial 20", width=5, height=2,bg='#ccc', command=lambda botao = "botao9":clique(botao))
cobertura["botao9"].place(x=10, y=250)
cobertura["botao10"]= Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao10":clique(botao))
cobertura["botao10"].place(x=105, y=250)
cobertura["botao11"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao11":clique(botao))
cobertura["botao11"].place(x=200, y=250)
cobertura["botao12"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao12":clique(botao))
cobertura["botao12"].place(x=295, y=250)

#Criando os botoes - Linha 4
botoes["botao13"] = Button(janela,text="💎",font="Arial 20", width=5, height=2,bg='#ccc')
botoes["botao13"].place(x=10, y=345)
botoes["botao14"]= Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao14"].place(x=105, y=345)
botoes["botao15"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao15"].place(x=200, y=345)
botoes["botao16"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao16"].place(x=295, y=345)

#Criando as coberturas - Linha 4
cobertura["botao13"] = Button(janela,text="",font="Arial 20", width=5, height=2,bg='#ccc', command=lambda botao = "botao13":clique(botao))
cobertura["botao13"].place(x=10, y=345)
cobertura["botao14"]= Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao14":clique(botao))
cobertura["botao14"].place(x=105, y=345)
cobertura["botao15"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao15":clique(botao))
cobertura["botao15"].place(x=200, y=345)
cobertura["botao16"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao16":clique(botao))
cobertura["botao16"].place(x=295, y=345)

#Criando os botoes - Linha 5
botoes["botao17"] = Button(janela,text="💎",font="Arial 20", width=5, height=2,bg='#ccc')
botoes["botao17"].place(x=10, y=440)
botoes["botao18"]= Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao18"].place(x=105, y=440)
botoes["botao19"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao19"].place(x=200, y=440)
botoes["botao20"] = Button(janela,text="💎",font="Arial 20", width=5, height=2, bg='#ccc')
botoes["botao20"].place(x=295, y=440)

#Criando as coberturas - Linha 5
cobertura["botao17"] = Button(janela,text="",font="Arial 20", width=5, height=2,bg='#ccc', command=lambda botao = "botao17":clique(botao))
cobertura["botao17"].place(x=10, y=440)
cobertura["botao18"]= Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao18":clique(botao))
cobertura["botao18"].place(x=105, y=440)
cobertura["botao19"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao19":clique(botao))
cobertura["botao19"].place(x=200, y=440)
cobertura["botao20"] = Button(janela,text="",font="Arial 20", width=5, height=2, bg='#ccc', command=lambda botao = "botao20":clique(botao))
cobertura["botao20"].place(x=295, y=440)

#Texto pontuação
placar = Label(janela, text="Maior pontuação: ", font="Arial 16",foreground="black",background="#a4a4a4" )
placar.place(x=10, y=545)

reset()
with open(endereco_arquivo, "r") as arquivo:
    pontuacao = arquivo.read()
maior_pontuacao = Label(janela, text=pontuacao, font="Arial 16",foreground="black",background="#a4a4a4" )
maior_pontuacao.place(x=180,y=545)



janela.mainloop()