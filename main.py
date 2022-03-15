
import array as arr

# array with int type
stato = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
nuovo_stato = arr.array('i', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#il nuovo stato verrà costruito a partire dal vecchio con le regole assegnate.
# Quando poi il nuovo stato è completo, allora lo "stato" diventerà quello che era prima il "nuovo_stato"

n = 21 #n è il numero di colonne della matrice che stamperò. Già che c'ero l'ho reso anche il numero di righe

for i in range(n):
    print(nuovo_stato[i], end=" ")

print()

for k in range (1, n): #k è l'indice della riga della matrice che sto stampando

    for i in range(1, n-1): #creo il nuovo stato applicando la regola del 30
        if ((stato[i-1] == 1) and (stato[i] == 1) and (stato[i+1] == 1)):
            nuovo_stato[i]=0
            #print('T1') #con i T posso controllare quale regola sia stata applicata
        if ((stato[i-1] == 1) and (stato[i] == 1) and (stato[i+1] == 0)):
            nuovo_stato[i]=0
            #print('T2')
        if ((stato[i-1] == 1) and (stato[i] == 0) and (stato[i+1] == 1)):
            nuovo_stato[i]=0
            #print('T3')
        if ((stato[i-1] == 1) and (stato[i] == 0) and (stato[i+1] == 0)):
            nuovo_stato[i]=1
            #print('T4')
        if ((stato[i-1] == 0) and (stato[i] == 1) and (stato[i+1] == 1)):
            nuovo_stato[i]=1
            #print('T5')
        if ((stato[i-1] == 0) and (stato[i] == 1) and (stato[i+1] == 0)):
            nuovo_stato[i]=1
            #print('T6')
        if ((stato[i-1] == 0) and (stato[i] == 0) and (stato[i+1] == 1)):
            nuovo_stato[i]=1
            #print('T7')
        if ((stato[i-1] == 0) and (stato[i] == 0) and (stato[i+1] == 0)):
            nuovo_stato[i]=0
            #print('T8')

    #print("Array nuovo stato : ", end=" ")
    for i in range(n):
        print(nuovo_stato[i], end=" ")
        stato[i] = nuovo_stato[i]

    print() # così vado a capo per iniziare la riga successiva