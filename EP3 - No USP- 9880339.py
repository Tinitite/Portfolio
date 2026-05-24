#################################################
# MAC 115 - Introduçâo à Computação
#
# IF-USP - Segundo Semestre de 2017
#
# <turma: 21> - <nome do professor: Marco Dimas Gubitoso>
#
# <nome do(a) aluno(a): Rafael Albertini Silva>
# <número USP:9880339>
#################################################

from pylab import *
from scipy import *
import scipy.spatial.distance as ssd

from tkinter import *
import sys

#Janela princial
tk =  Tk()

#Divisoẽs da janela principal
f1 = Frame(tk)
f1.pack(side = TOP,expand=True, fill='x')
f2 = Frame(tk)
f2.pack(side = TOP,expand=True, fill='x')
f3 = Frame(tk)
f3.pack(side = TOP,expand=True, fill='x')
f4 = Frame(tk)
f4.pack(side = TOP,expand=True, fill='x')
f5 = Frame(tk)
f5.pack(side = TOP,expand=True, fill='x')
f6 = Frame(tk)
f6.pack(side = TOP,expand=True, fill='x')

#Variaveis para entrada de dados
q1 = DoubleVar() #Carga_1
q2 = DoubleVar() #Carga_2
q3 = DoubleVar() #Carga_3
q4 = DoubleVar() #Carga_4
q5 = DoubleVar() #Carga_5
h1 = DoubleVar() #altura_1
h2 = DoubleVar() #altura_2
h3 = DoubleVar() #altura_3
h4 = DoubleVar() #altura_4
h5 = DoubleVar() #altura_5
Vx = DoubleVar() #velocidade em x
T  = IntVar()    # tempo de simulação
dt = IntVar()    # intervalo de interpolação

# Base de entrada de dados
q1.set(1)
q2.set(1)
q3.set(1)
q4.set(1)
q5.set(1)
h1.set(1)
h2.set(1)
h3.set(1)
h4.set(1)
h5.set(1)
Vx.set(10)
T.set(1)
dt.set(1)

#Indentificações e entrada de dados
l1 =  Label(f1, text = "Carga_1").pack(side = LEFT)
e1 = Entry(f1, bd = 2, textvariable = q1).pack(side = LEFT)
l1_1 =  Label(f1, text = "C").pack(side = LEFT)

l2 =  Label(f2, text = "Carga_2").pack(side = LEFT)
e2 = Entry(f2, bd = 2, textvariable = q2).pack(side = LEFT)
l2_1 =  Label(f2, text = "C").pack(side = LEFT)

l3 =  Label(f3, text = "Carga_3").pack(side = LEFT)
e3 = Entry(f3, bd = 2, textvariable = q3).pack(side = LEFT)
l3_1 =  Label(f3, text = "C").pack(side = LEFT)

l4 =  Label(f4, text = "Carga_4").pack(side = LEFT)
e4 = Entry(f4, bd = 2, textvariable = q4).pack(side = LEFT)
l4_1 =  Label(f4, text = "C").pack(side = LEFT)

l5 =  Label(f5, text = "Carga_5").pack(side = LEFT)
e5 = Entry(f5, bd = 2, textvariable = q5).pack(side = LEFT)
l5_1 =  Label(f5, text = "C").pack(side = LEFT)

l6 =  Label(f1, text = "  Altura_1").pack(side = LEFT)
e6 = Entry(f1, bd = 2, textvariable = h1).pack(side = LEFT)
l6_1 =  Label(f1, text = "cm").pack(side = LEFT)

l7 =  Label(f2, text = "  Altura_2").pack(side = LEFT)
e7 = Entry(f2, bd = 2, textvariable = h2).pack(side = LEFT)
l7_1 =  Label(f2, text = "cm").pack(side = LEFT)

l8 =  Label(f3, text = "  Altura_3").pack(side = LEFT)
e8 = Entry(f3, bd = 2, textvariable = h3).pack(side = LEFT)
l8_1 =  Label(f3, text = "cm").pack(side = LEFT)

l9 =  Label(f4, text = "  Altura_4").pack(side = LEFT)
e9 = Entry(f4, bd = 2, textvariable = h4).pack(side = LEFT)
l9_1 =  Label(f4, text = "cm").pack(side = LEFT)

l10 =  Label(f5, text = "  Altura_5").pack(side = LEFT)
e10 = Entry(f5, bd = 2, textvariable = h5).pack(side = LEFT)
l10_1 =  Label(f5, text = "cm").pack(side = LEFT)


l11 =  Label(f1, text = "  Vx").pack(side = LEFT)
e11 = Entry(f1, bd = 2, textvariable = Vx).pack(side = LEFT)
l11_1 =  Label(f1, text = "cm/s").pack(side = LEFT)


l12 =  Label(f2, text = "   T").pack(side = LEFT)
e12 = Entry(f2, bd = 2, textvariable = T).pack(side = LEFT)
l12_1 =  Label(f2, text = "s").pack(side = LEFT)

l13 =  Label(f3, text = "  dt").pack(side = LEFT)
e13 = Entry(f3, bd = 2, textvariable = dt).pack(side = LEFT)
l13_1 =  Label(f3, text = "s").pack(side = LEFT)

#Botão de fechar a janela
b2 = Button(f6, text = "Fechar", command = lambda :sys.exit()).pack(side = RIGHT)



def Forca(q1,q2, q3, q4, q5, h1, h2, h3, h4, h5,k):
    """
    Função que calcula a força resultande em uma particula

    :param q1: Carga_1
    :param q2: Carga_2
    :param q3: Carga_3
    :param q4: Carga_4
    :param q5: Carga_5
    :param h1: Altura_1
    :param h2: Altura_2
    :param h3: Altura_3
    :param h4: Altura_4
    :param h5: Altura_5
    :param k: Constante elétrostática(Genérica)
    :return: F = lista com as forças elétricas de intereção de uma partícula com as demais partículas
    """
    d = np.array([[h1],[h2]])
    dist1 = ssd.pdist(d)
    d = np.array([[h1], [h3]])
    dist2 = ssd.pdist(d)
    d = np.array([[h1], [h4]])
    dist3 = ssd.pdist(d)
    d = np.array([[h1], [h5]])
    dist4 = ssd.pdist(d)
    F = np.array([(k*q1*q2)/dist1, (k*q1*q3)/dist2, (k*q1*q4)/dist3 ,(k*q1*q5)/dist4])
    return F

def Ay(F,k):
    """
    Calcula a aceleração de uma particula com as demais em função das forças elétricas
    :param F: lista com as forças elétricas de intereção de uma partícula com as demais partículas
    :param k: Constante elétrostática(Genérica)
    :return: F/k = Lista com as acelerações de interação entre uma partícula com as demias
    """
    return (F/k)

def traj_Y(ay,T, dt, h,P,linha):
    """
    Função que monta uma matriz com as coordenas em y da partícula a cada instante de tempo
    :param ay: aceleração resultante da partícula
    :param T: Tempo de simulação
    :param dt: intervalo de interpolação
    :param h: altura inicial da partícula
    :param P: Matriz de posições das partículas em cada instante de tempo
    :param linha: Linha da matriz P que esta as posições da partícula
    :return: Matriz P com a linha, correspondente a partícula, preenchida
    """
    t = np.linspace(0,T+1,T//dt, endpoint=True)#cria uma lista com os intantes de tempos
                                                #entre 0 e T/dt
    vy = 0 #velocidade inicial em y da partícula
    Y = h #posição inicial da partícula em y
    vy =  vy + ay*t #cria uma lista com as velocidades em y, das partículas, atualizadas
    Y += (1/2)*ay*t**2 + vy*t #cria uma lista com as posições em y, das partícuals, atualizadas
    for j in range(0,T//dt):
        P[linha][j] = Y[j] # copia as posições para matriz de poição, na linha correspondente
                            # à partícula

    return P

def traj_X(Vx,T,dt):
    """
    Função cria uma lista com as posições em x atualizadas em cada instante de tempo
    :param Vx: velocidade em x
    :param T: tempo de simulação
    :param dt: intervalo de interpolação
    :return: A lista X com as posições
    """
    t = np.linspace(0, T + 1, T // dt, endpoint=True)#cria uma lista com os intantes de tempos
                                                #entre 0 e T/dt
    X = Vx*t # lista com as posições atualizadas da patírcula
    return X

#Lista de cores
cor = ("black","orange","yellow","violet","blue","green","red")
#contador pra indicar qual cor da lista será usada pra plotar o gráfico
indica = 0

def desenha (q1,q2,q3,q4,q5,h1,h2,h3,h4,h5,Vx,T,dt):
    """
    Função que recebe os dados e os resultados das interações de cada partícuala
    e plota o gráfico com a curva de cada partícula
    :param q1: Carga_1
    :param q2: Carga_2
    :param q3: Carga_3
    :param q4: Carga_4
    :param q5: Carga_5
    :param h1: altura_1
    :param h2: altura_2
    :param h3: altura_3
    :param h4: altura_4
    :param h5: altura_5
    :param Vx: Velocidade em x
    :param T: Tempo de simulação
    :param dt: Intervalo de interpolação
    """

    global indica

    k = 2 #Constante eletrostática genérica
    Q = np.array([q1,q2,q3,q4,q5])#Lista com as cargas elétrica de cada partícula
    H = np.array([h1,h2,h3,h4,h5])#Lista com as alturas iniciais de cada partícula
    n = T//dt#Divisão interia do tempo de simulação pelo intervalo de interpolação
    P = np.zeros((5,int(n)))#Criando a matriz de posição de cada partícula em cada instante de tempo
    for i in range (H.size):
        P[i][0] = H[i] # Copia as posições iniciais de cada partícula

    #Calcula das forças e acelerações de cada partícula
    F1 = Forca(Q[0], Q[1], Q[2], Q[3], Q[4], H[0], H[1], H[2], H[3], H[4], k)
    a1 = Ay(F1,k)
    F2 = Forca(Q[1], Q[0], Q[2], Q[3], Q[4], H[1], H[0], H[2], H[3], H[4], k)
    a2 = Ay(F2, k)
    F3 = Forca(Q[2], Q[1], Q[0], Q[3], Q[4], H[2], H[1], H[0], H[3], H[4], k)
    a3 = Ay(F3, k)
    F4 = Forca(Q[3], Q[1], Q[2], Q[0], Q[4], H[3], H[1], H[2], H[0], H[4], k)
    a4 = Ay(F4, k)
    F5 = Forca(Q[4], Q[1], Q[2], Q[3], Q[0], H[4], H[1], H[2], H[3], H[0], k)
    a5 = Ay(F5, k)

    F = np.array([F1,F2,F3,F4,F5])#Matriz com as forças sobre as partículas
    A = np.array([a1,a2,a3,a4,a5])#matriz com as acelerações sobre as partículas

    for j in range(5):
        P = traj_Y(A[j].sum(), T, dt, H[j],P,j)#Copia as posições em y em cada instante de tempo
                                                # em cada partícula

    X = traj_X(Vx, T, dt)#Copia as posições em x em cada instante de tempo em cada partícula

    #Plota a curva de cada partícula no mesmo gráfico
    plot(X, P[0], color=cor[indica], linewidth=1.0, linestyle="-")
    indica += 1
    indica %= len(cor)

    plot(X, P[1], color=cor[indica], linewidth=1.0, linestyle="-")
    indica += 1
    indica %= len(cor)

    plot(X, P[2], color=cor[indica], linewidth=1.0, linestyle="-")
    indica += 1
    indica %= len(cor)

    plot(X, P[3], color=cor[indica], linewidth=1.0, linestyle="-")
    indica += 1
    indica %= len(cor)

    plot(X, P[4], color=cor[indica], linewidth=1.0, linestyle="-")
    indica += 1
    indica %= len(cor)

    show() # mostra o gráfico

#Botão que plota o gráfico
b1 = Button(f6, text = "Desenhar", command = lambda : desenha(q1.get(),q2.get(),q3.get(),q4.get(),
                                                              q5.get(),h1.get(),h2.get(),h3.get(),
                                                              h4.get(),h5.get(),Vx.get(),T.get(),
                                                              dt.get())).pack(side = LEFT)
mainloop()#chama a janela principal