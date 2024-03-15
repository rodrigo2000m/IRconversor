# Conversor de archivos de LabSolutions IR a IRsolution
# Autor: Rodrigo Moreira
# Correo electrónico: rmoreira@fq.edu.uy
# Organización: Facultad de Química, UDeLaR
# Fecha de creación: 24.03.14
# Última modificación: 24.03.14

import os
import time

def IRconversor():
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("IRconversor")
    print("Este programa modifica los archivos .txt generados en el LabSolutions IR a .txt que pueden ser leidos por el IRsolution y convertidos en .smf para tratamiento de los espectros.")
    print("\n")

    ir_inp = input("Ingrese el nombre de la carpeta donde estan guardados los IRs que quiere convertir (absoluta o relativa): \n")
    ir_inps = os.listdir(ir_inp)

    print("\n Los archivos presentes en la carpeta son: \n ")

    for i in ir_inps:
        print(i)

    print("\n")
    process_files = input("Desea continuar? si/no \n")

    if process_files == "SI" or process_files == "si" or process_files == "Si" or process_files == "s" or process_files == "S":
        ir_out = input("Ingrese la ruta de la carpeta donde va a guardar los nuevos archivos (absoluta o relativa): \n")

        for file in ir_inps:
            current_path = os.path.join(ir_inp, file)
            ir_file = open(current_path, "r")
            
            new_var = ""
            for linea in ir_file:
                if "##TITLE" in linea or "##DATA TYPE" in linea or "##XUNITS" in linea:
                    continue
                else:
                    new_var+=linea
            
            new_var = new_var.replace(",", ".")

            out_path = os.path.join(ir_out, file)

            ir_out_file = open(out_path, "w")
            ir_out_file.write(new_var)
            ir_out_file.close()

            ir_file.close()

        print("Termino la conversion de los archivos.\n\nCuando abras los archivos .txt generados en el IRSolution se creara un archivo .smf automáticamente.")
        print("\n")
        print("----------------------------------------------------------------------------------------------------------------------------")
        time.sleep(2)
        IRconversor()
    else:
        time.sleep(2)
        IRconversor()

if __name__ == "__main__":
    IRconversor()

