import shutil
ruta_original = "ruta/del/archivo_original.txt"
ruta_copia = "ruta/del/archivo_copia.txt"
shutil.copyfile(ruta_original, ruta_copia)

import filecmp
iguales = filecmp.cmp(ruta_original, ruta_copia)

if iguales:
    print("Los archivos son iguales")
else:
    print("Los archivos son diferentes")

