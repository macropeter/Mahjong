import functools

werteliste={'Pon':2,'Poe':4,'Pvn':4,'Pve':8,
            'Kon':8,'Koe':16,'Kvn':16,'Kve':32,
            'TP':2}



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
    
    def __init__(self,ident):
        self.ident=ident
        self.__Gesamt=0
        self.__Saldo=0
        
    def BerechneSumme(self):
        global punktestand
        hilfliste=[werteliste[k]*getattr(self,k) for k in werteliste]
        self.__Gesamt=functools.reduce(lambda x,y: x+y,hilfliste)
        return self.__Gesamt

    def __str__(self):
        return self.name+':'+str(self.__Gesamt)

spielerliste=[spieler('Spieler1'),
              spieler('Spieler2'),
              spieler('Spieler3'),
              spieler('Spieler4')]

punkteliste={'Spieler1':0,
             'Spieler2':0,
             'Spieler3':0,
             'Spieler4':0}



def Update(punktestand):
    return [item.BerechneSumme() for item in spielerliste]


def RundeAbrechnung(werte,neu):
    "Eine Runde abrechnen, wer zahlt wem wieviel"
    zn=[0,0,0,0]
    ins=neu[0]+neu[1]+neu[2]+neu[3]
    zn[0]=ins-4*neu[0]
    zn[1]=ins-4*neu[1]
    zn[2]=ins-4*neu[2]
    zn[3]=ins-4*neu[3]
    return zn

dx=[8,4,14,26]
