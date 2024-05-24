
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
        if (len((set(wierzcholkiA) | set(wierzcholkiB)) - (set(wierzcholkiA) & set(wierzcholkiB))) > 2) | zrodlo not in (set(wierzcholkiA) | set(wierzcholkiB)) | wyjscie not in (set(wierzcholkiA) | set(wierzcholkiB)):
            return  "niedokonczony"
        return "prawidlowy"

class Flow:

    def __init__(self, wierzcholki, zrodlo, wyjscie, wagi):
        self.wierzcholki = sorted(wierzcholki)
        self.wagi = sorted(wagi)
        self.krawedzie = []
        self.zrodlo = zrodlo
        self.wyjscie = wyjscie
        for krawedz, wartosc in self.wagi.items():
            self.krawedzie.append(droga(krawedz[0], krawedz[1], 0, wartosc))
            self.krawedzie.append(droga(krawedz[1], krawedz[0], 0, 0))

    def WyszukajSciezke(self):
        wierzcholki = {}
        sciezka = []
        sciezka_tymczasowa = []
        for krawedz in self.krawedzie:
            sciezka_tymczasowa = sciezka.copy() + krawedz
            if (krawedz.przeplywAktualny < krawedz.przeplywMaksymalny) & (CzySciezka(sciezka_tymczasowa) == "prawidlowy") & (self.zrodlo in wierzcholki & self.wyjscie in wierzcholki):
                wierzcholki.add(krawedz.wierzcholekA)
                wierzcholki.add(krawedz.wierzcholekB)
            elif (krawedz.przeplywAktualny < krawedz.przeplywMaksymalny) & (CzySciezka(sciezka_tymczasowa) == "niedokonczony"):
                sad

    def Ford_Fulkerson(self):
        pass
        
        
if __name__=="__main__":
    f = Flow(["a","b","c","d","e","f"],["a"],["e"],{('a','b'):3 ,('a','c'):10 , ('a','f'):15 , ('c','f'):2 , ('c','d'):7 , 
    ('c','e'):9 , ('b','d'):4, ('b','e'):25 , ('d','f'):5 , ('d','c'):2 , ('f','c'):5 , ('f','e'):6 , ('f','d'):3})