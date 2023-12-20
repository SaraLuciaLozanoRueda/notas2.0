import os
import notas as notas
menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar estudiante\n4. Salir"
subMenuNotas = "1.Parciales\n2.Quices\n3.Trabajos\n4.Regresar al menu principal"
hasError = True
def menuPrincipal()-> int:
    global hasError
    hasError =True
    print(menu)
    while(hasError== True):
        try:
            return int(input(":)"))
        except ValueError:
            hasError=True    

def menuNotas(alumnos:dict):
    os.system("cls")
    header = """"""
    """"""""""""""""""""""""""""""""""""""""""
    """""""       MENU DE REGISTRO     """""""
    """"""""""""""""""""""""""""""""""""""""""
    isActiveMenu=True
    while(isActiveMenu):
        os.system("cls") 
        print(header)
        try:
            print (subMenuNotas)
            opMenu= int(input(":)"))
        except ValueError:
            print("opcion invalida..... Recuerde que son enteros")
        else:
                if(opMenu==1):
                    notas.addGrade(alumnos,"parciales")
                elif (opMenu==2):
                    notas.addGrade(alumnos,"quices") 
                elif (opMenu==3):
                    notas.addGrade(alumnos,"trabajos")
                elif (opMenu==4):
                    isActiveMenu=False
                else:
                    print ("La opcion ingresada es invalida")