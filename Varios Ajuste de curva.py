# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:25:42 2022

@author: datomi
"""

#**************************Ajuste de Curva**************************

# código de ajuste de curva q testa todas as possibilidades

import numpy as np
import pylab as plt
import pandas as pd
import time

vx=[]
vy=[]

def pontuar(x,y):
    return(vx.append(x),vy.append(y))

'Instruções:'
'Escolha o tipo de ajuste que vc quer'
'e depois coloque os pontos e pronto'

ex = 0.01 #Exatidão do gráfico

#Qual ajuste?
#n=2 Linear
#n=3 Quadrático
#n>=4 Polinomial

n = 9

#Pontos (x,y)

pontuar(0,0)
pontuar(0.25,0.71)
pontuar(0.5,0.98182)
pontuar(0.75,1.164)
pontuar(1,1.31)
pontuar(1.5,1.46364)
pontuar(2,1.5091)
pontuar(2.5,1.4182)
pontuar(3,1.25455)
pontuar(3.5,1.14364)
pontuar(4,1.1)
pontuar(4.5,1.0655)
pontuar(5,1.0364)
pontuar(5.5,1.03273)
pontuar(6,1.0291)
pontuar(6.5,1.0255)
pontuar(7,1.0255)


# pontuar(100,0.786)
# pontuar(150,0.758)
# pontuar(200,0.737)
# pontuar(250,0.72)
# pontuar(300,0.707)
# pontuar(350,0.7)
# pontuar(400,0.69)
# pontuar(450,0.686)
# pontuar(500,0.684)
# pontuar(550,0.683)
# pontuar(600,0.685)
# pontuar(650,0.69)
# pontuar(700,0.695)
# pontuar(750,0.702)
# pontuar(800,0.709)
# pontuar(850,0.716)
# pontuar(900,0.72)
# pontuar(950,0.723)
# pontuar(1000,0.726)


# pontuar(1,11.083)
# pontuar(0.9,11.118)
# pontuar(0.8,11.234)
# pontuar(0.7,11.263)
# pontuar(0.6,11.287)
# pontuar(0.5,11.402)
# pontuar(0.4,11.411)



# df = pd.read_csv("plot-data.csv")

# vx = list(df["x"])
# vy = list(df[" y"])



'________________________________________________________________________________________________'

'Código em si, ALTERAR SOMENTE SE VC SOUBER O QUE ESTÁ FAZENDO'

com = time.time()

raix = 'x**(1/2)'
ra3x = 'x**(1/3)'
                  
sobx = 'x**(-1)'
sox2 = 'x**(-2)'
sox3 = 'x**(-3)'
sox4 = 'x**(-4)'

dosx = '2**x'
trex = '3**x'
xmx1 = 'x*(x-1)'

senx = 'np.sin(x)'
cosx = 'np.cos(x)'
tgx  = 'np.tan(x)'
atgx = 'np.arctan(x)*180/np.pi'

xsen = 'x*np.sin(x)'
xcos = 'x*np.cos(x)'

sehx = 'np.sinh(x)'
cohx = 'np.cosh(x)'
tghx = 'np.tanh(x)'

expx = 'np.exp(x)'
exmx = 'np.exp(-x)'
xemx = 'x*np.exp(-x)'
norm = 'np.exp(-(x**2))'

lnnx = 'np.log(x)'
logx = 'np.log10(x)'
pix  = 'np.pi**x'



p   = len(vx)
ini = min(vx)
fin = max(vx)
        
lista_decisao = [senx,
                  cosx,
                  tgx,
                  sehx,
                  cohx,
                  tghx,
                  expx,
                  exmx,
                  xemx,
                  raix,
                  ra3x,
                  lnnx,
                  logx,
                  sobx,
                  sox2,
                  sox3,
                  sox4,
                  dosx,
                  trex,
                  pix,
                  atgx,
                  norm,
                  xmx1,
                  xsen,
                  xcos]





lista_escolha1 = [0] * len(lista_decisao)


def check_de_valores(lista_escolha1,lista_decisao):
    
    if any(a > 600 for a in vx): #limitação do math.exp(x) que não pode ser maior que +ou- 700
                                 #limitação do math.pi**x que não pode ser maior que +ou- 600
    
        lista_decisao.remove(expx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(exmx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(xemx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(pix)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(sehx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(cohx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(tghx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(dosx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(trex)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(norm)
        lista_escolha1.remove(0)
    
    if min(vx) < 0: #se x < 0, raiz n funciona
        
        lista_decisao.remove(raix)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(ra3x)
        lista_escolha1.remove(0)
            
    if max(vx) > 1.5 : #se em grau > 90, não tem pq usar sen cos e tg
    
        lista_decisao.remove(senx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(cosx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(tgx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(xsen)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(xcos)
        lista_escolha1.remove(0)

    if any(a == 0 for a in vx): #se o valor de x é muito pequeno, 1/x pode dar valores muitos estranhos
        
        lista_decisao.remove(sobx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(sox2)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(sox3)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(sox4)
        lista_escolha1.remove(0)
                
    if any(a == 0 for a in vx) or min(vx) < 0: #verifica se algum valor é igual a 0 e se x < 0
    
        lista_decisao.remove(lnnx)
        lista_escolha1.remove(0)
        
        lista_decisao.remove(logx)
        lista_escolha1.remove(0)
        
    
    return(lista_escolha1,lista_decisao)

lista_escolha1,lista_decisao = check_de_valores(lista_escolha1,lista_decisao)

print('\nAjuste de curva usando o Método dos Mínimos Quadrados')

def cal_erro(lista1,gx,vx,vy):

    #erropor = []

    #ytra = np.mean(vy)
    ytra = sum(vy)/len(vy)
    
    SQresr = 0
    SQexpr = 0

    Erropor = 0
    
    for i in lista1:
        
        x = vx[i]
        
        y = eval(gx)
                
        #yr = vy[i]
                
        if vy[i] == 0:
            pr = 0
        else:
            pr = (abs(vy[i] - y))*100/(vy[i])

            if pr > Erropor:
                Erropor = pr
            
        #erropor.append(pr)
        
        SQresr += (vy[i] - y) ** 2
        
        SQexpr += (y - ytra) ** 2

    R2 = SQexpr/(SQexpr+SQresr)    

    #Erropor = max(erropor)
    
    return(Erropor,R2)



def ajuste(n:int,
           lista_escolha1:list,
           lista_decisao:list,
           vx:list,
           vy:list,
           p:int,
           lista_de_funcoes:list,
           lista_de_erros:list,
           lista_de_R2:list
           ):
    
    gz=[]
    gx = ""
    lista1=np.arange(0,p,1)

    A = np.zeros((n,n))
    B = np.zeros((1,n))[0]
    
    #criação do sistema de equações para econtrar o resultado do ajuste de curva
    for i in lista1:
        
        gs=[]
        x = vx[i]
        
        #enchendo a matriz de x**j
        for j in range(n):
           gs.append(x**j)
           
        #trocando os x**j por funções escolhidas
        for j in range(len(lista_decisao)):

            v_a_trc = lista_escolha1[j]
            
            if v_a_trc != 0:
                
                index_da_troca = lista_escolha1.index(v_a_trc)

                gs[v_a_trc] = eval(str(lista_decisao[index_da_troca]))
        
        #fazendo as outras partes da matriz
        for k in range(len(A)):

            for j in range(int(len(A))):

                A[j,k] = A[j,k]+(gs[j]*gs[k])
        
        #fazendo a outra matriz, de reusltados
        for j in range(len(A)):
      
            B[j] = B[j] + (vy[i]*gs[j])

    
    #resultado do sistema de quações
    X=np.linalg.inv(A).dot(B)
    
    #enchendo a equação com x**j primeiramente
    for j in range(n):

        gz.append("x"+"**"+str(j))
    
    #pegando as funções que foram usadas nessa equação e trocando pelos x**j
    for j in range(len(lista_decisao)):
        v_a_trc = lista_escolha1[j]
        if v_a_trc != 0:
            index_da_troca = lista_escolha1.index(v_a_trc)
            gz[v_a_trc] = lista_decisao[index_da_troca]


    #organizando a equação
    for j in range(n):
        
        if X.item(j) < 0:
            
            mais = " "
        
        else:
            
            mais = " + "
        
        if j == 0:
            
            gx = str(gx) +mais+ str(X.item(j))
            
        else:
            gx = str(gx) +mais+ (str(X.item(j))+"*"+str(gz[j]))
        
    # print('Função encontrada:',gx)
    gx=str(gx)
    
    #calculo do erro
    er,R2 = cal_erro(lista1,gx,vx,vy)

    lista_de_funcoes.append(gx)
    lista_de_erros.append(er)
    lista_de_R2.append(R2)


    #return(gx,er,R2)


    
#aqui começa a testar tudo

lista_de_erros = []
lista_de_R2 = []
lista_de_funcoes = []
    
ajuste(n,lista_escolha1,lista_decisao,vx,vy,p,lista_de_funcoes,lista_de_erros,lista_de_R2)


listas_escolhas = []

for i in np.arange(1,n,1):

    i = int(i)

    for m in range(len(lista_escolha1)):
        
        lista_escolha1[m] = i
          
        if lista_escolha1 not in listas_escolhas:

            listas_escolhas.append(list(lista_escolha1))
            
        
        for j in range(len(lista_escolha1)):
            
            if i+1 < n:
                lista_escolha1[j] = i+1
            if i+1 == n:
                lista_escolha1[j] = i-1

            
            if lista_escolha1 in listas_escolhas:
                lista_escolha1[j] = 0
                lista_escolha1[m] = 0
                continue
            

            if lista_escolha1 not in listas_escolhas:
                
                listas_escolhas.append(list(lista_escolha1))

            
            lista_escolha1[j] = 0
            
        lista_escolha1[m] = 0






for i in listas_escolhas:
        try:
            ajuste(n,i,lista_decisao,vx,vy,p,lista_de_funcoes,lista_de_erros,lista_de_R2)
        except:
            lista_de_funcoes.append(1)
            lista_de_erros.append(10000)
            lista_de_R2.append(0)
            pass

        porcen = "Carregando " + str(round(100*(len(lista_de_funcoes)/len(listas_escolhas)),2)) + " %"

        print(porcen,end = "")
        print("\b" * len(porcen), end = "",flush = True)


menor_erro_indx = lista_de_erros.index(min(lista_de_erros))
maior_R2_indx   = lista_de_R2.index(max(lista_de_R2))


a2 = set(lista_de_funcoes)
print(len(a2))

func_menor_erro = lista_de_funcoes[menor_erro_indx]
func_maior_R2   = lista_de_funcoes[maior_R2_indx]

print(len(lista_de_funcoes),'funções analisadas')
print('___________________________________________________________\n')

print('Aqui a função com menor erro em porcentagem:\n')
print('f(x) =',lista_de_funcoes[menor_erro_indx])
print('\nErro máximo: ',round(lista_de_erros[menor_erro_indx],2),'%')
print('R² =',round(lista_de_R2[menor_erro_indx],4))

print('___________________________________________________________\n')

print('Aqui a função com maior R2:\n')
print('f(x) =',lista_de_funcoes[maior_R2_indx])
print('\nErro máximo: ',round(lista_de_erros[maior_R2_indx],2),'%')
print('R² =',round(lista_de_R2[maior_R2_indx],4))

print('___________________________________________________________\n')

fim = time.time()

print('Tempo de processamento: %s segundos'%round(fim-com,1))
print('Foram analisadas: %s funções/segundos'%round(len(lista_de_funcoes)/(fim-com),1))

#listas_escolhas = list(set(listas_escolhas))

#for i in listas_escolhas:
#    print(i)


#Gráficos:

try:
    plt.style.use('extensys-gd')
except:
    pass

def grafico(Titulo,
            equacao,
            corp,
            core):
    
    vetor2=[]

    lista2g=np.arange(ini,fin + ex,ex)
    for x in lista2g:
        y=eval(equacao)
        vetor2.append(y)

    fig = plt.figure(num=None, figsize=(10.5, 7.5), dpi=200, facecolor='w', edgecolor='k')
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    plt.title(Titulo)
    plt.scatter(vx,vy,color= corp,s=50)
    plt.plot(lista2g,vetor2,color= core,label='Equação')
    plt.legend(bbox_to_anchor=(1.2,0.96), frameon=True, shadow=True, ncol=1)
    #plt.show()

    fig.savefig(f"{Titulo}.png")



grafico('Gráfico da Função com menor erro em %',
         func_menor_erro,
         'green',
         'blue')

grafico('Gráfico da Função com maior R2',
         func_maior_R2,
         'black',
         'red')

print('Fique atento ao gráfico, pode ter erro!!')


