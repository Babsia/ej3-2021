class camion:
    __id=0
    __nombre=''
    __patente=''
    __marca=''
    __tara=0
    def __init__(self,id,nom,patente,marca,tara):
        if (0<id<21):
            self.__id=id
            self.__nombre=nom
            self.__patente=patente
            self.__marca=marca
            self.__tara=tara
    def __str__(self):
        return(self.__nombre)
    def gettara(self):
        return self.__tara
    def getpatente(self):
        return self.__patente
    def getnom(self):
        return self.__nombre

   

    