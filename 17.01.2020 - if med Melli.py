# Lager meny


def if_test():  #Oppgavesett 1 (oppgave 3)

    print('Poeng mellom 92-100 = A')
    print('Poeng mellom 77-91 = B')
    print('Poeng mellom 58-76 = C')
    print('Poeng mellom 46-57 = D')
    print('Poeng mellom 0-39 = F')
    
    sok=int(input('Søk på studentens karakterpoeng: ')) # MÅ ha int for å søke i if/elif
    if sok>=0 and sok <=39:
        print('Karakteren er F')
        
    elif sok>=40 and sok <=45:
        print('Karakteren er E')
        
    elif sok>=46 and sok<=57:
        print('Karakteren er D')
        
    elif sok>=58 and sok<=76:
        print('Karakteren = C')
        
    elif sok>=77 and sok<=91:
        print('Karakteren = B')
        
    elif sok>=92 and sok<=100:
        print('Karakteren = A')
    else:
        print('Karaktersummen eksisterer ikke. Prøv igjen')





    

def storste_tall():
    
    
    liste=[] # Tom liste 
    tall_nr=1 # tall nr
    antall=int(input('Oppgi antall tall i liste: '))
    for t in range(antall): #t=variabel
        print('tall nr', tall_nr)
        tall_nr+=1
        tall=int(input('Oppgi tall: '))
        liste+=[tall] # Glemmer ikke tall som er oppgitt

    print('Listen er: ',liste)

    



    
    plass=0
    storste=liste[0] # antar at plass null er den størrste 
    for e in range (1,len(liste)):#starter på 1, fordi vi antar at plass 0 er størrst og skal kun sjekkes en gang, med nabo tallet-e "byttes ut" for hver runde med plass i range
        if liste[e] >= storste: 
            storste=liste[e]
            plass=e
            
    print ('Det største tallet er:',storste)
    print('Utgjør plass nr:',plass+1) # Sparer på e må +1 fordi den teller fra 0




    

    '''if liste[1] <= storste: #2 tall
        storste=liste[1]
        
    if liste[2] >= storste:
        storste=liste[2]

    if liste[3] >= storste:
        storste=liste[3]

    if liste[4] >= storste:
        storste=liste[4]'''

        




    
    

def c():
    print('c')
    
def meny():
    ny=True

    while ny==True:
        print('Menyvalg')
        print('Meny 1= Søk på karakterpoeng ')
        print('Meny 2= Finner største tall ')
        print('Meny 3=c ')
        print('Meny 4= Avslutt')
        valg=input('Gjør et valg fra menyen: ')

        if valg=='1':
            loop='Ja'
            while loop=='Ja' or loop=='ja':
                if_test()
                loop=input('Kjøre igjen? Ja/ja: ')

        elif valg=='2':
            loop='Ja'
            while loop=='Ja' or loop=='ja':
                storste_tall()
                loop=input('Kjøre igjen? Ja/ja: ')
          

        elif valg=='3':
            loop='Ja'
            while loop=='Ja' or loop=='ja':
                c()
                loop=input('Kjøre igjen? Ja/ja: ')
            

        else:
            print('Programmet avsluttes')
            ny=False

meny()

        
        
        
    
