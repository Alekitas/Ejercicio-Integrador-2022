class Cama:
    __idCama=''
    __habit=''
    __estado=bool
    __nomyap=None
    __diagnos=''
    __fechaint=''
    __fechaalt=''
    def __init__(self,idCama,habit,estado,nomyap,diagnos,fechaint,fechaalt):
        self.__idCama=idCama
        self.__habit=habit
        self.__estado=estado
        self.__nomyap=nomyap
        self.__diagnos=diagnos
        self.__fechaint=fechaint
        self.__fechaalt=fechaalt
    def getidCama(self):
        return self.__idCama
    def gethabit(self):
        return self.__habit
    def getestado(self):
        return self.__estado
    def getnomyap(self):
        return self.__nomyap
    def getdiagnos(self):
        return self.__diagnos
    def getfechaint(self):
        return self.__fechaint
    def getfechaalt(self,fecha):
        self.__fechaalt=fecha
        return self.__fechaalt
    def cambiarestado(self,false):
        self.__estado=False