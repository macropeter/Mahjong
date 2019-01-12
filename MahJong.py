import functools

werteliste={'Pon':2,'Poe':4,'Pvn':4,'Pve':8,'Kon':8,'Koe':16,'Kvn':16,'Kve':32,'TP':2}
punktestand=[0,0,0,0]

class spieler:
    Pon=0
    Poe=0
    Pvn=0
    Pve=0
    Kon=0
    Koe=0
    Kvn=0
    Kve=0
    TP=0
    Gesamt=0
    Saldo=0
    
    def __init__(self,name):
        self.name=name
        
    def BerechneSumme(self):
        global punktestand
        hilfliste=[punktewertung[k]*getattr(spieler0,k) for k in punktewertung]
        self.Gesamt=functools.reduce(lambda x,y: x+y,hilfliste)
        return self.Gesamt

    def __str__(self):
        return self.name+':'+str(self.Gesamt)
        

spielerliste=[spieler('Spieler0'),
              spieler('Spieler1'),
              spieler('Spieler2'),
              spieler('Spieler3')]

def saldoBerechnung(werte,punkte,neu):
    
    zn=[0,0,0,0]
    ins=neu[0]+neu[1]+neu[2]+neu[3]
    zn[0]=ins-4*neu[0]
    zn[1]=ins-4*neu[1]
    zn[2]=ins-4*neu[2]
    zn[3]=ins-4*neu[3]
    
    
    for i in range(4):
        punkte[i]=punkte[i]+zn[i]
    
    return punkte

def NeuerSpielstand():
    global spielstand
    spielstand=[sp.Gesamt for sp in spielerliste]
    return spielstand

dx=[8,4,14,26]
