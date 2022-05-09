from ClaseMedicamento import Medicamentos
import csv
class ManejadorMedicamentos:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def Iniciar(self):
        archivo=open('medicamentos.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unMedicamento=Medicamentos(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__lista.append(unMedicamento)
    def DatosMedicamentos(self,idcama):
        total=0
        print('Medicamento/monodroga Presentacion Cantidad Precio')
        for i in range(len(self.__lista)):
            if idcama==self.__lista[i].getidCama():
                print('{medicamento} {monodroga} {presentacion}    {cant}     {precio} '.format(medicamento=self.__lista[i].getnomcom(),monodroga=self.__lista[i].getmonodroga(),presentacion=self.__lista[i].getpresentacion(),cant=self.__lista[i].getcantapli(),precio=self.__lista[i].getpreciotot()))
                p=float(self.__lista[i].getpreciotot())
                total+=p
        print('Total Adeudado: ',total)