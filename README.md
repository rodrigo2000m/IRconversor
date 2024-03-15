# IRconversor
## Convertidor de Datos LabSolutions IR a IRsolution

Este script de Python convierte datos espectroscópicos generados por el programa LabSolutions IR en un formato compatible con IRsolution.

## Descarga

Puedes descargar este repositorio seleccionando el botón CODE y eligiendo "Download ZIP" o clonando el repositorio en la modalidad que prefieras.

## Uso

1. Ejecutar el archivo para tu sistema operativo desde la carpeta correspondiente:
   - **Para Windows:** [windows/dist/IR_conversor.exe](windows/dist/IR_conversor.exe)
   - **Para Linux:** [linux/dist/IR_conversor](linux/dist/IR_conversor)
2. También puedes acceder al código fuente en Python si prefieres:
   - [IR_conversor.py](IR_conversor.py)
4. Ejecuta el archivo `IR_conversor` o `IR_conversor.py` según tu preferencia.
5. Sigue las instrucciones para ingresar el nombre de la carpeta con los archivos de entrada y el nombre de la carpeta con los archivos de salida para IRsolution.
6. El programa generará los archivos de salida compatibles con IRsolution en el directorio seleccionado.
7. Los archivos `.txt` generados podrán leerse en el IRsolution y al abrirlos se genera de forma automática el archivo `.smf` correspondiente.

## Tests

En la carpeta `tests`, encontrarás espectros generados en LabSolutions IR y exportados como archivos `.txt`. Estos archivos pueden ser utilizados para probar el funcionamiento de `IR_conversor`. Una vez convertidos, los archivos generados podrán ser leídos por IRsolution, y se generarán archivos `.smf` de forma automática.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o deseas mejorar el script, no dudes en enviar un pull request o contactarme por correo.

## Contacto

Si tienes preguntas, comentarios o sugerencias, no dudes en contactarnos por correo electrónico:
- Correo electrónico: rmoreira@fq.edu.uy

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE), lo que significa que cualquiera puede utilizar, modificar y distribuir el código bajo los términos de dicha licencia.
