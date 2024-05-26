
class droga:

    def __init__(self, wierzcholekA, wierzcholekB, przeplywAktualny, przeplywMaksymalny):
        self.wierzcholekA = wierzcholekA
        self.wierzcholekB = wierzcholekB
        self.przeplywAktualny = przeplywAktualny
        self.przeplywMaksymalny = przeplywMaksymalny

def CzySciezka(krawedzie: droga, zrodlo, wyjscie):
    wierzcholkiA = []
    wierzcholkiB = []
    for krawedz in krawedzie:
        if (krawedz.wierzcholekA in wierzcholkiA) or (krawedz.wierzcholekB in wierzcholkiB):
            return "nieprawidlowy"
        wierzcholkiA.append(krawedz.wierzcholekA)
        wierzcholkiB.append(krawedz.wierzcholekB)
    if (len((set(wierzcholkiA) | set(wierzcholkiB)) - (set(wierzcholkiA) and set(wierzcholkiB))) > 2) | zrodlo not in (set(wierzcholkiA) | set(wierzcholkiB)) | wyjscie not in (set(wierzcholkiA) | set(wierzcholkiB)):
        return  "niedokonczony"
    return "prawidlowy"

def UsunKrawedzieZtakimWierzcholkiem(krawedzie: droga, wierzcholek):
    print("Usuwanie")
    print(wierzcholek)
    krawedzie = [krawedz for krawedz in krawedzie if krawedz.wierzcholekA != wierzcholek and krawedz.wierzcholekB != wierzcholek]
    return krawedzie

def WyszukajSciezke(krawedzie: droga, wierzcholek_poczatkowy, wierzcholek_koncowy):
    print("Nowe wywolanie")
    for krawedz in krawedzie:
        print(krawedz.wierzcholekA + " : " + krawedz.wierzcholekB)
    krawedziee=krawedzie.copy()
    for krawedz in krawedzie:
        sciezka = WyszukajSciezke(UsunKrawedzieZtakimWierzcholkiem(krawedziee, krawedz.wierzcholekA), krawedz.wierzcholekB, wierzcholek_koncowy)
        if ((krawedz.przeplywAktualny < krawedz.przeplywMaksymalny) and (krawedz.wierzcholekA == wierzcholek_poczatkowy)):
            if(krawedz.wierzcholekB == wierzcholek_koncowy):
                itemy = []
                itemy.append(krawedz)
                return itemy
            elif( sciezka != None):
                sciezka.append(krawedz)
                return sciezka
    return

class Flow:

    def __init__(self, wierzcholki, zrodlo, wyjscie, wagi):
        self.wierzcholki = sorted(wierzcholki)
        self.wagi = dict(sorted(wagi.items()))
        self.krawedzie = []
        self.zrodlo = zrodlo[0]
        self.wyjscie = wyjscie[0]
        for krawedz, wartosc in self.wagi.items():
            self.krawedzie.append(droga(krawedz[0], krawedz[1], 0, wartosc))
            self.krawedzie.append(droga(krawedz[1], krawedz[0], 0, 0))

    def Ford_Fulkerson(self):
        sciezka = WyszukajSciezke(self.krawedzie, self.zrodlo, self.wyjscie)
        for droga in sciezka:
            print(droga.wierzcholekA)
        
        
if __name__=="__main__":
    f = Flow(["a","b","c","d","e","f"],['a'],['e'],{('a','b'):3 ,('a','c'):10 , ('a','f'):15 , ('c','d'):7 , 
    ('c','e'):9 , ('b','d'):4, ('b','e'):25 , ('d','f'):5 , ('f','c'):5 , ('f','e'):6 })
    f.Ford_Fulkerson()