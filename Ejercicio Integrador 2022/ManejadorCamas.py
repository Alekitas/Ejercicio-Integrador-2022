from ClaseCama import Cama
import csv
import numpy as np
from datetime import datetime
class ManejadorCamas:
    __Dimension=0
    __Cantidad=0
    __Incremento=5
    
    def __init__(self,Dimension=5,Incremento=5):
        self.__cama=np.empty(Dimension,dtype=Cama)
        self.__Cantidad=0
        self.__Dimension=Dimension
        
    def AgregarCama(self,cama):
        if self.__Cantidad==self.__Dimension:
            self.__Dimension+=self.__Incremento
            self.__cama.resize(self.__Dimension)
        self.__cama[self.__Cantidad]=cama
        self.__Cantidad+=1
        
    def Iniciar(self):
        archivo=open('camas.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unaCama=Cama(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.AgregarCama(unaCama)
    def DatosDiagnostico(self,nompaciente,unManejadorM):
        i=0
        while nompaciente!=self.__cama[i].getnomyap():
            i+=1
        if nompaciente==self.__cama[i].getnomyap():
            fecha=datetime.today().strftime('%d/%m/%Y')
            print('Paciente: {nombre}        Cama: {cama}         Habitacion: {habitacion}         '.format(nombre=self.__cama[i].getnomyap(),cama=self.__cama[i].getidCama(),habitacion=self.__cama[i].gethabit()))
            print('Diagnostico: {diag}             Fecha de internacion: {fecha}'.format(diag=self.__cama[i].getdiagnos(),fecha=self.__cama[i].getfechaint()))
            print('Fecha de alta: {fec}'.format(fec=self.__cama[i].getfechaalt(fecha)))
            unManejadorM.DatosMedicamentos(self.__cama[i].getidCama())
            self.__cama[i].cambiarestado(False)
        else:
            print('\n--El paciente ingresado no existe--\n')
    def ListarPacientes(self,diagnostico):
        i=0
        while diagnostico!=self.__cama[i].getdiagnos():
            i+=1
            if diagnostico==self.__cama[i].getdiagnos():
                if self.__cama[i].getestado():
                    fecha=datetime.today().strftime('%d/%m/%Y')
                    print('Paciente: {nombre}        Cama: {cama}         Habitacion: {habitacion}         '.format(nombre=self.__cama[i].getnomyap(),cama=self.__cama[i].getidCama(),habitacion=self.__cama[i].gethabit()))
                    print('Diagnostico: {diag}             Fecha de internacion: {fecha}'.format(diag=self.__cama[i].getdiagnos(),fecha=self.__cama[i].getfechaint()))
                    print('Fecha de alta: {fec}'.format(fec=self.__cama[i].getfechaalt(fecha)))