#Program for oversikt over foring av fisk i merder.
antallForinger = 2
kgForLager = 50000
maksKgLager = 70000
prosentGrense = 20
antallMerder = 6
# Listen merder inneholder antall fisk i merden og hvor mye for det er beregnet per fisk per foring
merder = [[200000,0.2],[160000,0.3],[160000,0.3],[130000,0.4],[130000,0.4],[130000,0.4]]


def Registreringavforing():
    print(f'Registrering av foring')
    print(f'Hvilken merde er foret 1-{antallMerder}?')
    m = input()
    m = int(m)
    forBrukt = merder[m-1][0]*merder[m-1][1]
    print(kgForLager)
    kgForLager = kgForLager - forBrukt
    if kgForLager <= maksKgLager*prosentGrense:
        print('Lageret for fiskefôr er snart tomt. Du må bestille mer')

def justerantallforinger():
    print(f'Justering av antall foringer per dag. Antall foringer resigtrert i dag er {antallForinger}.')
    print(f'Nytt antall: ')
    antallForinger = input()
    print(antallForinger)

def justerantallmerder():
    print(f'Justering av antall merder i anlegget. Antall merder resigtrert i dag er {antallMerder}.')
    print(f'Nytt antall: ')
    antallMerder = input()

def Registrerfisk():
    print(f'Justering av antall merder i anlegget. Antall merder resigtrert i dag er {antallMerder}.')
    print(f'Nytt antall: ')
    antallMerder = input()


    
while True:
    print(f'1: Registrer en foring')
    print(f'2: Registrer antall foringer per dag')
    print(f'3: Registrere antall merder')
    print(f'4: Registrering av fisk')

    print(f'8: Justering av forlager')
    print(f'9: List ut informasjon')
    print(f'0: Avslutt')
    print(f'Valg: ')
    valg = input()
    if valg == '1':
        Registreringavforing()

    if valg == '2':
        justerantallforinger()

    if valg == '3':
        justerantallmerder()

    if valg == '4':
        Registrerfisk()
        
    if valg == '8':
        print(f'Justering av for på lager. Antall for resigtrert i dag er {kgForLager} Kg.')
        print(f'Nytt antall: ')
        kgForLager = input()
        print("antall for",kgForLager)
    if valg == '9':
        print(f'Antall foringer per dag: {antallForinger}')
        print(f'Antall merder : {antallMerder}')
        print(f'Antall kg for på lager: {kgForLager}')
        print(f'Størrelse på lager i Kg: {maksKgLager}')
        print(f'Prosentgrense for bestilling av for: {prosentGrense}')
        input()
    if valg == '0':
        break

