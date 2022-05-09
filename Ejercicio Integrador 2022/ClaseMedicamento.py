class Medicamentos:
    __idCama=''
    __idMedicamento=''
    __nomcom=''
    __monodroga=''
    __presentacion=''
    __cantapli=''
    __preciotot=''
    def __init__(self,idCama,idMedicamento,nomcom,monodroga,presentacion,cantapli,preciotot):
        self.__idCama=idCama
        self.__idMedicamento=idMedicamento
        self.__nomcom=nomcom
        self.__monodroga=monodroga
        self.__presentacion=presentacion
        self.__cantapli=cantapli
        self.__preciotot=preciotot
    def getidCama(self):
        return self.__idCama
    def getidMedicamento(self):
        return self.__idMedicamento
    def getnomcom(self):
        return self.__nomcom
    def getmonodroga(self):
        return self.__monodroga
    def getpresentacion(self):
        return self.__presentacion
    def getcantapli(self):
        return self.__cantapli
    def getpreciotot(self):
        return self.__preciotot