from ManejadorCamas import ManejadorCamas
from ManejadorMedicamentos import ManejadorMedicamentos

if __name__=='__main__':
    unManejadorC=ManejadorCamas()
    unManejadorM=ManejadorMedicamentos()
    unManejadorC.Iniciar()
    unManejadorM.Iniciar()
    
    nompaciente=input('Ingrese un apellido y nombre de paciente: ')
    unManejadorC.DatosDiagnostico(nompaciente,unManejadorM)
    diagnostico=input('Ingrese un diagnostico: ')
    unManejadorC.ListarPacientes(diagnostico)