#Questa è semplicemente la trascrizione del programma del blog a cui si era ispirato Giampieri per la lezione



def window(iterable, width=3):
    for index in range(len(iterable)-width+1):
        yield(iterable[index:index+width])

# window is a function that split a string in smaller string of lenght = 'width', 
# each containing successive elements of the original string. 
# In this case each element of the rule depends on the element itself, the previous one and
# the following one, so we set width=3

rule={"111": '0', "110": '0', "101": '0', "000": '0', 
"100": '1', "011": '1', "010": '1', "001": '1'}

#rule 30, as defined by wolfram

def rule_30():
    initial_state='0000001000000'  #stato iniziale, da implementare meglio
    state = initial_state #all'inizio lo stato è quello iniziale
    for i in range(len(initial_state)):
        pattern= window(state) #non posso fare direttamente window(initial_state), ma 
                              #devo assegnare man mano a un'altra variabile il valore di window(state) perchè se no userei 
                              #sempre la prima stringa
        state=''.join(rule[pat] for pat in pattern)
        #assegno allo stato il valore di join. join dà il valore della stringa (in questo caso vuota) su cui viene chiamato,
        #e aggiunge le stringhe inserite come argomento. in questo caso le stringhe sono il contenuto del dic 'rule' le cui 
        # chiavi sono date dai valori di pattern, e cioè dalle stringhe di tre caratteri precedentemente fornite da window
        
        state='0{}0'.format(state)
        #aggiungo degli 0 prima e dopo il nuovo state per evitare che la stringa diminuisca il numero di elementi e il 
        # programma venga eventualmente bloccato. format inserisce il suo argomento al posto delle graffe 
        print(state)
        

rule_30()

#{}